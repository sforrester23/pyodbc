# Exercise 3

import pyodbc

server='localhost,1433'
database='Northwind'
username='SA'
password='Passw0rd2018'

connect_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor_nwdb = connect_nwdb.cursor()

cursor_nwdb = connect_nwdb.cursor()

count_row = cursor_nwdb.execute("SELECT * FROM ORDERS WHERE ShipCity = 'Rio De Janeiro' OR ShipCity = 'Reims'")

print(count_row.fetchall())
