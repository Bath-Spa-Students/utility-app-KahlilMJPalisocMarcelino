class VendingMachine:
    def __init__(self):
        self.items = {
            '01': {'name': 'Mai Dubai Water', 'price': 1.00, 'stock': 15},
            '02': {'name': '7up', 'price': 2.00, 'stock': 15},
            '03': {'name': 'Pepsi', 'price': 2.50, 'stock': 8},
            '04': {'name': 'Mountain Dew', 'price': 1.50, 'stock': 12},
            '05': {'name': 'Lacnor Chocolate Milk', 'price': 3.00, 'stock': 20},
            '06': {'name': 'Break Chocolate', 'price': 2.00, 'stock': 10},
            '07': {'name': 'Maltesers', 'price': 4.00, 'stock': 15},
            '08': {'name': 'Snickers', 'price': 5.00, 'stock': 10},
            '09': {'name': 'Stix Salted', 'price': 1.50, 'stock': 8},
            '10': {'name': '7days Croissant', 'price': 1.50, 'stock': 20},
            '11': {'name': 'Loacker Chocolate', 'price': 1.25, 'stock': 15},
            '12': {'name': 'Lays Salted', 'price': 1.50, 'stock': 10},
            '13': {'name': 'Pringles Barbeque', 'price': 2.00, 'stock': 12},
            '14': {'name': 'Vimto', 'price': 1.25, 'stock': 15},
            '15': {'name': 'Evian Water', 'price': 5.25, 'stock': 10},
            '16': {'name': 'Kitkat Matcha', 'price': 3.50, 'stock': 12},
            '17': {'name': 'Oreo', 'price': 1.50, 'stock': 10},
            '18': {'name': 'Tiffany Bugles Cheese', 'price': 1.25, 'stock': 15},
            '19': {'name': 'Mr. Krisp', 'price': 2.50, 'stock': 10},
            '20': {'name': 'Emirates Pofaki', 'price': 1.75, 'stock': 12}
        }

    def display_items(self):
        print("-------Welcome to a typical UAE Vending Machine:-------")
        print("-------Select An Item/s:-------")
        for key, item in self.items.items():
            print(f"{key}. {item['name']} - AED{item['price']} - Stock: {item['stock']}")

    def purchase_item(self, selection, quantity):
        if selection in self.items:
            selected_item = self.items[selection]
            if selected_item['stock'] >= quantity:
                amount_due = selected_item['price'] * quantity

                # Prompt user to insert money
                while amount_due > 0:
                    try:
                        payment = float(input(f"Kind Reminder: Do not fold your bills & insert in any direction. You may now insert AED{amount_due:.2f} : "))
                        if payment >= amount_due:
                            change = payment - amount_due
                            print(f"Thank you for your purchase! Your change is AED{change:.2f}.")
                            selected_item['stock'] -= quantity
                            break
                        else:
                            print("Insufficient payment. Please insert more money.")
                            amount_due -= payment
                    except ValueError:
                        print("Invalid payment amount. Please enter a valid number.")
            else:
                print(f"Sorry, not enough stock for {selected_item['name']}. Available stock: {selected_item['stock']}")
        else:
            print("Invalid selection. Please try again.")

    def add_item(self, name, price, stock):
        key = str(len(self.items) + 1).zfill(2)
        self.items[key] = {'name': name, 'price': price, 'stock': stock}
        print(f"Item '{name}' added successfully.")

vending_machine = VendingMachine()

# Display available items
vending_machine.display_items()

# Prompt user for input
selection = input("Enter the item number you wish to purchase: ")
quantity = int(input("Enter the quantity you wish to purchase: "))

# Purchase item
vending_machine.purchase_item(selection, quantity)

