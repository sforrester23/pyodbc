import pyodbc

# We should consider the concept of "Strong Params": never EVER trust user inputs
# Avoid SQL injections
# Filter for SQL injections

class ConnectMsSQL():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connect_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.connect_db.cursor()

    def __filter_query(self, sqlquery):
        return self.cursor.execute(sqlquery)
        # Doing some filtering for bad queries

    def __sql_query(self, sqlquery): # we encapsulate this and then only call it in other methods
        return self.__filter_query(sqlquery)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    def sql_query_fetchall(self, query):
        return self.__filter_query().fetchall()

    def print_all_records(self, table):
        query_rows = self.__filter_query('SELECT * FROM {}'.format(table))
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        query_rows = self.__filter_query('SELECT AVG(UnitPrice) FROM Products')
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def return_average_unit_price_products(self):
        # Query
        query = self.__filter_query('SELECT * FROM Products')
        # Get all the unit prices
        prices = []
        while True:
            # get individual prices
            # append to prices list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        # sum and divide by length of rows
        return (sum(prices)/len(prices))


    # def total_sales_for_company(self):
    #     query_rows = self.__filter_query("SELECT CompanyName, SUM(ROUND(UnitPrice*Quantity*(1-Discount),2)) FROM [Order Details] OD "
    #                                      "JOIN Orders O ON OD.OrderID=O.OrderID"
    #                                      "JOIN Customers C ON C.CustomerID=O.CustomerID"
    #                                      "GROUP BY CompanyName")


# CRUD

# Create 1 entry
    # use INSERT
    # the cursor cannot make transactions (go to documentation)

# Read all entries
    # fetch all records and return as either list or dictionaries

# Read one entry
    # fetch specific record
    # Intake a certain condition to search with
    # get one value using ID

# Update 1 entry
    # find out the position (ID) of the data we'd like to update
    # use UPDATE TABLE where that specific record exits
    # Cursor does not make transactions (Documentation)

# Destroy 1 entry
    # destroy what?
    # the ID of the specific record
    
    # destroy the record