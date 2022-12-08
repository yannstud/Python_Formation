class Buyings:
    def __init__(self):
        self.product = {}

    def add(self, name, price):
        self.product[name] = price

    def show(self):
        print('----------------------')
        for i, p in enumerate(self.product):
            print(f'{i} : {p} - {self.product[p]}')

    def delete(self, name):
        if name in self.product:
            del self.product[name]
        else:
            print("Error: Invalid product")

    def total_price(self):
        ret = 0.0
        for product, value in self.product.items():
            ret += value
        print(f"Total price: {ret}")

buyings = Buyings()

buyings.add("Banana", 3.6)
buyings.add("Egg", 2.5)
buyings.add("Salad", 3)

while True:
    cmd = input("Enter a command (+: Add, s: Delete, t: Total price, a: Print, q: Quit): ")

    if cmd == '+':
        product = input("Enter the name of the product: ")
        price = float(input("Enter the price: "))
        buyings.add(product, price)
    elif cmd == "t":
        print(buyings.total_price())
    elif cmd == "s":
        name = input("Enter the name of the product to delete")
        buyings.delete(name)
    elif cmd == "a":
        buyings.show()
    elif cmd == "q":
        break
    else:
        print("Invalid command")
