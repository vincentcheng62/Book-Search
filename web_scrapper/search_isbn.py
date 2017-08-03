# This file reads keywords from "keywords_list.txt"
# Search the ISBN10 from those keywords 
# Output: "keywords_ISBN10.json"


import isbnlib
import json


with open("keywords_list.txt", "r") as f:
	keyword_list = []
	for line in f:
		keyword_list.append(line)

extracted_data = []
for word in keyword_list:
	word = word.rstrip()
	booklist = isbnlib.goom(word) #booklist is a list of dictionary

	for i in range(0, len(booklist)-1):
		isbn_13 = booklist[i]['ISBN-13']
		isbn_10 = isbnlib.to_isbn10(isbn_13)

		is_valid_isbn10 = isbnlib.is_isbn10(isbn_10)
		if isbnlib.is_isbn10(isbn_10) == True:
			data = {
                    'ISBN10':isbn_10,
                    'KEYOWRD':word,
                    }
			extracted_data.append(data)
		else:
			print ("Invalid isbn10:", isbn_10)

f = open('keywords_ISBN10.json','w')
json.dump(extracted_data,f,indent=4)