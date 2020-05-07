import mysql.connector

try:
  cnx = mysql.connector.connect(user='root',password='', database='telephon_bas')
  cursor = cnx.cursor()
  cursor.execute("SELECT * FROM telephon_bas.telephon")  
  cnx.close()
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))
