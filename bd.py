import mysql.connector
import adodbapi
from mysql.connector import Error
import pyodbc
import MySQLdb
def connect():
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')


            if conn.is_connected():
                print('Connected to MySQL database')
                cursor = conn.cursor()
                #sql="SELECT column_name FROM information_schema.columns where table_schema='telephon_bas' and table_name='telephon';"
               # cursor.execute(sql)
                #columns=cursor.fetchall()
                #if(self.entry_Data_finish.get()!=''):
                 #   sql = "INSERT INTO telephon_bas.telephon (Name, Zena, Akkum, Data_begin, Data_finish, proizvod_Name, type_Name, Ekran_Diagonal, Ekran_PIX_inch, color_Name) VALUES (`" + self.entry_Name.get() + "`, `" + self.entry_Price.get() + "`, `" + self.entry_Akkum.get() + "`, `" + self.entry_Data_start.get() + "`, `" + self.entry_Data_finish.get() + "`, `" + self.entry_Name_proizvod.get() + "`, `" + self.entry_type_Name.get() + "`, `" + self.entry_Ekran_Diagonal.get() + "`, `" + self.entry_Ekran_pix.get() + "`, `" + self.entry_color_Name.get() + "`);"
                #else:
               #sql = "insert into telephon(%s) values(" + self.entry_Name.get() + ", " + self.entry_Price.get() + ", " + self.entry_Akkum.get() + ", " + self.entry_Data_start.get() + ", " + self.entry_Name_proizvod.get() + ", " + self.entry_type_Name.get() + ", " + self.entry_Ekran_Diagonal.get() + ", " + self.entry_Ekran_pix.get() + ", " + self.entry_color_Name.get() + ");" % (columns)
                    #cursor.execute(sql)
                #sql = "UPDATE color set sex = male where id=1;"
                sql = "select * from telephon_bas.telephon;"
                cursor.execute(sql)
                result = cursor.fetchall()

                for item in result:
                    print(item)
                conn.close()
        except Error as e:
            print(e)

        finally:
            conn.close()



if __name__ == '__main__':
    connect()
