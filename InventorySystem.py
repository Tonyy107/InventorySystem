# inventory_system.py
from database.setup import create_database, DATABASE_PATH
import os
import sys
import sqlite3
import cmd


sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))


create_database()


def add_product(name, description, quantity, price, location):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO products (name, description, quantity, price, location) VALUES (?, ?, ?, ?, ?)",
              (name, description, quantity, price, location))
    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("UPDATE products SET quantity = ? WHERE id = ?",
              (new_quantity, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()


def generate_report():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    conn.close()
    return rows


def check_low_stock(threshold):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE quantity < ?", (threshold,))
    rows = c.fetchall()
    conn.close()
    return rows


def search_product(search_term):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE name LIKE ?",
              ('%' + search_term + '%',))
    rows = c.fetchall()
    conn.close()
    return rows


class InventorySystem(cmd.Cmd):
    intro = 'Welcome to the Inventory Management System. Type help or ? to list commands.\n'
    prompt = '(inventory) '

    def do_add(self, arg):
        'Add a new product: add name description quantity price location'
        try:
            args = arg.split()
            name = args[0]
            description = args[1]
            quantity = int(args[2])
            price = float(args[3])
            location = args[4]
            add_product(name, description, quantity, price, location)
            print(f"Product '{name}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def do_update(self, arg):
        'Update product quantity: update product_id new_quantity'
        try:
            args = arg.split()
            product_id = int(args[0])
            new_quantity = int(args[1])
            update_quantity(product_id, new_quantity)
            print(
                f"Quantity for product ID '{product_id}' updated to '{new_quantity}'.")
        except Exception as e:
            print(f"Error: {e}")

    def do_report(self, arg):
        'Generate inventory report: report'
        rows = generate_report()
        for row in rows:
            print(row)

    def do_check(self, arg):
        'Check low stock items: check threshold'
        try:
            threshold = int(arg)
            rows = check_low_stock(threshold)
            for row in rows:
                print(f"Low stock alert: {row}")
        except Exception as e:
            print(f"Error: {e}")

    def do_exit(self, arg):
        'Exit the inventory system: exit'
        print('Exiting the Inventory Management System.')
        return True


if __name__ == '__main__':
    InventorySystem().cmdloop()
