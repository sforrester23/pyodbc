import pyodbc

# In this file, we will make our connection

# Parameters/Variables for connection
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
connect_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(connect_nwdb)

# Create a Cursor

# Fetch some data