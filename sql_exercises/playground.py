# import sqlite3

# conn = sqlite3.connect(
#     ":memory:"
# )  # would create an in memory db. !! it will disappear when disconnected

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# # create a table
# c.execute(
#     """
#           CREATE TABLE customers (
#               first_name TEXT,
#               last_name TEXT,
#               email TEXT
#                         )
#     """
# )

# # data types:

# # NULL
# # INTERGER
# # REAL
# # TEXT
# # BLOB

# # commit out command
# conn.commit()

# # close connection
# conn.close()


##########################################
# Populate the table
# import sqlite3

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# # insert one row

# # c.execute(" INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
# # c.execute(" INSERT INTO customers VALUES ('Tim', 'Ferris', 'tim@codemy.com')")
# # c.execute(" INSERT INTO customers VALUES ('Mary', 'Pippin', 'mpippin@codemy.com')")


# # insert many rows at ones
# many_customers = [
#     ("Wes", "Brown", "wes@brown.com"),
#     ("mi", "mo", "mimo@example.com"),
#     ("qui", "bono", "qbono@mi.com"),
# ]

# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# # commit out command
# conn.commit()

# # close connection
# conn.close()

#################################################################

# Query the database
# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# # Query the table
# c.execute("SELECT rowid, * FROM customers")  # shows the default SQLite's index
# c.execute("SELECT * FROM customers")
# # print(c.fetchone())  # fetches the last or first (not sure) row in the table
# # print(c.fetchone()[2])  # fetches the last or first (not sure) row in the table
# # print(c.fetchmany(3))
# # print(c.fetchall())

# for i in c.fetchall():
#     print(i)


# # commit out command
# conn.commit()

# # close connection
# conn.close()

# #################################################################

# # WHERE clause
# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# # Query the table

# # c.execute("SELECT * FROM customers WHERE last_name = 'Elder' ")

# # c.execute(    "SELECT * FROM customers WHERE last_name LIKE 'Br%' ")  # search with the wildcard
# c.execute(
#     "SELECT * FROM customers WHERE email LIKE '%codem%' "
# )  # search with the wildcard

# for i in c.fetchall():
#     print(i)


# # commit out command
# conn.commit()

# # close connection
# conn.close()

#################################################################

# UPDATE RECORDS
# import sqlite3

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# c.execute(
#     """UPDATE customers SET first_name = 'John'
#        WHERE rowid = 1
#           """
# )  #

# conn.commit()

# c.execute("SELECT rowid, * FROM customers")
# # before using fetchall or any fetch, you MUST first use c.execute with some sort of SELECT
# # if not, the fetch will not bring anything
# for i in c.fetchall():
#     print(i)


# conn.commit()
# conn.close()

#################################################################
# ORDER BY RECORDS
# import sqlite3

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()
# # query table customers and order by last name
# # c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# items = c.fetchall()

# for i in items:
#     print(i)


# conn.commit()
# conn.close()

# #################################################################
# # AND OR
# import sqlite3

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# # c.execute("SELECT * FROM customers WHERE last_name LIKE 'Pi%' AND first_name LIKE '%a%'"
# # )
# c.execute(
#     "SELECT * FROM customers WHERE last_name LIKE 'Pi%' OR first_name LIKE '%e%' OR email LIKE '%de%'"
# )


# items = c.fetchall()

# for i in items:
#     print(i)


# conn.commit()
# conn.close()

#################################################################
# LIMITING RESULTS
# import sqlite3

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# c.execute("SELECT * FROM customers LIMIT 2")


# items = c.fetchall()

# for i in items:
#     print(i)


# conn.commit()
# conn.close()

# #################################################################
# # DROPPIN TABLE
# import sqlite3

# conn = sqlite3.connect("/code/data/customers.db")
# c = conn.cursor()

# c.execute("DROP TABLE customers")
# conn.commit()

# c.execute("SELECT * FROM customers")
# items = c.fetchall()

# for i in items:
#     print(i)


# conn.close()


#################################################################
### DROPPING TABLE
import sqlite3

conn = sqlite3.connect("/code/data/customers.db")
c = conn.cursor()


c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()

for i in items:
    print(i)

conn.commit()
conn.close()
