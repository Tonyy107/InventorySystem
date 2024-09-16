# Inventory Management System

![Inventory Management System](https://img.shields.io/badge/Inventory-Management-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Overview

The **Inventory Management System** is a user-friendly desktop application built with Python and Tkinter for managing inventory data. It provides a graphical interface for adding, editing, deleting, and viewing inventory items. The system utilizes an SQLite database (`db`) to store and persist inventory data across sessions, ensuring durability.

## Features

- **Add New Items**: Add inventory items with details like name, quantity, and price.
- **Edit Existing Items**: Modify the details of any existing inventory item.
- **Delete Items**: Easily remove items from the inventory.
- **Search Functionality**: Search for inventory items by name or keyword.
- **View Inventory**: Display all items in a table format with sortable columns.
- **Data Persistence**: Inventory data is saved in the SQLite database (`db`) for future use.
- **Error Handling**: Validates input to prevent incorrect data from being added.

## Requirements

- **Python 3.x**
- **Tkinter** (GUI library that comes pre-installed with Python)
- **SQLite3** (for database operations)

To ensure you have Tkinter installed, you can run:
```bash
sudo apt-get install python3-tk  # For Linux systems
```
## Installation
### 1.Clone this repository:
```bash
git clone https://github.com/Tonyy107/InventorySystem
cd InventorySystem
```
### 2.Install the required libraries:
```bash
sudo apt-get install python3-tk
```
### 3.Run the application:
```bash
python inventory_system_gui.py
```

## Project Structure
```bash
inventory-management-system/
│
├── database/               # Folder containing the SQLite database
│   ├── inventory.db        # The actual SQLite database file
│   └── setup.py            # the file that create SQLite database
│
├── inventory_system_gui.py # Handles the Tkinter GUI setup and functionality (and work as main file)
├── InventorySystem.py      # Handles core inventory logic (add, edit, delete)
└── README.md               # Project documentation
```
## Usage
- **Launch the Application:** Start the system by running main.py.
- **Add New Items:** Fill out the details in the form and click the "Add Item" button.
- **Edit Items:** Select an item from the list, make changes in the form, and click "Update Item".
- **Delete Items:** Select an item from the list and click "Delete Item".
- **Search:** Use the search bar to filter items based on keywords.
- **Save and Load Data:** The inventory is automatically saved to the db file and loaded upon reopening the application.

## Screenshots
Main Interface

Add New Item

Edit Item

## Technologies Used
- **Python:** Core logic implementation.
- **Tkinter:** For creating the graphical user interface.
- **SQLite:** Database engine for storing inventory data in the db file.
## Future Enhancements
- **User Authentication:** Implement user login for accessing the system.
- **Advanced Search & Filtering:** Add advanced filtering options based on item categories, price ranges, etc.
- **Export Data:** Allow users to export the inventory data to various formats like PDF or Excel.
- **Multi-User Support:** Enable multiple users to manage the inventory with role-based permissions.
- **Data Analytics:** Add features like sales forecasting, inventory trends, and restock alerts based on historical data.
## Contributing
### Contributions are welcome! Please follow these steps:

**1. Fork the repository.**

**2. Create a new branch:**
```bash
git checkout -b feature-name.
```

**3. Make your changes and commit:** 
```bash
git commit -m 'Add some feature'.
```

**4. Push to the branch:** 
```bash
git push origin feature-name.
```

**5. Submit a pull request.**

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


## Author
**Anton Magdy** - Developer of the Inventory Management System
[GitHub Profile](https://github.com/Tonyy107)