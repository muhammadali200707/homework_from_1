from datetime import datetime
from typing import Optional
from uuid import uuid4

"""Multiple Inheritance"""  # ------------------------------------------------------------------------------------


class Iphone:
    def __init__(self, model: Optional[str], year: Optional[int], price: Optional[float]) -> None:
        self.model = model
        self.year = year
        self.price = price

    def datatime(self):
        time = datetime.now()
        print(time)

    def info(self):
        print(f"Model: {self.model} -- Year: {self.year} -- Price: {self.price}")

    def __repr__(self):
        return f"Model: {self.model} - - Year: {self.year} - - Price: {self.price}"


class Samsung:
    def phone_id(self):
        return str(uuid4())

    def battery_power(self):
        return int(100)


class Redmi(Iphone, Samsung):
    pass


# new_phone = Redmi('Redmi note 12 pro', 2023, 8_000_000)
# print(new_phone)


"""Multilevel Inheritance"""  # ---------------------------------------------------------------------------------


class Bmw:
    def run_bmw(self):
        print("BMW is running")

    def turn_of(self):
        print("Turn of is running")


class Tesla(Bmw):
    def charging(self):
        print("Tesla is charging")

    def battery_power(self):
        print("Battery is fully charged")


class Honda(Tesla):
    def refueling(self):
        print("Fuel is being poured into the engine")

    def car_wash(self):
        print("The car is being washed")


class Audi(Honda):
    def car_repair(self):
        print("The car is being repaired")


# car1 = Audi()
# car1.car_repair()
# car1.car_wash()
# car1.run_bmw()
# car1.turn_of()
# car1.battery_power()
# car1.charging()

"""Method Resolution Order => MRO"""  # ------------------------------------------------------------------------


class Instagram:
    def open(self):
        return "The Instagram app is opening "

    def logout(self):
        return "The Instagram app is logged out"


class Telegram:
    def open(self):
        return "The Telegram app is opening "

    def logout(self):
        return "The Telegram app is logged out"


class Safari:
    def open(self):
        return "The Safari app is opening "

    def logout(self):
        return "The Safari app is logged out"


class Tiktok:
    def open(self):
        return "The Tiktok app is opening "

    def logout(self):
        return "The Tiktok app is logged out"


class Photos:
    def open(self):
        return "The Photos app is opening "

    def logout(self):
        return "The Photos app is logged out"


class Translate:
    def open(self):
        return "The Translate app is opening "

    def logout(self):
        return "The Translate app is logged out"


class Yandex:
    def open(self):
        return "The Yandex app is opening "

    def logout(self):
        return "The Yandex app is logged out"


class Youtube(Instagram, Telegram, Safari, Tiktok, Photos, Translate, Yandex):
    def open(self):
        return "The Youtube app is opening "

    def logout(self):
        return "The Youtube app is logged out"


# app = Youtube()
# print(app.open())
# print(app.logout())

"""Single Inherit"""


class Uzb:
    def uzbekiston(self):
        print("The population of Uzbekistan")


class Usa(Uzb):
    def america(self):
        print("The population of Uzbekistan")


# population = Usa()
# population.uzbekiston()
# population.america()


"""Hierarchical Inherit """


class Father:
    def dad(self):
        print("Hello everyone")

    def dads_name(self):
        print("My name is John ")

    def dads_age(self):
        print("My age is 25")

    def dads_weight(self):
        print("My weight is 100 kg")

    def dads_height(self):
        print("My height is 195 sm")

    def dads_work(self):
        print("I work as lawyer")


class Son(Father):
    def son(self):
        print("Hello everyone I am Jack  and John is my father")


class Daughter(Father):
    def daughter(self):
        print("Hello everyone I am Anna and John is my father , Jack is my brother")


# person1 = Son()
# person2 = Daughter()
# person1.dad()
# person1.dads_name()
# person1.dads_age()
# person1.dads_weight()
# person1.dads_height()
# person1.dads_work()
# person1.son()
# person2.daughter()


"""Hybrid Inherit"""


class University:
    def univer(self):
        print("This function is in University")


class FirstStudent(University):
    def student(self):
        print("This function is in student 1. ")


class SecondStudent(University):
    def student2(self):
        print("This function is in student 2.")


class ThirdStudent(FirstStudent, University):
    def student3(self):
        print("This function is in student 3.")

# student1 = University()
# student1.univer()
