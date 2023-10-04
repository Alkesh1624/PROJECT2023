Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> items_list = ["meat","banana","redbull"]
... 
... def display_menu():
...     print("Menu:")
...     print("1. Add item to the list")
...     print("2. Delete item from the list")
...     print("3. Display current items on the list")
...     print("4. Exit")
... 
... def add_item():
...     item = input("Enter the item name: ")
...     items_list.append(item)
...     print(f"Item '{item}' added to the list.")
... 
... def delete_item():
...     item = input("Enter the item name: ")
...     if item in items_list:
...         items_list.remove(item)
...         print(f"Item '{item}' deleted from the list.")
...     else:
...         print(f"Item '{item}' not found in the list.")
... 
... def display_items():
...     print("Current items on the list:")
...     for item in items_list: 
...         print("- " + item)
... 
... # Main program loop
... while True:
...     display_menu()
...     choice = input("Enter your choice (1-4): ")
... 
...     if choice == "1":
...         add_item()
...     elif choice == "2":
...         delete_item()
...     elif choice == "3":
        display_items()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
