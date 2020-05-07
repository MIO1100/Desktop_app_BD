import MySQLdb

con=MySQLdb.connect(host="localhost",user="root",passwd="root",db="telephon_bas",charset='utf8')
print (con)
cur=db.cursor()
cur= execute("select  Name")
for item in cur.fetchall():
    print (item)
