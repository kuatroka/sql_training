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


show_all()
