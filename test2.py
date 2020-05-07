import tkinter as tk
import  datetime
from tkinter import ttk
from tkinter import *
import mysql.connector
import MySQLdb
from mysql.connector import Error
from tkinter import messagebox
from tkinter import filedialog as fd
x=0
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        #ДОБАВЛЕНИЕ ТУЛБАРА ДОБАВИТЬ
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)
        btn_delete = tk.Button(toolbar, text='Удалить запись', command=self.delete, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_delete.pack(side=tk.LEFT)
        btn_doc = tk.Button(toolbar, text='Вывод', command=self.doc, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_doc.pack(side=tk.LEFT)
        #ДОБАВИЛИ
        #Выбор таблицы
        self.combobox = ttk.Combobox(self, values=[u'Телефоны', u'Цвета', u'Типы', u'Производители', u'Экраны'])
        #
        self.lablel_description = tk.Label(self, text='Выбор таблицы').pack(fill=tk.BOTH)
        self.combobox.current(0)
        self.combobox.pack(fill=tk.BOTH)
        self.but_cmena_tab = Button(self)
        self.but_cmena_tab["text"] = "Обновить"
        self.but_cmena_tab.bind("<Button-1>", self.MAIN_TABL)
        self.but_cmena_tab.pack(fill=tk.BOTH)
        #ДОБАВЛЕНИЕ ВЬЮ ( таблица вывода результата запроса
        self.tree = ttk.Treeview(self, columns=('ID_telephon', 'Name', 'Price', 'Akkum', 'Data_begining', 'Data_finish',
                                                'proizvod_Name', 'type_Name', 'Ekran_Diagonal', 'Ekran_PIX_inch',
                                                'color_Name'), height=13, show='headings')
        self.tree.column('ID_telephon', width=20,anchor=tk.CENTER)
        self.tree.column('Name', width=120, anchor=tk.CENTER)
        self.tree.column('Price', width=40, anchor=tk.CENTER)
        self.tree.column('Akkum', width=135, anchor=tk.CENTER)
        self.tree.column('Data_begining', width=150, anchor=tk.CENTER)
        self.tree.column('Data_finish', width=150, anchor=tk.CENTER)
        self.tree.column('proizvod_Name', width=150, anchor=tk.CENTER)
        self.tree.column('type_Name', width=85, anchor=tk.CENTER)
        self.tree.column('Ekran_Diagonal', width=65, anchor=tk.CENTER)
        self.tree.column('Ekran_PIX_inch', width=120, anchor=tk.CENTER)
        self.tree.column('color_Name', width=100, anchor=tk.CENTER)

        self.tree.heading('ID_telephon', text='ID')
        self.tree.heading('Name', text='Название телефона')
        self.tree.heading('Price', text='Цена')
        self.tree.heading('Akkum', text='Ёмкость аккумулятора')
        self.tree.heading('Data_begining', text='Дата начала производства')
        self.tree.heading('Data_finish', text='Дата окончания производства')
        self.tree.heading('proizvod_Name', text='Название производителя')
        self.tree.heading('type_Name', text='название типа')
        self.tree.heading('Ekran_Diagonal', text='Диагональ экрана')
        self.tree.heading('Ekran_PIX_inch', text='Пикселей на дюйм')
        self.tree.heading('color_Name', text='Основной цвет')
        #получение данных

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')
            if conn.is_connected():
                print('Connected to MySQL database')
                if(self.combobox.get()=="Телефоны"):
                    sql = "select * from telephon_bas.telephon;"
                elif(self.combobox.get()=="Производители"):
                    sql = "select * from telephon_bas.proizvod;"
                elif(self.combobox.get()=="Цвета"):
                    sql = "select * from telephon_bas.color;"
                elif(self.combobox.get()=="Типы"):
                    sql = "select * from telephon_bas.type;"
                elif(self.combobox.get()=="Экраны"):
                    sql = "select * from telephon_bas.Ekran;"
                cursor = conn.cursor()

                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    self.tree.insert('', 'end', values=row)
                self.tree.yview()
                self.tree.pack(side=TOP, fill=X)
        except Error as e:
            messagebox.showerror('Error', '%s' % e)
            exit()
        finally:
            conn.close()

    def MAIN_TABL(self,event):
        self.tree.destroy()
        if(self.combobox.get()=="Телефоны"):
            self.tree = ttk.Treeview(self,
                                     columns=('ID_telephon', 'Name', 'Price', 'Akkum', 'Data_begining', 'Data_finish',
                                              'proizvod_Name', 'type_Name', 'Ekran_Diagonal', 'Ekran_PIX_inch',
                                              'color_Name'), height=13, show='headings')
            self.tree.column('ID_telephon', width=20, anchor=tk.CENTER)
            self.tree.column('Name', width=120, anchor=tk.CENTER)
            self.tree.column('Price', width=40, anchor=tk.CENTER)
            self.tree.column('Akkum', width=135, anchor=tk.CENTER)
            self.tree.column('Data_begining', width=150, anchor=tk.CENTER)
            self.tree.column('Data_finish', width=150, anchor=tk.CENTER)
            self.tree.column('proizvod_Name', width=150, anchor=tk.CENTER)
            self.tree.column('type_Name', width=85, anchor=tk.CENTER)
            self.tree.column('Ekran_Diagonal', width=65, anchor=tk.CENTER)
            self.tree.column('Ekran_PIX_inch', width=120, anchor=tk.CENTER)
            self.tree.column('color_Name', width=100, anchor=tk.CENTER)

            self.tree.heading('ID_telephon', text='ID')
            self.tree.heading('Name', text='Название телефона')
            self.tree.heading('Price', text='Цена')
            self.tree.heading('Akkum', text='Ёмкость аккумулятора')
            self.tree.heading('Data_begining', text='Дата начала производства')
            self.tree.heading('Data_finish', text='Дата окончания производства')
            self.tree.heading('proizvod_Name', text='Название производителя')
            self.tree.heading('type_Name', text='название типа')
            self.tree.heading('Ekran_Diagonal', text='Диагональ экрана')
            self.tree.heading('Ekran_PIX_inch', text='Пикселей на дюйм')
            self.tree.heading('color_Name', text='Основной цвет')
        elif(self.combobox.get()=="Типы"):
            self.tree = ttk.Treeview(self,
                                     columns=('ID', 'Name'), height=13, show='headings')
            self.tree.column('ID', width=20, anchor=tk.CENTER)
            self.tree.column('Name', width=120, anchor=tk.CENTER)
            self.tree.heading('ID', text='ID')
            self.tree.heading('Name', text='Название')
        elif(self.combobox.get()=="Цвета"):
            self.tree = ttk.Treeview(self,
                                     columns=('ID', 'Name'), height=13, show='headings')
            self.tree.column('ID', width=20, anchor=tk.CENTER)
            self.tree.column('Name', width=120, anchor=tk.CENTER)
            self.tree.heading('ID', text='ID')
            self.tree.heading('Name', text='Название')
        elif( self.combobox.get()=="Производители"):
            self.tree = ttk.Treeview(self,
                                     columns=('ID', 'Name'), height=13, show='headings')
            self.tree.column('ID', width=20, anchor=tk.CENTER)
            self.tree.column('Name', width=120, anchor=tk.CENTER)
            self.tree.heading('ID', text='ID')
            self.tree.heading('Name', text='Название')
        elif(self.combobox.get()=="Экраны"):
            self.tree = ttk.Treeview(self,
                                     columns=('ID', 'Diagonal', 'PIX_inch'), height=13, show='headings')
            self.tree.column('ID', width=20, anchor=tk.CENTER)
            self.tree.column('Diagonal', width=120, anchor=tk.CENTER)
            self.tree.column('PIX_inch', width=120, anchor=tk.CENTER)
            self.tree.heading('ID', text='ID')
            self.tree.heading('Diagonal', text='Диагональ')
            self.tree.heading('PIX_inch', text='Пикселей в дюйме')

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')
            if conn.is_connected():
                print('Connected to MySQL database')
                if(self.combobox.get()=="Телефоны"):
                    sql = "select * from telephon_bas.telephon;"
                elif(self.combobox.get()=="Производители"):
                    sql = "select * from telephon_bas.proizvod;"
                elif(self.combobox.get()=="Цвета"):
                    sql = "select * from telephon_bas.color;"
                elif(self.combobox.get()=="Типы"):
                    sql = "select * from telephon_bas.type;"
                elif(self.combobox.get()=="Экраны"):
                    sql = "select * from telephon_bas.Ekran;"
                cursor = conn.cursor()

                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    self.tree.insert('', 'end', values=row)
                self.tree.yview()
                self.tree.pack(side=TOP, fill=X)
        except Error as e:
            messagebox.showerror('Error', '%s' % e)
            exit()
        finally:
            conn.close()
    def open_dialog(self):
        Child()
    def delete(self):
        Child_delete()
    def doc(self):
        Child_doc()


        #ДОЧЕРНЕЕ ОКНО ДОБАВЛЕНИЯ
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()


    def init_child(self):
        #Обшие параметры дочернего окна
        self.title("Добавить запись")
        self.geometry('1050x100+300+200')
        self.resizable(False, False)
        #виджеты
        self.combobox = ttk.Combobox(self, values=[u'Телефоны', u'Цвета', u'Типы', u'Производители', u'Экраны'])
        #
        lablel_description = tk.Label(self, text='Выбор таблицы')
        lablel_description.place(x=0, y=0)
        self.combobox.current(0)
        self.combobox.place(x=100, y=0)
        #2 кнопка выбора
        self.but_cmena_tab = Button(self)
        self.but_cmena_tab["text"] = "Обновить"
        self.but_cmena_tab.bind("<Button-1>", self.telephon)
        self.but_cmena_tab.pack()
        self.but_cmena_tab.place(x=250, y=0)

        #кнопка
        self.but_create_tele = Button(self)
        self.but_create_tele["text"] = "Добавить"
        self.but_create_tele.bind("<Button-1>", self.new)
        self.but_create_tele.pack()
        self.but_create_tele.place(x=350, y=0)

        self.grab_set()
        self.focus_set()
        root.mainloop()
    def telephon(self,event):
        #удаление виджетов прошлого запроса
        global x
        x=x+1
        if(x>=2):
            self.lablel_Name.destroy()
            self.entry_Name.destroy()
            self.lablel_price.destroy()
            self.entry_Price.destroy()
            self.lablel_Akkum.destroy()
            self.entry_Akkum.destroy()
            self.lablel_start.destroy()
            self.entry_Data_start.destroy()
            self.lablel_finish.destroy()
            self.entry_Data_finish.destroy()
            self.lablel_proizv.destroy()
            self.combobox_proizv.destroy()
            self.lablel_type.destroy()
            self.combobox_type.destroy()
            self.lablel_Disgonal.destroy()
            self.combobox_diagonal.destroy()
            self.lablel_PIX.destroy()
            self.combobox_PIX.destroy()
            self.lablel_color.destroy()
            self.combobox_color.destroy()
        #конец удаления
        #Условия использования виджетов
        if(self.combobox.get()=="Телефоны"):
            self.lablel_Name = tk.Label(self, text='Название телефона')
            self.lablel_Name.place(x=0, y=25)
            self.entry_Name = ttk.Entry(self)
            self.entry_Name.place(x=0, y=55)

            self.lablel_price = tk.Label(self, text='Цена')
            self.lablel_price.place(x=100, y=25)
            self.entry_Price = ttk.Entry(self)
            self.entry_Price.place(x=100, y=55)

            self.lablel_Akkum = tk.Label(self, text='Ёмкость аккумулятора')
            self.lablel_Akkum.place(x=200, y=25)
            self.entry_Akkum = ttk.Entry(self)
            self.entry_Akkum.place(x=200, y=55)

            self.lablel_start = tk.Label(self, text='Дата начала')
            self.lablel_start.place(x=300, y=25)
            self.entry_Data_start = ttk.Entry(self)
            self.entry_Data_start.place(x=300, y=55)

            self.lablel_finish = tk.Label(self, text='Дата окончания')
            self.lablel_finish.place(x=400, y=25)
            self.entry_Data_finish = ttk.Entry(self)
            self.entry_Data_finish.place(x=400, y=55)

            self.lablel_proizv = tk.Label(self, text='Производитель')
            self.lablel_proizv.place(x=500, y=25)

            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='telephon_bas',
                                               user='root',
                                               password='')
                cursor = conn.cursor()
                if conn.is_connected():
                    sql="SELECT Name FROM proizvod"
                cursor.execute(sql)
                result = cursor.fetchall()
            except Error as e:
                messagebox.showerror('Error', '%s' % e)
                exit()

            finally:
                conn.close()
            self.combobox_proizv = ttk.Combobox(self, width=12)
            self.combobox_proizv['values']=result
            self.combobox_proizv.current(0)
            self.combobox_proizv.place(x=500, y=55)

            self.lablel_type = tk.Label(self, text='Тип')
            self.lablel_type.place(x=600, y=25)

            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='telephon_bas',
                                               user='root',
                                               password='')
                cursor = conn.cursor()
                if conn.is_connected():
                    sql="SELECT Name FROM type"
                cursor.execute(sql)
                result = cursor.fetchall()
            except Error as e:
                messagebox.showerror('Error', '%s' % e)
                exit()

            finally:
                conn.close()
            self.combobox_type = ttk.Combobox(self, width=12)
            self.combobox_type['values']=result
            self.combobox_type.current(0)
            self.combobox_type.place(x=600, y=55)

            self.lablel_Disgonal = tk.Label(self, text='Диагональ')
            self.lablel_Disgonal.place(x=700, y=25)

            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='telephon_bas',
                                               user='root',
                                               password='')
                cursor = conn.cursor()
                if conn.is_connected():
                    sql="SELECT Diagonal FROM Ekran"
                cursor.execute(sql)
                result = cursor.fetchall()
            except Error as e:
                messagebox.showerror('Error', '%s' % e)
                exit()

            finally:
                conn.close()
            self.combobox_diagonal = ttk.Combobox(self, width=12)
            self.combobox_diagonal['values']=result
            self.combobox_diagonal.current(0)
            self.combobox_diagonal.place(x=700, y=55)

            self.lablel_PIX = tk.Label(self, text='Пиксели на дюйм')
            self.lablel_PIX.place(x=800, y=25)

            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='telephon_bas',
                                               user='root',
                                               password='')
                cursor = conn.cursor()
                if conn.is_connected():
                    sql="SELECT PIX_inch FROM Ekran"
                cursor.execute(sql)
                result = cursor.fetchall()
            except Error as e:
                messagebox.showerror('Error', '%s' % e)
                exit()

            finally:
                conn.close()
            self.combobox_PIX = ttk.Combobox(self, width=12)
            self.combobox_PIX['values']=result
            self.combobox_PIX.current(0)
            self.combobox_PIX.place(x=800, y=55)

            self.lablel_color = tk.Label(self, text='Цвет')
            self.lablel_color.place(x=900, y=25)

            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='telephon_bas',
                                               user='root',
                                               password='')
                cursor = conn.cursor()
                if conn.is_connected():
                    sql="SELECT Name FROM color"
                cursor.execute(sql)
                result = cursor.fetchall()
            except Error as e:
                messagebox.showerror('Error', '%s' % e)
                exit()

            finally:
                conn.close()
            self.combobox_color = ttk.Combobox(self, width=12)
            self.combobox_color['values']=result
            self.combobox_color.current(0)
            self.combobox_color.place(x=900, y=55)

        elif(self.combobox.get()=="Цвета"):
            self.lablel_Name = tk.Label(self, text='Название цвета')
            self.lablel_Name.place(x=0, y=25)
            self.entry_Name = ttk.Entry(self)
            self.entry_Name.place(x=0, y=55)
        elif (self.combobox.get() == "Типы"):
            self.lablel_Name = tk.Label(self, text='Название типа')
            self.lablel_Name.place(x=0, y=25)
            self.entry_Name = ttk.Entry(self)
            self.entry_Name.place(x=0, y=55)
        elif (self.combobox.get() == "Производители"):
            self.lablel_Name = tk.Label(self, text='Производитель')
            self.lablel_Name.place(x=0, y=25)
            self.entry_Name = ttk.Entry(self)
            self.entry_Name.place(x=0, y=55)
        elif (self.combobox.get() == "Экраны"):
            self.lablel_Name = tk.Label(self, text='Дюймы')
            self.lablel_Name.place(x=0, y=25)
            self.entry_Name = ttk.Entry(self)
            self.entry_Name.place(x=0, y=55)
            self.lablel_price = tk.Label(self, text='Пикселей на дюйм')
            self.lablel_price.place(x=100, y=25)
            self.entry_Price = ttk.Entry(self)
            self.entry_Price.place(x=100, y=55)
        self.grab_set()
        self.focus_set()
        root.mainloop()
    def new(self, event):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            if conn.is_connected():
                print('Connected to MySQL database')
                if(self.combobox.get()=="Телефоны"):
                    sql="select Name from telephon;"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    if any(self.entry_Name.get() in s for s in result):
                        messagebox.showerror('Error:', ' Название повторяется')
                        exit()
                    if(len(self.entry_Name.get())==0 | len(self.entry_Price.get())==0 | len(self.entry_Data_start.get())==0 | len(self.entry_Akkum.get())==0):
                        messagebox.showerror('Error:', ' данные не введены')
                        exit()
                    #now = datetime.datetime.now()
                    #now=now.strftime("%Y-%m-%d")
                    #datetime.date.=self.entry_Data_start
                    #t=self.entry_Data_finish.get()
                    if(self.entry_Data_start.get()>self.entry_Data_finish.get() ):
                        if self.entry_Data_finish.get():
                            messagebox.showerror('Error:', ' ошибка в дате ')
                            exit()
                    if not self.entry_Data_start.get():
                        messagebox.showerror('Error:', ' ошибка в дате ')
                        exit()
                    tabl="telephon"
                    if (self.entry_Data_finish.get() != '' ):
                        sql = "INSERT INTO " + tabl + " (Name, Zena, Akkum, Data_begin, Data_finish, proizvod_Name, type_Name, Ekran_Diagonal, Ekran_PIX_inch, color_Name) VALUES ('" + self.entry_Name.get() + "', " + self.entry_Price.get() + ", " + self.entry_Akkum.get() + ", '" + self.entry_Data_start.get() + "', '" + self.entry_Data_finish.get() + "', '" + self.combobox_proizv.get() + "', '" + self.combobox_type.get() + "', " + self.combobox_diagonal.get() + ", " + self.combobox_PIX.get() + ", '" + self.combobox_color.get() + "');"
                    else:
                        sql = "insert into " + tabl + " (Name, Zena, Akkum, Data_begin, proizvod_Name, type_Name, Ekran_Diagonal, Ekran_PIX_inch, color_Name) values ('" + self.entry_Name.get() + "', " + self.entry_Price.get() + ", " + self.entry_Akkum.get() + ", '" + self.entry_Data_start.get() + "' , '" + self.combobox_proizv.get() + "' , '" + self.combobox_type.get() + "', " + self.combobox_diagonal.get() + ", " + self.combobox_PIX.get() + ", '" + self.combobox_color.get() + "');"
                if (self.combobox.get() == "Цвета"):
                    tabl = "color"
                    sql = "select Name from color;"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    if any(self.entry_Name.get() in s for s in result):
                        messagebox.showerror('Error:', ' Название повторяется')
                        exit()
                    sql = "insert into " + tabl + " (Name) value ('" + self.entry_Name.get() + "');"
                if (self.combobox.get() == "Типы"):
                    tabl = "type"
                    sql = "select Name from type;"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    if any(self.entry_Name.get() in s for s in result):
                        messagebox.showerror('Error:', ' Название повторяется')
                        exit()
                    sql = "insert into " + tabl + " (Name) value ('" + self.entry_Name.get() + "');"
                if (self.combobox.get() == "Производители"):
                    tabl = "proizvod"
                    sql = "select Name from proizvod;"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    if any(self.entry_Name.get() in s for s in result):
                        messagebox.showerror('Error:', ' Название повторяется')
                        exit()
                    sql = "insert into " + tabl + " (Name) value ('" + self.entry_Name.get() + "');"
                if (self.combobox.get() == "Экраны"):
                    sql = "select Diagonal from telephon;"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    sql1 = "select PIX_inch from telephon;"
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    if (any(self.entry_Name.get() in s for s in result) & any(self.entry_Price.get() in s1 for s1 in result1)):
                        messagebox.showerror('Error:', ' запись по повторяется')
                        exit()
                    sql = "insert into Ekran (Diagonal, PIX_inch) values (" + self.entry_Name.get() + " , " + self.entry_Price.get() + ");"
                cursor.execute(sql)
                conn.commit()
        except Error as e:
            messagebox.showerror('Error', '%s'% e)
            exit()
        finally:
            conn.close()
