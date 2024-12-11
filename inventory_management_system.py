"""
Project Description
Build a command-line app that allows a small business to manage their inventory. The app will let users:
•	add new item
•	update stock
•	view all items
•	search for specific items by name

This project is perfect for practicing CRUD (Create, Read, Update, Delete) operations using dictionaries.
Learning Benefits
You will practice CRUD operations, dictionary manipulation, and handling user input while building a tool that models real-world applications.

"""
import json

# Ensure the database file exists with initial data
try:
    with open("database.json", "x") as file:
        json.dump({}, file, indent=4)  # Initialize with an empty dictionary
except FileExistsError:
    pass  # The file already exists, no need to reinitialize

message = (
    "Welcome to the Inventory Management system!\n"
    "1. Add new items,\n"
    "2. Update stock,\n"
    "3. View inventory,\n"
    "4. Search for an item,\n"
    "5. Exit"
)
print(message)

user_choice = input("Choose an action from 1 to 5: ")

if user_choice == "1":
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    with open("database.json", "r+") as file:
        data = json.load(file)
        data[item_name] = (item_quantity, price)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    print(f"Added {item_name} to the inventory.")

elif user_choice == "2":
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter updated quantity: "))
    price = float(input("Enter updated price: "))
    with open("database.json", "r+") as file:
        data = json.load(file)
        if item_name in data:
            data[item_name] = (item_quantity, price)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            print(f"Updated {item_name} in the inventory.")
        else:
            print(f"{item_name} not found in inventory.")

elif user_choice == "3":
    try:
        with open("database.json", "r") as file:
            data = json.load(file)
            if data:
                for item_name, (quantity, price) in data.items():
                    print(f"Item: {item_name}, Quantity: {quantity}, Price: {price}")
            else:
                print("The inventory is empty.")
    except FileNotFoundError:
        print("The database file is missing. Please add items to initialize the inventory.")
    except json.JSONDecodeError:
        print("The database file is corrupted. Please reset the inventory.")

elif user_choice == "4":
    item_name = input("Enter item name to search: ")
    with open("database.json", "r") as file:
        data = json.load(file)
        if item_name in data:
            quantity, price = data[item_name]
            print(f"Item: {item_name}, Quantity: {quantity}, Price: {price}")
        else:
            print(f"{item_name} not found.")

elif user_choice == "5":
    print("Exiting the system. Goodbye!")
    exit()

else:
    print("Invalid choice. Please select an option between 1 and 5.")

