# 🛒 Grocery Management System

A simple Python-based Grocery Management System where you can keep track of your groceries, track food expiry, organize shopping lists, generate smart recipes amongst others.

---

## 🚀 Features

- Add, Update, Delete grocery items
- Track item expiry and get notified about expired or expiring items
- Generate shopping list based on items out of stock in inventory
- Generate smart recips based on your available itemsin inventory, filtered dynamically to check for items users are allergic to
- Save recipes to favorites or export thm to text files so you can use it whenever
- Customize recipes
- Get information about specific items (shelflife, best storage, classes etc.)

---

## 📂 Project Structure

GROCERY-MANAGER/
|-- main.py # Entry point
|-- recipes.py # Recipe generation logic
|-- inventory.py # Core logic for managing groceries
|-- data/ # Folder for data storage (JSON)
| |** foodData.json
| |** recipeData.json
| |** invenoryData.json
|** README.md
