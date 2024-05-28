from typing import Optional, List


class Car:
    def __init__(self, car_reg_number: str, phone: Optional[str] = None):
        self.__car_reg_number = car_reg_number
        self.__phone = phone

    @property
    def car_reg_number(self):
        return self.__car_reg_number

    @car_reg_number.setter
    def car_reg_number(self, other):
        if isinstance(other, str):
            self.__car_reg_number = other
        else:
            raise Exception('Car reg number must be "str"')

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, other):
        if isinstance(other, str):
            self.__phone = other
        else:
            raise Exception('Car reg number must be "str"')


car1 = Car("01X592HA", "1111")
car2 = Car("80A555AA", "2222")
car3 = Car("90B999BB", "3333")
car4 = Car("40Z777ZZ", "4444")

cars_list: List[Car] = [car1, car2, car3, car4]


class User:
    def __init__(self,
                 username: str,
                 email: Optional[str] = None,
                 address: Optional[str] = None,
                 cars: Optional[List[Car]] = None):
        self.__username = username
        self.email = email
        self.address = address
        self.__cars = cars or []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, other):
        if isinstance(other, str):
            self.__username = other
        else:
            raise Exception('Username must be "str"')

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, other):
        if isinstance(other, str):
            self.__cars = other
        else:
            raise Exception('Username must be "str"')

        # writing setter and getter method


ali = User("Ali", cars=[car1, car2])
sherzod = User('Sherzod', cars=[car3, ])

users_list = [ali, sherzod]


def get_user_by_username(username: str) -> Optional[User]:
    for user in users_list:
        if user.username == username:
            return user
    return None


def get_phone_by_car_reg_number(car_reg_number: str, cars_list: List[Car]) -> Optional[Car]:
    for car in cars_list:
        if car.car_reg_number == car_reg_number:
            pn = car.phone
            return car

    raise Exception(f'{car_reg_number} is not defined')


def send_message():
    username = input('Enter your username: ')
    car_reg_number = input('Enter your car reg number: ')
    user = get_user_by_username(username)
    car = get_phone_by_car_reg_number(car_reg_number, cars_list)

    if not user:
        raise Exception(f'{username} is not defined')
    else:
        # Send message logic
        if car in user.cars:
            print(f'{user.username} => {car.phone}')
        else:
            print(f'{car_reg_number} does not belong to {username}')


send_message()