class Car:
    factory = "BMW is the best car!"

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    @staticmethod
    def multiply():
        print(8 * 5)

    @classmethod
    def get_car(cls):
        return cls.factory

    @classmethod
    def set_car(cls, x):
        if isinstance(x, str):
            cls.factory = x
        else:
            print("X is not string")


car1 = Car("BMW", "blue", "65_000")
# car1.set_car("Ford")
# print(car1.factory)
