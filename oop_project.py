from typing import Optional
from math import sqrt


class Computer:
    model_of_computer = "Dell"

    def __init__(self, name: Optional[str] = None,
                 model: Optional[str] = None,
                 color: Optional[str] = None,
                 price: Optional[float] = None):
        self.name = name
        self.model = model
        self.color = color
        self.price = price

    @staticmethod
    def square(number: int) -> float:
        return sqrt(number)

    # number1 = Computer.square(25)
    # print(f"The square of {number1}")
    @staticmethod
    def identify() -> None:
        age = int(input("Enter your age --> "))
        if age > 30:
            print(f"Your age is {age} years old \nSorry here only for young people,You can't enter to there")
        elif 0 > age > 130:
            print(f'Invalid input for your age \nYou entered this{age} years old')
        else:
            print(f"Your age is {age} years \nYou can enter, welcome to the party")

    # Computer.identify()

    @classmethod
    def get_computer(cls) -> str:
        return f' This computer is made by {cls.model_of_computer}'

    # computer1 = Computer.get_computer()
    # print(computer1)

    @classmethod
    def set_factory(cls) -> None:
        if isinstance(cls.model_of_computer, str):
            cls.model_of_computer = 'Mac'
        else:
            print("You cannot set factory because it is not a string")

    # Computer.set_factory()
    # new_comp = Computer.model_of_computer
    # print(f'This is new computer factory --> {new_comp}')

    def comp_info(self):
        print(f'Name: {self.name} -- Model : {self.model} -- Color: {self.color} -- Price: {self.price}')

    # camp1 = Computer("Laptop")
    # camp1.comp_info()

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self.name = value
        else:
            "Name must be an string"


# name1 = Computer("Toshiba")
# print(name1.name)
