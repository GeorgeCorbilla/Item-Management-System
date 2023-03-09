class Item:
    id_counter = 0

    def __init__(self, name, description, price, quantity):

        Item.id_counter += 1
        self.id = Item.id_counter
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ItemManagement:
    def __init__(self):
        self.items = []

    def add_item(self):
        print("\nAdd New Item")
        print("-----------------------------")
        name = input("Name: ")
        description = input("Description: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        item = Item(name, description, price, quantity)
        self.items.append(item)
        print("-----------------------------")
        print("Item added successfully.")

    def view_item(self):
        print("\nView Item")
        print("-----------------------------")
        item_id = int(input("Enter item id: "))
        item = self.find_item(item_id)
        if item:
            print("Id:", item.id)
            print("Name:", item.name)
            print("Description:", item.description)
            print("Price:", item.price)
            print("Quantity:", item.quantity)
        else:
            print("-----------------------------")
            print("Item not found.")

    def update_item(self):
        print("\nUpdate Item")
        print("-----------------------------")
        item_id = int(input("Enter item id: "))
        item = self.find_item(item_id)
        if item:
            name = input(f"Name ({item.name}): ")
            description = input(f"Description ({item.description}): ")
            price = input(f"Price ({item.price}): ")
            price = float(price) if price else item.price
            quantity = input(f"Quantity ({item.quantity}): ")
            quantity = int(quantity) if quantity else item.quantity
            item.name = name
            item.description = description
            item.price = price
            item.quantity = quantity
            print("-----------------------------")
            print("Item updated successfully.")
        else:
            print("-----------------------------")
            print("Item not found.")

    def delete_item(self):
        print("\nDelete Item")
        print("-----------------------------")
        item_id = int(input("Enter item id: "))
        item = self.find_item(item_id)
        if item:
            self.items.remove(item)
            print("-----------------------------")
            print("Item deleted successfully.")
        else:
            print("-----------------------------")
            print("Item not found.")

    def show_all_items(self):
        print("\nAll Items")
        print("-----------------------------")
        for item in self.items:
            print(f"Id: {item.id}, Name: {item.name}, Description: {item.description}, Quantity: {item.quantity}")

    def find_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def main_menu(self):
        while True:
            print("\n=============================")
            print("\t\tItem Management")
            print("=============================")
            print("[A] - Add New Item")
            print("[V] - View Item")
            print("[U] - Update Item")
            print("[D] - Delete Item")
            print("[S] - Show all items")
            print("[X] - Exit")
            print("=============================")
            choice = input("Enter choice: ")
            if choice.upper() == "A":
                self.add_item()
            elif choice.upper() == "V":
                self.view_item()
            elif choice.upper() == "U":
                self.update_item()
            elif choice.upper() == "D":
                self.delete_item()
            elif choice.upper() == "S":
                self.show_all_items()
            elif choice.upper() == "X":
                print("System Exited")
                break
            else:
                print("Invalid choice, try again.")

item_management = ItemManagement()
item_management.main_menu()
