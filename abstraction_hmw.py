from abc import ABC, abstractmethod
from typing import Optional


class Worker(ABC):
    def __init__(self,
                 name: Optional[str]):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @abstractmethod
    def who_am_i(self) -> str:
        return f"I am + {self.__name} "

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def job(self):
        pass

    @abstractmethod
    def experience(self):
        pass

    @abstractmethod
    def annual_salary(self):
        pass


class Accountant(Worker):
    def __init__(self, name: str, age: int, salary_month: float, insurance: float):
        self.name = name
        self.age = age
        self.salary_month = salary_month
        self.insurance = insurance
        super().__init__(name="John")

    def who_am_i(self):
        return f"I am  {self.name}"

    def age(self):
        return f'I am {self.age}'

    def job(self):
        return f'I am Accountant'

    def experience(self):
        return f'I have 18 years of experience'

    def annual_salary(self):
        return f'{self.salary_month * 12 - self.insurance}'

    def __repr__(self):
        return f'{self.name} {self.age}'


class Reception(Worker):
    def __init__(self, name: str, age: int, salary_month: float, insurance: float):
        self.name = name
        self.age = age
        self.salary_month = salary_month
        self.insurance = insurance
        super().__init__(name="Ali")

    def who_am_i(self):
        return f"I am  {self.name}"

    def age(self):
        return f'I am {self.age}'

    def job(self):
        return f'I am Reception'

    def experience(self):
        return f'I have 5 years of experience'

    def annual_salary(self):
        return f'{self.salary_month * 12 - self.insurance}'

    def __repr__(self):
        return f'{self.name} {self.age}'


person = Accountant("Ali", 25, 12_000_000, 50_000)
print(person.annual_salary())
print(person.job())
print(person.experience())

worker = Reception("Ali", 20, 10_000_000, 80_000)
print(person.annual_salary())
print(person.job())
print(person.experience())
# shunday qilib hamasini chaqirsa boladi
