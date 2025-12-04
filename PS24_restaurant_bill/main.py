# Create a Restaurant class that stores menu items in a dictionary and prints the bill.

class Restaurant:
    def __init__(self, menu):
        self.menu = menu

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"- {item}: {price}")

    def calculate_bill(self, orders):
        total = 0
        for item, qty in orders.items():
            if item in self.menu:
                total += self.menu[item] * qty
        return total


def main():
    menu = {
        "pizza": 12.0,
        "pasta": 10.0,
        "salad": 7.5,
        "soda": 2.5,
    }
    restaurant = Restaurant(menu)
    restaurant.print_menu()
    orders = {}
    while True:
        item = input("Enter item to order (blank to finish): ").lower()
        if not item:
            break
        if item not in menu:
            print("Item not in menu.")
            continue
        qty = int(input("Enter quantity: "))
        orders[item] = orders.get(item, 0) + qty
    total = restaurant.calculate_bill(orders)
    print(f"Orders: {orders}")
    print(f"Total bill: {total}")


if __name__ == "__main__":
    main()
