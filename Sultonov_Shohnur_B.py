from typing import Optional
from abc import ABC, abstractmethod
from math import sqrt, ceil


#  Sultonov Shohnur B - variant
# 3 - question________________________________________________________________________
class Persons:
    def __init__(self, name: str, age: Optional[int], address: str, phone: int) -> None:
        self.name = name
        self.age = age
        self._address = address
        self.__phone = phone

    @property
    def phone(self) -> int:
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        if isinstance(new_phone, int):
            self.__phone = new_phone
        else:
            raise TypeError('Phone must be an integer')

    def name(self):
        return f"I am {self.name}"

    def age(self):
        return f"I am {self.age} years old"

    def address(self):
        return f"I live {self._address}"

    def __repr__(self):
        return f"I am {self.name}, I am {self.age} years old, I live {self._address}, My phone number is {self.phone}"


# person1 = Persons('John', 18, 'john@gmail.com', 977777777)
# print(person1)
# print(person1.name)
# print(person1.age)
# print(person1.address())
# print(person1.phone)


# 4 - question____________________________________________________________________________________
class Phone:
    def __init__(self, model: str, price: str, color: str):
        self.__model = model
        self.__price = price
        self.__color = color

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if isinstance(new_model, str):
            self.__model = new_model
        else:
            raise TypeError('Model must be string')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, str):
            self.__price = new_price
        else:
            raise TypeError('Price must be string')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        if isinstance(new_color, str):
            self.__color = new_color
        else:
            raise TypeError('Color must be string')

    def __repr__(self):
        return f"Model: {self.model}, Price: {self.price}, Color: {self.color}"

    # phone = Phone('Iphone 14 pro', "1.200 $", "Black")
    # print(phone)
    # print(phone.model)
    # print(phone.price)
    # print(phone.color)


# 5 - question__________________________________________________________________________________________


class Home:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}"

    def __repr__(self):
        return f"Name: {self.name}, Address: {self.address}"

    def __bool__(self):
        if self.name is str:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.address))


# home1 = Home("House", "Tashkent")
# print(hash(home1))
# print(home1)


# 6 -question__________________________________________________________________________________________
"""
Example for Multilevel Inheritance
"""


class Tesla:
    def __init__(self, model: str, price: str, to_100: Optional[float]):
        self.model = model
        self.price = price
        self.to_100 = to_100

    def model(self):
        return f"This car's model is {self.model}"

    def price(self):
        return f"This car's price is {self.price}"

    def to_100(self):
        return f"In {self.to_100} seconds the car can up 100 km/h"


class Honda(Tesla):
    def __init__(self, color: str, speed: Optional[float]):
        self.color = color
        self.speed = speed
        super().__init__("Tesla", "70_000 $", 2.7)

    def color(self):
        return f"This car's color is {self.color}"

    def speed(self):
        return f"This car's speed is {self.speed}"


class Bmw(Honda):
    def __init__(self, factory: str):
        self.factory = factory
        super().__init__("Black", 260.8)

    def __repr__(self):
        return (f"Model: {self.model} -- Price: {self.price} -- To hundred: {self.to_100}  -- Speed: {self.speed}"
                f" Factory: {self.factory} -- Color: {self.color}")


# car1 = Bmw("Bmw")
# print(car1)


"""
Example for MRO 
"""


class Instagram:
    def name(self): return f"This app's name is Instagram"

    def __repr__(self):
        return f"This app's name is Instagram "


class Telegram:
    def name(self): return f"This app's name is {self.name}"

    def __repr__(self):
        return f"This app's name is Telegram"


class TikTok:

    def name(self): return f"This app's name is {self.name}"

    def __repr__(self):
        return f"This app's name is Tik Tok"


class App(Instagram, Telegram, TikTok):
    pass


# app = App()
# print(app)

# 8 - question_____________________________________________________
class Tv(ABC):
    @abstractmethod
    def turn_on(self):
        return 'Tv is turing on'

    @abstractmethod
    def turn_off(self):
        return 'Tv is turing off'


class Samsung(Tv):
    def turn_on(self):
        return 'Samsung is turning on'

    def turn_off(self):
        return 'Samsung is turning off'


class Roison(Tv):
    def turn_on(self):
        return 'Roison is turning on'

    def turn_off(self):
        return 'Roison is turning off'


# samsung = Samsung()
# print(samsung.turn_on())
# print(samsung.turn_off())
# roison = Roison()
# print(roison.turn_on())
# print(roison.turn_off())

# 7 - question_________________________________________________________________________________________
class Nexia:
    @classmethod
    def speed(cls): return f"This car's speed is 200 km/h "

    @staticmethod
    def add(x=7, y=3): return x + y


# car = Nexia
# print(car.speed())
# print(car.add())

# 1 - question__________________________________________________________________________________________________


class Math:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def math(self):
        print(sqrt(self.a * self.b))

    def __repr__(self):
        return f'{self.a} + {self.b} = {self.a + self.b}'


# math = Math(5, 5)
# print(math)


