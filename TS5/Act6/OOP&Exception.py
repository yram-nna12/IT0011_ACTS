class Item:
    def __init__(self, item_id, name, category, description, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __str__(self):
        return f"| {self.item_id:<6} | {self.name:<20} | {self.category:<15} | {self.description:<30} | ₱{self.price:>8.2f} |"


class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, category, description, price):
        try:
            item_id = int(item_id)  # Ensuring item_id is an integer
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            if price < 0:
                raise ValueError("Price cannot be negative.")
            self.items[item_id] = Item(item_id, name, category, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            print("\nInventory List:")
            print("-" * 100)
            print("| ID    | ITEM NAME            | CATEGORY       | DESCRIPTION                   | PRICE     |")
            print("-" * 100)
            for item in self.items.values():
                print(item)
            print("-" * 100)

    def update_item(self, item_id, name=None, category=None, description=None, price=None):
        try:
            item_id = int(item_id)  # Ensuring item_id is an integer
            if item_id not in self.items:
                raise KeyError("Item ID not found.")
            if price is not None and price < 0:
                raise ValueError("Price cannot be negative.")

            item = self.items[item_id]
            if name:
                item.name = name
            if category:
                item.category = category
            if description:
                item.description = description
            if price is not None:
                item.price = price
            print("Item updated successfully!")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        try:
            item_id = int(item_id)  # Ensuring item_id is an integer
            if item_id not in self.items:
                raise KeyError("Item ID not found.")
            del self.items[item_id]
            print("Item deleted successfully!")
        except KeyError as e:
            print(f"Error: {e}")


def run_application():
    manager = ItemManager()
    while True:
        print("\nITEM MANAGEMENT SYSTEM")
        print("[C] Add Item")
        print("[R] View Items")
        print("[U] Update Item")
        print("[D] Delete Item")
        print("[E] Exit")
        choice = input("Enter choice: ").strip().upper()

        if choice == "C":
            try:
                item_id = input("Enter Item ID: ")
                name = input("Enter Item Name: ").strip().title()
                category = input("Enter Item Category: ").strip().title()
                description = input("Enter Item Description: ").strip()
                price = float(input("Enter Item Price: "))
                manager.add_item(item_id, name, category, description, price)
            except ValueError:
                print("Invalid input for price.")

        elif choice == "R":
            manager.view_items()

        elif choice == "U":
            item_id = input("Enter Item ID to update: ")
            name = input("Enter new name (leave blank to keep current): ").strip().title() or None
            category = input("Enter new category (leave blank to keep current): ").strip().title() or None
            description = input("Enter new description (leave blank to keep current): ").strip() or None
            try:
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, category, description, price)
            except ValueError:
                print("Invalid input for price.")

        elif choice == "D":
            item_id = input("Enter Item ID to delete: ")
            manager.delete_item(item_id)

        elif choice == "E":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


run_application()