from typing import Optional, List


class Car:
    def __init__(self, car_reg_number: str, phone: Optional[str] = None):
        self.__car_reg_number = car_reg_number
        self.__phone = phone

    def get_car_reg_number(self) -> str:
        return self.__car_reg_number

    @property
    def car_reg_number(self):
        print("Getter method is calling")
        return self.__car_reg_number

    @car_reg_number.setter
    def car_reg_number(self, other):
        if isinstance(other, str):
            self.__car_reg_number = other
        else:
            raise TypeError("Car reg number must be a string")

    def get_phone(self):
        return self.__phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, other):
        if isinstance(other, str):
            self.__phone = other
        else:
            raise TypeError("Phone must be a string")


car1 = Car("01X592HA", "1111")
car2 = Car("80A555AA", "2222")
car3 = Car("90B999BB", "3333")
car4 = Car("40Z777ZZ", "4444")

cars_list: List[Car] = [car1, car2, car3, car4]


class User:
    def __init__(self,
                 username: str,
                 email: Optional[str],
                 address: Optional[str],
                 cars: List[Car]):
        self.__username = username
        self.email = email
        self.address = address
        self.__cars = cars or []

    def get_username(self):
        return self.__username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, other):
        if isinstance(other, str):
            self.__username = other

    def get_cars(self):
        return self.__cars

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, other):
        if isinstance(other, List):
            self.__cars = other
        else:
            raise TypeError("Car must be a List")


john = User('John', 'john@gmail.com', 'USA', cars=[car1, car2, car3])
anna = User('Anna', 'anna@gmail.com', 'Korea', cars=[car4])

user_list = [john, anna]


def get_user_by_username(username: str) -> Optional[User]:
    for user in user_list:
        if user.username == username:
            return user
    return None


def get_phone_by_car_reg_number(car_reg_number: str, cars_list: List[Car]):
    for car in cars_list:
        if car.car_reg_number == car_reg_number:
            pn = car.phone
            return pn
    raise Exception(f'{car_reg_number} is not defined')


def send_message():
    username = input('Enter your username: ')
    car_reg_number = input('Enter your car reg number')
    user = get_user_by_username(username)
    phone = get_phone_by_car_reg_number(car_reg_number)

    if not user:
        raise Exception(f'{username} is not defined')
    else:
        if car_reg_number in user:
            print("Find")


send_message()
