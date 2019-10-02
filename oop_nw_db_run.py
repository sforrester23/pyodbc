from oop_db_connect import *

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_nw = ConnectMsSQL(server, database, username, password)
print(db_nw)
print(db_nw.connect_db)

print(db_nw.cursor.execute('SELECT * FROM Products').fetchone())