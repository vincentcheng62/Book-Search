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


# to install it to executable
# pyinstaller --onefile book_search.py


qtCreatorFile = "book_search_table.ui"

# load the ui dynamically by using the ui compiler provided by Qt
try:
	Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
except Exception as e:
	print (e)
	# prompt a warning message box
	easygui.msgbox("The .ui material for the client is not found!")
			


#Class for the ui, contains controller to handle user interaction (e.g. button click)
class MyApp(QtWidgets.QDialog, Ui_MainWindow):

	def process_input_string(self, input):
		title = re.sub('[^A-Za-z0-9]+', '+', input)
		#return re.findall("[A-Za-z0-9]+", title)		
		return title

	def select_currency_change(self,i):
		#self.getbookbytitle()
		self.out_currency_code = self.CurrencyComboBox.currentText()
		char = self.process_input_string(self.lineEdit_input.text())
		if len(char) > 0 and self.tableView.columnWidth(0) > 0:  # if there is previous search record
			self.getbookbytitle()
		
	def btnstate_search_method(self,b):
		self.search_method = b.text()
		
	def CalculateLowerPrice(self, price1, price2):
		if re.findall("[0-9]+", price1) == []:
			return price2
		elif re.findall("[0-9]+", price2) == []:
			return price1
		else:
			if float(re.sub('[A-Za-z]+', '', price1)) > float(re.sub('[A-Za-z]+', '', price2)):
				return price2
			else:
				return price1

	#Function to be invoked when user submit the search
	def getbookbytitle(self):
		char = self.process_input_string(self.lineEdit_input.text())
		if len(re.findall("[A-Za-z0-9]+", char)) > 0: #if user really type in something
		
			#Do RMI to invoke the book search function in the server
			#Server will response in json and the client handle and display the result
			#as table format
			try:
				server_response = self.server_connector.GetBookInfoByKeyword(char, self.search_method, self.out_currency_code)
			except Exception as e:
				print (e)
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Warning)
				msg.setText('Lost connection to RMI server!')
				msg.exec_()
				sys.exit()
			
			servermessage = json.loads(server_response)
			if servermessage['status'] != 'OK':
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Warning)
				msg.setText(servermessage['status'])
				msg.exec_()
				
			else:
				header = ['ISBN', 'Title', 'Database price', 'Google API price', 'Lower price']
				
				data = []
				for bookitem in servermessage['items']:
					data.append([bookitem['ISBN'], bookitem['booktitle'], bookitem['ourprice'], 
					bookitem['googleprice'], self.CalculateLowerPrice(bookitem['ourprice'], bookitem['googleprice'])])
				
				tablemodel = MyTableModel(data, header, self)
				self.tableView.setModel(tablemodel)
				self.tableView.setColumnWidth(1, 160)
		
		#user input sth, but after processing becomes none, it means user input invalid string
		elif len(char) > 0 :
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText('Invalid Input String!')
			msg.exec_()
			
		
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		
		self.pushButton_search.clicked.connect(self.getbookbytitle)
		
		#Currency
		self.CurrencyComboBox.addItems(["HKD", "USD", "JPY"])
		self.CurrencyComboBox.currentIndexChanged.connect(self.select_currency_change)
		self.out_currency_code = self.CurrencyComboBox.itemText(0)

		#Logo 
		pixmap = QPixmap( "book_logo.gif")
		pixmap = pixmap.scaled(105, 105, QtCore.Qt.KeepAspectRatio)
		self.label_logo.setPixmap(pixmap)
		self.label_logo.show()
		
		#Search method (title/isbn10)
		self.search_method = "Title"
		self.radioButton_title.toggled.connect(lambda:self.btnstate_search_method(self.radioButton_title))
		self.radioButton_isbn10.toggled.connect(lambda:self.btnstate_search_method(self.radioButton_isbn10))
		
		self.server_connector = Pyro4.Proxy("PYRONAME:booksearchrmi")    # use name server object lookup uri shortcut

			
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setFixedSize(window.size())
    window.show()
    sys.exit(app.exec_())
