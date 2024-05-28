class Car:
    def __init__(self, model, price, color):
        self.model = model
        self.__price = price
        self.__color = color

    def get_price(self):
        return self.__price

    @property
    def price(self):
        print("Getter method is calling")
        return self.__price

    @price.setter
    def price(self, value):
        print("Setter method is calling")
        if isinstance(value, int):
            self.__price = value
        else:
            raise TypeError('Price must be a integer')

    def get_color(self):
        return self.__color

    @property
    def color(self):
        print("Getter method is calling")
        return self.__color

    @color.setter
    def color(self, other):
        print("Setter method is calling")
        if isinstance(other, str):
            self.__price = other
        else:
            raise TypeError('Price must be a string')


bmw = Car('BMW', 13000, 'red')
# bmw.price = 10000
# print(bmw.get_price())
# bmw.color = "Black"
# print(bmw.color)