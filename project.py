class User:
    species = "OOP"

    def __init__(self, username, password, age, email, address):
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.address = address

    def get_information(self):
        return f'{self.username} -- {self.password} -- {self.age} --  {self.email} --  {self.address}'

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username
        return new_username

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email

    def get_address(self):
        return self.password

    def set_address(self, address):
        self.address = address


"""   
    @classmethod
    def get_species(cls):
      return f' This type {cls.species}'

    @classmethod
    def set_species(cls, new_species):
     cls.species = new_species
 

User.set_species('Backend')
print(User.get_species())
"""

""" Set instance method ---> USERNAME
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.set_username('Jack')
print(user1.get_information())
"""

""" Set with attributes ---> USERNAME
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.username = 'Ali'
print(user1.get_information())
"""

""" Set instance method ---> PASSWORD
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.set_password('admin123')
print(user1.get_information())
"""

""" Set with attributes ---> PASSWORD
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.password = 'ali123'
print(user1.get_information())
"""

""" Set instance method ---> AGE
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.set_age('90')
print(user1.get_information())
"""

""" Set with attributes ---> AGE
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.age = '99'
print(user1.get_information())
"""

""" Set instance method ---> EMAIL
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.set_email('ali@gmail.com')
print(user1.get_information())
"""

""" Set with attributes ---> EMAIL
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.email = 'shox@gmail.com'
print(user1.get_information())
"""

""" Set instance method ---> ADDRESS
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.set_address('ali@gmail.com')
print(user1.get_information())
"""

""" Set with attributes ---> ADDRESS
user1 = User('John', '123456', '18', 'jhon@gamil.com>', 'USA')
user1.address = 'shox@gmail.com'
print(user1.get_information())
"""
