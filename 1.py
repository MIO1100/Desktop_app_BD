import mysql.connector
conn= pymysql.connect(host='localhost',port=3306,user='root',passwd='toor',db='telephon_bas')
a=conn.cursor()
sql='SELECT * from `from`;'
a.execute(sql)
countrow= a.execute(sql)
print("Number of rows:", countrow)
data=a.fetchone()
print(data)
