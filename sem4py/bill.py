class Bill:
    def __init__(self, date, customer_name):
        self.date = date
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name, rate, quantity):
        total_amount = rate * quantity
        self.items.append({
            'item_name': item_name,
            'rate': rate,
            'quantity': quantity,
            'total_amount': total_amount
        })

    def display_bill(self):
        print("Date:", self.date)
        print("Customer Name:", self.customer_name)
        print("===================================")
        print("Item Name\tRate\tQuantity\tTotal Amount")
        print("-----------------------------------")
        for item in self.items:
            print(f"{item['item_name']}\t\t{item['rate']}\t{item['quantity']}\t\t{item['total_amount']}")
        print("===================================")

if __name__ == "__main__":
    # Create a new bill
    my_bill = Bill("2023-07-20", "John Doe")

    # Add items to the bill
    my_bill.add_item("Item 1", 10, 2)
    my_bill.add_item("Item 2", 15, 3)
    my_bill.add_item("Item 3", 5, 4)

    # Display the bill
    my_bill.display_bill()
