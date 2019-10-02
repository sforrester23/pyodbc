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
# Allows us to execute readonly queries on the database

# Creating a cursor
cursor_nwdb = connect_nwdb.cursor()

cursor_nwdb.execute("SELECT CustomerID FROM customers;")

# print(cursor_nwdb)

# Fetch rows from cursor - .fetchone()
# row = cursor_nwdb.fetchone()
# print(row)

# Fetch all rows from cursos - .fetchall()
# This is bad MM'kay?
rows = cursor_nwdb.execute("SELECT * FROM Customers").fetchall()
# print(rows)
print(type(rows)) # This is a list type
print(type(rows[0])) # each instance of this list is a class object
print(type(rows[0].CustomerID)) # we can access said class objects with . - this is a string

rows = cursor_nwdb.execute("SELECT * FROM Products").fetchall()

for record in rows:
    print(type(record))
    print(record.UnitPrice) # We can access the column of a specific record

# However, this is dangerous as we said.
# BEcause we can clog our machine with too much data

rows = cursor_nwdb.execute("SELECT * FROM Products") # no fetching

cursor_nwdb.execute("SELECT * FROM Customers")

row = cursor_nwdb.fetchone() # cursor means it maintains the state
print(row.ContactName)
row = cursor_nwdb.fetchone() # each call to fetch will fetch the next one, because it knows it fetched the previous one
print(row.ContactName)
row = cursor_nwdb.fetchone() # this makes python become a little bit more persistant, in a way
print(row.ContactName)

# This is more effiecient than a for loop
while True:
    record = rows.fetchone() # fetches each one in turn, as it maintains state it knows not to repeat the first one each time, it only takes the next one
    # when the fetching gets to the end, the record will be None, so break the while loop
    if record is None:
        break
    # print the contact name each time for the fetched record
    print(record.ContactName)


# Fetch some data using for loops