# Book-Search
A book search software that combine web scrapping result from adebook.com and google book

Screenshot:
![alt tag](https://github.com/vincentcheng62/Book-Search/blob/master/screenshot.png)


Installation 
(1) Install Python3.4 (Anaconda is recommended)
(2) Install Pyro4 (for Pyro server)
$pip install pyro4
(3) Install mysql (a localhost on port 3306)
(4) install pymysql
$pip install PyMySql


Run the application 
1.	Populate our test data (adebooks.sql) to your mysql server
$ python populate_mysqldump.py

2.	Startup the Pyro server
$ python -m Pyro4.naming
$ python rmiserver.py

3.	Start the application 
$ python book_search.py
Or 
Launch the executables: book_search.exe 


** Notes: the adebook.sql was created by web scrapping, that extract book price from the web 
The regarded scripts are in  ./web_scrapper
a. prepare "keywords_list.txt", which includes the keywords 
b. run "search_isbn.py", output: "keywords_ISBN10.json"
	python search_isbn.py
c. run "abebooks_scraper_Python3.py", output: "adebookDB.json"
	python abebooks_scraper_Python3.py
d. import "adebookDB.json" into MySQL
e. export the data as *.sql

The MySQL database have book information with te following keywords: 
python
database
perl
sql
data mining
parallel computing
statistics
technology
robotics
data structures
information
computer vision
