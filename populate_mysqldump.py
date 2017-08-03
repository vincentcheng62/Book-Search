import subprocess, pymysql, json, os

#ask user to input their username and password of his mysql server so that we can 
#help him to populate the mysql dump to his database
USER = input("Please input the login username of your mysql server: ")
PASSWORD = input("Please input the login password of your mysql server: ")

DbName = "mysql"

#Since user may not run this script from the directory where this script is located
#Add the absolute directory here as a protection
absdir = os.path.dirname(os.path.abspath(__file__))
sqlfile = os.path.join(absdir, "adebooks.sql")
cmd = "mysql " + DbName + " -u" + USER + " -p" + PASSWORD + " < " + sqlfile
print(cmd)
proc = subprocess.Popen(cmd, shell = True)
stdout, stderr = proc.communicate()

#save the user login data so as to login to the database by our python code later       
log_data = {'username':USER, 'password':PASSWORD}
f=open('dbinfo.json','w')
json.dump(log_data,f,indent=4)

# print out the database content just for confirmation
print ("\nThe database details: ")

conn = pymysql.connect(host='localhost', port=3306, user=USER, passwd=PASSWORD, db=DbName)
cur = conn.cursor()
query = "SELECT * FROM %s.adebookdb" % DbName
cur.execute(query)

for row in cur:
	print(row)

cur.close()
conn.close()
