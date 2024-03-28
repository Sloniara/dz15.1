class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        total_price = self.price * len(self) + other.price * len(other)
        total_quantity = len(self) + len(other)
        return total_price, total_quantity


class Smartphone(Product):
    def __init__(self, name, price, quantity, performance, model, memory, color):
        super().__init__(name, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{super().__str__()} Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}"


class LawnGrass(Product):
    def __init__(self, name, price, quantity, country, germination_period, color):
        super().__init__(name, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{super().__str__()} Страна-производитель: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"


class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты классов Product, Smartphone и LawnGrass")
        self.__products.append(product)

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            products_info.append(str(product))
        return products_info

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        return Product(name, description, price, quantity_in_stock)
