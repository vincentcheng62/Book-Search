# saved as greeting-server.py
#export PYRO_SERIALIZERS_ACCEPTED=serpent,json,marshal,pickle,dill
#SET PYRO_SERIALIZERS_ACCEPTED=serpent,json,marshal,pickle,dill

#python -m Pyro4.naming

import sys, requests, json, pymysql, re, urllib.error, Pyro4
from pprint import pprint
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
#from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from urllib.request import urlopen
from forex_python.converter import CurrencyRates, CurrencyCodes
from itertools import product
import easygui
from tablemodel import MyTableModel


registername = "booksearchrmi"

@Pyro4.expose
class Rmi_Connector(object):
	def __init__(self):
		self.dict_currency_ratio = {}
		
		#create a currency lookuptable so as to handle currency conversion later
		self.create_currency_dictionary()
		
	def convert_currency(self, in_currency, out_currency, in_price):
		out_price = in_price
		if (in_currency != out_currency):
			key = in_currency + ":" + out_currency
			out_price = in_price * self.dict_currency_ratio[key] 
			out_price = round(out_price,2)
		return out_price
		
	def create_currency_dictionary(self):
		currencylist = ["HKD", "USD", "JPY"]
		cr = CurrencyRates()
		for item in product(tuple(currencylist), repeat=2):
			in_currency = item[0]
			out_currency = item[1]
			if in_currency != out_currency:
				key = in_currency + ":" + out_currency
				ratio = cr.get_rate(in_currency, out_currency)
				self.dict_currency_ratio[key] = ratio
		print(self.dict_currency_ratio)
		
	def ConvertDictToJson(self, resultdictionary):
		itemlist=[]
		for key,value in resultdictionary.items():
			dicttemp={}
			dicttemp['ISBN'] = key
			dicttemp['booktitle'] = value[0]
			dicttemp['ourprice'] = value[1]
			dicttemp['googleprice'] = value[2]
			itemlist.append(dicttemp)
		return itemlist
		
	'''
	Server will response a json format:
	{
	  "items": [
		{
		  "ISBN": "1155068667",
		  "booktitle": "Python for beginner",
		  "ourprice": "",
		  "googleprice": "$USD 30"
		},
		{
		  "ISBN": "109873645",
		  "booktitle": "Design Pattern",
		  "ourprice": "HK$ 90",
		  "googleprice": ""
		}
	  ],
	  "status": "OK"
	}
	'''	
	
	def GetBookInfoFromGoogleAPI(self, search_method, keyword, out_currency_code, resultdictionary):
		if search_method == "ISBN10":
			url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(keyword)
		else: 
			url = "https://www.googleapis.com/books/v1/volumes?q=" + str(keyword) + "+intitle:" + str(keyword)

		print("open " + url)
		try:
			r = urlopen(url).read().decode('utf8')
			data = json.loads(r)
			
			if "items" in data:
				
				for item in data["items"]:
					#isbn10
					if "industryIdentifiers" in item["volumeInfo"]:
						isbns = item["volumeInfo"]["industryIdentifiers"]
						isbn10 = ""
						for i in range(0, len(isbns)):
							if isbns[i]["type"] == "ISBN_10":
								isbn10 = isbns[i]["identifier"]
						if isbn10 == "":
							continue
						
						# whether has sales info
						pricestring=''

						if "listPrice" in item["saleInfo"]:
							price = item["saleInfo"]["listPrice"]["amount"]
							currency_code = item["saleInfo"]["listPrice"]["currencyCode"]
							out_price = self.convert_currency(currency_code, out_currency_code, price)
							pricestring = out_currency_code + str(out_price)

						if "saleability" in item["saleInfo"]:
							if pricestring == '':
								pricestring = "NotForSale" #item["saleInfo"]["saleability"]


						if isbn10 in resultdictionary:
							resultdictionary[isbn10][2] = pricestring
						else: 
							resultdictionary[isbn10] = [item["volumeInfo"]["title"], 'Not in DB', pricestring]

			else:
				print("No books are found!")
				#return json.dumps({'status': 'No books are found!'})
			
		except urllib.error.URLError as e:
			print(e.code)
			return 'HTTP error!'
	
		return "OK"
		
	def GetBookInfoByKeyword(self, keyword, search_method, out_currency_code):
		
		try:
			# Load the saved user login info
			with open('dbinfo.json') as f:
				logininfo = json.load(f)
		except Exception as e:
			print (e)
			return json.dumps({'status': 'Missing login mysql datafile'})		
		
		try:
			conn = pymysql.connect(host='localhost', port=3306, user=logininfo["username"], passwd=logininfo["password"], db='mysql')
		except Exception as e:
			print (e)
			return json.dumps({'status': 'Mysql connection fail!'})
		
		try:
			cur = conn.cursor()
			print("connected to the database successfully")
			print(keyword)
			if search_method == "ISBN10":
				query = "SELECT ISBN10, TITLE, SALE_PRICE FROM mysql.adebookdb WHERE ISBN10 = %s and TITLE != 'None'"
				keyworddb = re.sub('[\+]+','',keyword)
			else:
				query = "SELECT ISBN10, TITLE, SALE_PRICE FROM mysql.adebookdb WHERE KEYOWRD RLIKE %s and TITLE != 'None'"
				keyworddb = re.sub('[\+]+',' ',keyword)
	
			params = (keyworddb, )
			cur.execute(query, params)
			print("Query successfully")

			result = cur.fetchall()

			cur.close()
			
		except Exception as e:
			print (e)
			return json.dumps({'status': 'Mysql query fail!'})
			
		finally:
			conn.close()
		
		
		#Create a dictionary with key=ISBN and value=['name', 'databaseprice', 'googleprice']
		# result : []
		resultdictionary = {}
		for row in result:
			result_isbn10 = row[0]
			result_title = row[1]
			result_db_price_usd = row[2]
			if result_db_price_usd != "None":
				result_db_price_usd = re.sub('[^0-9.]+', '', result_db_price_usd)
				result_db_price = self.convert_currency("USD", out_currency_code, float(result_db_price_usd))
				result_db_price_string = out_currency_code + str(result_db_price)
			else:
				result_db_price_string = "None"
			resultdictionary[result_isbn10] = [result_title, result_db_price_string, '']
		
		#--------------
		# Google API
		#--------------
		# Search by keyword in google api 
		returnstring = self.GetBookInfoFromGoogleAPI(search_method, keyword, out_currency_code, resultdictionary)
		if returnstring != "OK":
			return json.dumps({'status': returnstring})
		
		# Search the item in dictionary, but not serached above 
		for key, value in resultdictionary.items():
			if value[0] == "None" or value[2] == "":
				self.GetBookInfoFromGoogleAPI("ISBN10", key, out_currency_code, resultdictionary)
			
		#convert resultdictionary to itemlist
		if len(resultdictionary) > 0:
			itemlist = self.ConvertDictToJson(resultdictionary)
			return json.dumps({'status': 'OK', 'items': itemlist})
		else:
			return json.dumps({'status': 'No books are found!'})




daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Rmi_Connector)   # register the greeting maker as a Pyro object
ns.register(registername, uri)   # register the object with a name in the name server

print("Ready to accept client...")
print("The name registered in the name server is: " + registername)
daemon.requestLoop()                   # start the event loop of the server to wait for calls
