from lxml import html  
import json
import requests
from time import sleep
 
def AdebooksParser(url, isbn, keyword):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url,headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h2/a/span/text()'
            XPATH_SALE_PRICE = '//div[@class="item-price"]/span[@class="price"]/text()'

            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)

            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None

            if page.status_code!=200:
                raise ValueError('captha')
            data = {
                    'ISBN10':isbn,
                    'KEYOWRD':keyword,
                    'TITLE':NAME,
                    'SALE_PRICE':SALE_PRICE,
                    }
 
            return data
        except Exception as e:
            print (e)
 
def ReadIsbn():
	with open('keywords_ISBN10.json') as f:
		IsbnList = json.load(f)
		
	extracted_data = []
	for i in IsbnList:
		url = "https://www.abebooks.com/servlet/SearchResults?ds=1&isbn="+i["ISBN10"]
		print ("Processing: ",url)
		extracted_data.append(AdebooksParser(url, i["ISBN10"], i["KEYOWRD"]))
		sleep(2)
	f=open('adebookDB.json','w')
	json.dump(extracted_data,f,indent=4)
	
if __name__ == "__main__":
    ReadIsbn()
