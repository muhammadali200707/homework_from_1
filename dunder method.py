from typing import Optional


class Phone:
    def __init__(self,
                 factory: str,
                 model: Optional[str] = None,
                 price: Optional[str] = None) -> None:
        self.factory = factory
        self.model = model
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return len(self.factory) > len(other.factory) and len(self.model) > len(other.model) and len(self.price) > len(
            other.price)

    def __repr__(self):
        return f'{self.factory} -- {self.model} -- {self.price}'

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __add__(self, other):
        return len(self.factory) + len(other.factory) + len(self.model) + len(other.model) + len(
            self.price + other.price)

    def __bool__(self):
        return self.price > '1.900'

    def hash(self):
        return hash((self.factory, self.model, self.price))


phone1 = Phone("Iphone  ", 'Iphone 14 pro', '4')
phone2 = Phone("Samsung", 'S21 Ultra', '5')


# print(phone1 == phone2)  # This checks whether two numbers are equal
# print(phone1 > phone2)  # This checks if the length of the first data is longer than the length of the second
# print(phone1 < phone2)  # This checks if the length of the first data is shorter than the length of the second
# print(phone1 >= phone2)  # This checks if the first number is greater than or equal to the second number
# print(phone1 + phone2)  #This is the length of the two pieces of data
# print(bool(phone1))  #It checks if it is greater or less than the given value
# print(bool(phone2))  #It checks if it is greater or less than the given value
# print(hash(phone1.factory)) #It hashes the given data
# print(hash(phone1.model))  #It hashes the given data
# print(hash(phone1.price))  #It hashes the given data
class Math:
    def __init__(self, number: int) -> None:
        self.number = number

    def __mult__(self, other) -> int:
        return self.number * other.number

    def __sub__(self, other) -> int:
        return self.number - other.number


# num1 = Math(7)
# num2 = Math(5)
# print(num1.number * num2.number)  # This outputs the multiplication


# number1 = Math(120)
# number2 = Math(23)
# print(number1 - number2)  #This outputs the  subtraction


# count = 0
# a = " A boy is playing there."
# b = "There is a playground."
# c = "An aeroplane is in the sky."
# d = "The sky is pink."
# e = "Alphabets and numbers are allowed in the password."
# r = "A boy is playing there."
# q = "There is a playground."
# t = "An aeroplane is in the sky."
# o = "The sky is pink."
# p = "Alphabets and numbers are allowed in the password."
#
# if "is" in a:
#     count += 1
# if "is" in b:
#     count += 1
# if "is" in c:
#     count += 1
# if "is" in d:
#     count += 1
# if "is" in e:
#     count += 1
# if "is" in r:
#     count += 1
# if "is" in q:
#     count += 1
# if "is" in t:
#     count += 1
# if "is" in o:
#     count += 1
# if "is" in p:
#     count += 1
#
# print(f" Is so'zi  {count} marta qatnashgan ")

