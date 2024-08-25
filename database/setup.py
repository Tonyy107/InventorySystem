# database/setup.py
import sqlite3
import os
DATABASE_PATH = f'{os.getcwd()}/database/inventory.db'


def create_database():
    """
    Creates a SQLite database and a 'products' table if it doesn't exist.

    The 'products' table has the following columns:
    - id: INTEGER (Primary Key, Auto Increment)
    - name: TEXT (Not Null)
    - description: TEXT
    - quantity: INTEGER (Not Null)
    - price: REAL (Not Null)
    - location: TEXT

    Returns:
    None
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL,
                        location TEXT)''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created and connected successfully.")
