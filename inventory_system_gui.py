import tkinter as tk
from tkinter import ttk, messagebox
from database.setup import create_database
from InventorySystem import add_product, update_quantity, generate_report, check_low_stock, delete_product, search_product

create_database()


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x600")
        self.root.state('normal')
        self.root.configure(bg='#333333')

        style = ttk.Style()
        style.theme_use('clam')

        style.configure("TNotebook.Tab", background="#333333",
                        foreground="white", font=('Arial', 12, 'bold'))
        style.configure("TNotebook", background="#333333", borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", "#444444")])

        style.configure("TFrame", background="#333333")
        style.configure("TLabel", background="#333333",
                        foreground="white", font=('Arial', 10))
        style.configure("TEntry", font=('Arial', 10))
        style.configure("TButton", background="#444444",
                        foreground="white", font=('Arial', 10, 'bold'))

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        self.frame_add = ttk.Frame(self.notebook)
        self.frame_update = ttk.Frame(self.notebook)
        self.frame_report = ttk.Frame(self.notebook)
        self.frame_low_stock = ttk.Frame(self.notebook)
        self.frame_search = ttk.Frame(self.notebook)

        self.frame_add.pack(fill='both', expand=True)
        self.frame_update.pack(fill='both', expand=True)
        self.frame_report.pack(fill='both', expand=True)
        self.frame_low_stock.pack(fill='both', expand=True)
        self.frame_search.pack(fill='both', expand=True)

        self.notebook.add(self.frame_add, text='Add Product')
        self.notebook.add(self.frame_update, text='Update/Delete Product')
        self.notebook.add(self.frame_report, text='Generate Report')
        self.notebook.add(self.frame_low_stock, text='Check Low Stock')
        self.notebook.add(self.frame_search, text='Search Product')

        self.create_add_product_tab()
        self.create_update_delete_product_tab()
        self.create_report_tab()
        self.create_low_stock_tab()
        self.create_search_product_tab()

    def create_add_product_tab(self):
        ttk.Label(self.frame_add, text="Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky='W')
        self.name_entry = ttk.Entry(self.frame_add)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.frame_add, text="Description:").grid(
            row=1, column=0, padx=10, pady=5, sticky='W')
        self.description_entry = ttk.Entry(self.frame_add)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.frame_add, text="Quantity:").grid(
            row=2, column=0, padx=10, pady=5, sticky='W')
        self.quantity_entry = ttk.Entry(self.frame_add)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.frame_add, text="Price:").grid(
            row=3, column=0, padx=10, pady=5, sticky='W')
        self.price_entry = ttk.Entry(self.frame_add)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.frame_add, text="Location:").grid(
            row=4, column=0, padx=10, pady=5, sticky='W')
        self.location_entry = ttk.Entry(self.frame_add)
        self.location_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_button = ttk.Button(
            self.frame_add, text="Add Product", command=self.add_product)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_update_delete_product_tab(self):
        ttk.Label(self.frame_update, text="Product ID:").grid(
            row=0, column=0, padx=10, pady=5, sticky='W')
        self.product_id_entry = ttk.Entry(self.frame_update)
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.frame_update, text="New Quantity:").grid(
            row=1, column=0, padx=10, pady=5, sticky='W')
        self.new_quantity_entry = ttk.Entry(self.frame_update)
        self.new_quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        self.update_button = ttk.Button(
            self.frame_update, text="Update Quantity", command=self.update_quantity)
        self.update_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.delete_button = ttk.Button(
            self.frame_update, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_report_tab(self):
        self.report_button = ttk.Button(
            self.frame_report, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=0, column=0, pady=10)

        self.report_tree = ttk.Treeview(self.frame_report, columns=(
            "ID", "Name", "Description", "Quantity", "Price", "Location"), show="headings")
        self.report_tree.heading("ID", text="ID")
        self.report_tree.heading("Name", text="Name")
        self.report_tree.heading("Description", text="Description")
        self.report_tree.heading("Quantity", text="Quantity")
        self.report_tree.heading("Price", text="Price")
        self.report_tree.heading("Location", text="Location")

        self.report_tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.frame_report.grid_rowconfigure(1, weight=1)
        self.frame_report.grid_columnconfigure(0, weight=1)

    def create_low_stock_tab(self):
        ttk.Label(self.frame_low_stock, text="Low Stock Threshold:").grid(
            row=0, column=0, padx=10, pady=5, sticky='W')
        self.low_stock_entry = ttk.Entry(self.frame_low_stock)
        self.low_stock_entry.grid(row=0, column=1, padx=10, pady=5)

        self.check_low_stock_button = ttk.Button(
            self.frame_low_stock, text="Check Low Stock", command=self.check_low_stock)
        self.check_low_stock_button.grid(
            row=1, column=0, columnspan=2, pady=10)

        self.low_stock_tree = ttk.Treeview(self.frame_low_stock, columns=(
            "ID", "Name", "Description", "Quantity", "Price", "Location"), show="headings")
        self.low_stock_tree.heading("ID", text="ID")
        self.low_stock_tree.heading("Name", text="Name")
        self.low_stock_tree.heading("Description", text="Description")
        self.low_stock_tree.heading("Quantity", text="Quantity")
        self.low_stock_tree.heading("Price", text="Price")
        self.low_stock_tree.heading("Location", text="Location")

        self.low_stock_tree.grid(
            row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.frame_low_stock.grid_rowconfigure(2, weight=1)
        self.frame_low_stock.grid_columnconfigure(0, weight=1)

    def create_search_product_tab(self):
        ttk.Label(self.frame_search, text="Search:").grid(
            row=0, column=0, padx=10, pady=5, sticky='W')
        self.search_entry = ttk.Entry(self.frame_search)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = ttk.Button(
            self.frame_search, text="Search Product", command=self.search_product)
        self.search_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.search_tree = ttk.Treeview(self.frame_search, columns=(
            "ID", "Name", "Description", "Quantity", "Price", "Location"), show="headings")
        self.search_tree.heading("ID", text="ID")
        self.search_tree.heading("Name", text="Name")
        self.search_tree.heading("Description", text="Description")
        self.search_tree.heading("Quantity", text="Quantity")
        self.search_tree.heading("Price", text="Price")
        self.search_tree.heading("Location", text="Location")

        self.search_tree.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.frame_search.grid_rowconfigure(2, weight=1)
        self.frame_search.grid_columnconfigure(0, weight=1)

    def add_product(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        location = self.location_entry.get()
        if name and description and quantity and price and location:
            add_product(name, description, int(
                quantity), float(price), location)
            messagebox.showinfo(
                "Success", f"Product '{name}' added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def update_quantity(self):
        product_id = self.product_id_entry.get()
        new_quantity = self.new_quantity_entry.get()
        if product_id and new_quantity:
            update_quantity(int(product_id), int(new_quantity))
            messagebox.showinfo(
                "Success", f"Product ID '{product_id}' updated to quantity '{new_quantity}'.")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def delete_product(self):
        product_id = self.product_id_entry.get()
        if product_id:
            delete_product(int(product_id))
            messagebox.showinfo(
                "Success", f"Product ID '{product_id}' deleted successfully.")
        else:
            messagebox.showwarning(
                "Input Error", "Please fill in the Product ID")

    def generate_report(self):
        rows = generate_report()
        for row in self.report_tree.get_children():
            self.report_tree.delete(row)
        for row in rows:
            self.report_tree.insert("", "end", values=row)

    def check_low_stock(self):
        threshold = self.low_stock_entry.get()
        if threshold:
            rows = check_low_stock(int(threshold))
            for row in self.low_stock_tree.get_children():
                self.low_stock_tree.delete(row)
            for row in rows:
                self.low_stock_tree.insert("", "end", values=row)
        else:
            messagebox.showwarning(
                "Input Error", "Please enter a threshold value")

    def search_product(self):
        search_term = self.search_entry.get()
        if search_term:
            rows = search_product(search_term)
            for row in self.search_tree.get_children():
                self.search_tree.delete(row)
            for row in rows:
                self.search_tree.insert("", "end", values=row)
        else:
            messagebox.showwarning("Input Error", "Please enter a search term")


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