class Child_delete(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    def init_child(self):
        #Обшие параметры дочернего окна
        self.title("Добавить запись")
        self.geometry('500x450+300+200')
        self.resizable(False, False)
        #виджеты
        #Ввод
        lablel_ID = tk.Label(self, text='ID ')
        lablel_ID.place(x=0, y=25)
        self.entry_Name = ttk.Entry(self)
        self.entry_Name.place(x=0, y=55)
        self.combobox_delete = ttk.Combobox(self, values=[u'Телефоны', u'Цвета', u'Типы', u'Производители', u'Экраны'])
        #
        lablel_description = tk.Label(self, text='Выбор таблицы')
        lablel_description.place(x=0, y=0)
        self.combobox_delete.current(0)
        self.combobox_delete.place(x=100, y=0)
        # кнопка
        self.but_create_tele = Button(self)
        self.but_create_tele["text"] = "Удалить"
        self.but_create_tele.bind("<Button-1>", self.delete)
        self.but_create_tele.pack()
        self.but_create_tele.place(x=200, y=30)

        self.grab_set()
        self.focus_set()
        root.mainloop()
    def delete(self,event):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')

            if conn.is_connected():
                print('Connected to MySQL database')
                cursor = conn.cursor()
                if(self.combobox_delete.get()=="Телефоны"):
                    sql ="DELETE FROM telephon WHERE id_telephon="+self.entry_Name.get() + ";"
                elif( self.combobox_delete.get()=="Цвета"):
                    sql = "DELETE FROM color WHERE id= " + self.entry_Name.get() + ";"
                elif( self.combobox_delete.get()=="Типы" ):
                    sql = "DELETE FROM type WHERE id= " + self.entry_Name.get() + ";"
                elif( self.combobox_delete.get()=="Производители"):
                    sql = "DELETE FROM proizvod WHERE id= " + self.entry_Name.get() + ";"
                elif( self.combobox_delete.get()=="Экраны"):
                    sql = "DELETE FROM Ekran WHERE id= " + self.entry_Name.get() + ";"
                cursor.execute(sql)
                conn.commit()
                conn.close()
                cursor.close()
        except Error as e:
            messagebox.showerror('Error', '%s' % e)
            conn.close()
            cursor.close()
            exit()
class Child_doc(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    def init_child(self):
        #Обшие параметры дочернего окна
        self.title("Вывод в документ")
        self.geometry('500x450+300+200')
        self.resizable(False, False)
        self.combobox = ttk.Combobox(self, values=[u'Телефоны', u'Цвета', u'Типы', u'Производители', u'Экраны'])
        #
        self.lablel_description = tk.Label(self, text='Выбор таблицы').pack(fill=tk.BOTH)
        self.combobox.current(0)
        self.combobox.pack(fill=tk.BOTH)
        self.radio=Radiobutton(root,text="vbn")
        self.but_create_tele = Button(self)
        self.but_create_tele["text"] = "Вывод"
        self.but_create_tele.bind("<Button-1>", self.pech)
        self.but_create_tele.pack()
        self.but_create_tele.place(x=200, y=50)
    def pech(self,event):
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                    ("HTML files", "*.html;*.htm"),
                                                    ("All files", "*.*")))
        f = open(file_name, 'w')
        s = "Таблица %s\n" % self.combobox.get()
        f.write(s)
        s=" "
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')
            if conn.is_connected():
                cursor = conn.cursor()
                if (self.combobox.get() == "Телефоны"):
                    s = "ID_telephon | Name | Price | Akkum | Data_begining | Data_finish | proizvod_Name | type_Name | Ekran_Diagonal | Ekran_PIX_inch | color_Name\n"
                    f.write(s)
                    tabl = "telephon"
                elif (self.combobox.get() == "Цвета"):
                    s = "ID | Name \n"
                    f.write(s)
                    tabl = "color"
                elif (self.combobox.get() == "Типы"):
                    s = "ID | Name \n"
                    f.write(s)
                    tabl = "type"
                elif (self.combobox.get() == "Производители"):
                    s = "ID | Name \n"
                    f.write(s)
                    tabl = "proizvod"
                elif (self.combobox.get() == "Экраны"):
                    s = "ID | Diagonal | PIX \n"
                    f.write(s)
                    tabl="Ekran"

                sql= "select * from " + tabl + ";"
                cursor.execute(sql)
                result = cursor.fetchall()
        except Error as e:
            messagebox.showerror('Error', '%s' % e)
            exit()
        finally:
            conn.close()

        s="  "
        for i in range(len(result)):
            for j in range(len(result[i])):
                s=s+str(result[i][j])+" | "
            s=s+"\n"
        f.write(s)
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='telephon_bas',
                                           user='root',
                                           password='')
            if conn.is_connected():
                cursor = conn.cursor()
                if (self.combobox.get() == "Телефоны"):
                    tabl = "telephon"

                    sql = "select id_telephon from " + tabl + ";"
                elif (self.combobox.get() == "Цвета"):
                    tabl = "color"
                    sql = "select id from " + tabl + ";"
                elif (self.combobox.get() == "Типы"):
                    tabl = "type"
                    sql = "select id from " + tabl + ";"
                elif (self.combobox.get() == "Производители"):
                    tabl = "proizvod"
                    sql = "select id from " + tabl + ";"
                elif (self.combobox.get() == "Экраны"):
                    tabl="Ekran"
                    sql = "select id from " + tabl + ";"
                cursor.execute(sql)
                result = cursor.fetchall()
                s="\n"
                f.write(s)
                s="Количество  "
                f.write(s)
                s=str(len(result))
                f.write(s)
        except Error as e:
            messagebox.showerror('Error', '%s' % e)
            exit()
        finally:
            conn.close()
        f.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("База данных телефонов")
    root.geometry("1200x400+300+200")
    root.resizable(False, False)
    root.mainloop()
