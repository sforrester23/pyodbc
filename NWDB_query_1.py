# Question 1

import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
connect_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor_nwdb = connect_nwdb.cursor()

count_row = cursor_nwdb.execute("SELECT COUNT(*) FROM ORDERS")

print(count_row.fetchone()[0])

