import sqlite3

def create_database():

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        name TEXT,
        expiry_date TEXT,
        reminder_days INTEGER
    )
    """)

    conn.commit()
    conn.close()


def add_product(category, name, expiry_date, reminder_days):

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO products
        (category, name, expiry_date, reminder_days)
        VALUES (?, ?, ?, ?)
        """,
        (category, name, expiry_date, reminder_days)
    )

    conn.commit()
    conn.close()


def get_products():

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, name, expiry_date, reminder_days
    FROM products
    """)

    rows = cursor.fetchall()
    
    for row in rows:
        print(repr(row[1]))

    conn.close()

    return rows


create_database()

def delete_product(name):
    print("Trying to delete:",name)

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE name=?",
        (name.strip(),)
    )
    
    print("Rows deleted:",cursor.rowcount)

    conn.commit()
    conn.close()
    
def update_product(name, expiry_date, reminder_days):

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE products
        SET expiry_date = ?, reminder_days = ?
        WHERE name = ?
        """,
        (expiry_date, reminder_days, name)
    )

    conn.commit()
    conn.close()