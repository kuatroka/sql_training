import sqlite3

# create a function that queries database customers.db and prints every rows in a new line
def show_all():
    conn = sqlite3.connect("/code/data/customers.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    all_rows = c.fetchall()
    for row in all_rows:
        print(row)

    conn.commit()
    conn.close()


# create function that adds a new row to the database
def add_one(name, email, phone):
    conn = sqlite3.connect("/code/data/customers.db")
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (name, email, phone))

    conn.commit()
    conn.close()


# create function that deletes a row from the database
def delete_one(id):
    conn = sqlite3.connect("/code/data/customers.db")
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = ?", (id,))

    conn.commit()
    conn.close()


# create function that adds many rows to the database
def add_many(list):
    conn = sqlite3.connect("/code/data/customers.db")
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", list)

    conn.commit()
    conn.close()


# create function with where clause
def email_lookup(email):
    conn = sqlite3.connect("/code/data/customers.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE email LIKE ?", (email,))
    all_rows = c.fetchall()
    for row in all_rows:
        print(row)

    conn.close()
