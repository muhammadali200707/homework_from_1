# from typing import Optional
#
#
# class Man:
#     def __init__(self,
#                  fullname: str,
#                  age: Optional[int],
#                  weight: Optional[int],
#                  height: Optional[int]):
#         self.__fullname = fullname
#         self.__age = age
#         self.weight = weight
#         self.height = height
#
#     @property
#     def fullname(self):
#         return self.__fullname
#
#     @fullname.setter
#     def fullname(self, other):
#         self.__fullname = other
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, other):
#         self.__age = other
#
#     def get_info(self):
#         print(
#             f" My name is {self.fullname},"
#             f" I'm {self.age} years old,"
#             f" My weight is {self.weight},"
#             f" My height is {self.height}")
#
#     def role(self): print("I am Man ")
#
#
# class Husband(Man):
#     def role(self): print("I am Husband ")
#
#
# class Trainer(Man):
#     def role(self): print("I am Trainer ")
#
#
# class Father(Man):
#     def role(self): print("I am Father ")
#
#
# husband = Husband("Ali", 17, 80, 180)
# trainer = Trainer("John", 25, 90, 190)
# father = Father("Anna", 18, 55, 175)
# husband.get_info()
# husband.role()
# trainer.get_info()
# trainer.role()
# father.get_info()
# father.role()

# ______________________________________________________________________________________________________________________
# class Person:
#     def __init__(self, fullname: str):
#         self.__fullname = fullname
#
#     @property
#     def fullname(self):
#         return self.__fullname
#
#     @fullname.setter
#     def fullname(self, new_fullname: str):
#         self.__fullname = new_fullname
#
#
# class Accountant(Person):
#     def __init__(self, salary_moth: float, insurance: float):
#         self.__salary_moth = salary_moth
#         self.__insurance = insurance
#         super().__init__(fullname="Ali")
#
#     @property
#     def salary_moth(self):
#         return self.__salary_moth
#
#     @salary_moth.setter
#     def salary_moth(self, other):
#         self.__salary_moth = other
#
#     @property
#     def insurance(self):
#         return self.__insurance
#
#     @insurance.setter
#     def insurance(self, other):
#         self.__insurance = other
#
#     def annual_salary(self):
#         result = (self.__salary_moth * 12) - self.__insurance
#         print("Accountant annual salary:", result)
#
#
# class Guard(Person):
#     def __init__(self, salary_moth: float, insurance: float):
#         self.__salary_moth = salary_moth
#         self.__insurance = insurance
#         super().__init__(fullname="Ali")
#
#     @property
#     def salary_moth(self):
#         return self.__salary_moth
#
#     @salary_moth.setter
#     def salary_moth(self, other):
#         self.__salary_moth = other
#
#     @property
#     def insurance(self):
#         return self.__insurance
#
#     @insurance.setter
#     def insurance(self, other):
#         self.__insurance = other
#
#     def annual_salary(self):
#         result = (self.__salary_moth * 12) - self.__insurance
#         print("Guard annual salary:", result)
#
#
# class Secretary(Person):
#     def __init__(self, salary_moth: float, insurance: float):
#         self.__salary_moth = salary_moth
#         self.__insurance = insurance
#         super().__init__(fullname="Ali")
#
#     @property
#     def salary_moth(self):
#         return self.__salary_moth
#
#     @salary_moth.setter
#     def salary_moth(self, other):
#         self.__salary_moth = other
#
#     @property
#     def insurance(self):
#         return self.__insurance
#
#     @insurance.setter
#     def insurance(self, other):
#         self.__insurance = other
#
#     def annual_salary(self):
#         result = (self.__salary_moth * 12) - self.__insurance
#         print("Secretary annual salary:", result)
#
#
# accountant = Accountant(100, 10)
# accountant.annual_salary()
# guard = Guard(50, 10)
# guard.annual_salary()
# secretary = Secretary(80, 7)
# secretary.annual_salary()


# class Anna:
#     def __init__(self, full_name: str, age: int, phone_number: int, bank_number: int):
#         self.fullname = full_name
#         self.age = age
#         self.__phone_number = phone_number
#         self.__bank_number = bank_number
#
#     @property
#     def phone_number(self):
#         return self.__phone_number
#
#     @phone_number.setter
#     def phone_number(self, other):
#         self.__phone_number = other
#
#     @property
#     def bank_number(self):
#         return self.__bank_number
#
#     @bank_number.setter
#     def bank_number(self, other):
#         self.__bank_number = other
#
#     def get_public_info(self):
#         print(f"My name is {self.fullname}, I am  {self.age} years old.")
#
#     def get_private_info(self):
#         print(f"My phone number is {self.phone_number}, My bank number is {self.bank_number}")
#
#
# anna = Anna("Anna", 20, 77777777, 12090)
# anna.get_public_info()
# anna.get_private_info()


# class Protect:
#     def __init__(self, name: str):
#         self._name = name
#
#     def get_info(self):
#         print(f" Hello my name is {self._name}")
#
#
# protect = Protect('Ali')
# protect.get_info()
