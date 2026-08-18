# import SQLite
import sqlite3
# bring in dataframe
from csv_cleaner import books
from csv_cleaner import customers
# connect to the database (create books.db)
connection = sqlite3.connect('books.db')
# connect to the database (create customers.db)
connection = sqlite3.connect('customers.db')
# add dataframes to a SQL table
books.to_sql('books', connection, if_exists='replace', index=False)
customers.to_sql('customers', connection, if_exists='replace', index=False)
# check that it worked
cursor = connection.cursor()
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()
for row in rows:
    print(row)

