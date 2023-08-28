class Fridge:
    contents = {}

    def add(self, product:str, quantity:float):
        self.contents[product] = quantity

    def remove(self, product:str, quantity:float):
        if self.check(product, quantity):
            self.contents[product] -= quantity
        else:
            print("No such product or quantity is not enough")

    def check(self, product:str, quantity:float):
        if product in self.contents:
            print(f"{product} found, removing...")
            if quantity <= self.contents[product]:
                return True
        return False

    def list_products(self, ):
        pass