# Inventory Management System

A console-based Inventory Management System built with **Python** and **MySQL**.

This project is designed to manage products, stock, categories, brands, suppliers, customers, purchases, and sales through a simple command-line interface.

## 📌 Project Status

🚧 **Currently in Development**

This project is being developed as a learning project while improving my Python, MySQL, Git, and GitHub skills.

---
## How to Run
install mysql-connector-python
install dotenv
run file main.py
create datatabse using database.py
## ✨ Features

### Product Management
- Add new products
- Prevent duplicate products
- Store purchase price
- Store current stock
- View all products

### Product Categories
- Create product categories
- Store category information
- Connect products with categories

### Product Brands
- Create product brands
- Connect products with brands

### Supplier Management
- Store supplier information
- Store supplier name
- Store supplier email
- Store supplier phone number

### Customer Management
- Store customer information
- Store customer name
- Store customer email
- Store customer phone number

### Purchase Management
- Record purchases
- Connect purchases with suppliers
- Store purchase date
- Store purchase total
- Store purchased products and quantities

### Sales Management
- Record sales
- Connect sales with customers
- Store sale date
- Store sale total
- Store sold products and quantities

### Database
- MySQL database
- Relational database structure
- Primary keys
- Foreign keys
- Auto-increment IDs
- Database creation through Python

### Security
- Database credentials are stored using environment variables
- `.env` is excluded from Git using `.gitignore`

---

## 🛠️ Technologies Used

- Python
- MySQL
- MySQL Connector/Python
- python-dotenv
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```text
Inventory-Management-System/
│
├── database.py
├── Inventory_Management.py
├── .env
├── .gitignore
├── README.md
└── .venv/