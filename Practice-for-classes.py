# Exercise 1: Simple Class
#
# Create a simple class representing a "Person."
# Include attributes like name, age, and gender.
# Write methods to set and get these attributes.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set(self):
        self.name = input("set the name")
        self.age = input("set the age")
        self.gender = input("set the gender")

    def get(self):
        print(f'the name of the person is {self.name}')
        print(f'the age of the person is {self.age}')
        print(f'the gender of the person is {self.gender}')


person_instance = Person("hassan", 27, "male")


# Person.set(person_instance)
# Person.get(person_instance)


# Exercise 2: Bank Account Class
#
# Create a class representing a bank account. Include attributes like account_number,
# account_holder, and balance. Write methods to deposit and withdraw money,
# and a method to display the account details.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_details(self):
        print(f'your account number is {self.account_number}')
        print(f'Your are {self.account_holder}')
        print(f'Your balance is {self.balance}')


# Create instances of the BankAccount class
person1 = BankAccount(10500100, "Hassan", 50000)
person2 = BankAccount(10550101, "A", 20000)

# Call methods on instances
person1.deposit(1000)
person2.withdraw(5000)

# Display account details
person1.display_account_details()
person2.display_account_details()


# Exercise 3: Car Class
#
# Create a class representing a car. Include attributes like make, model, year, and mileage.
# Write methods to update the mileage and display information about the car.

class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self.mileage = mileage

    def update_mileage(self, update):
        self.mileage += update

    def display_info(self):
        print(self.model, end=' ')
        print(self.year, end=' ')
        print(self.mileage, end=' ')


car1 = Car("lambo", 2020, 10000)
car2 = Car("Honda", 2020, 50000)

car1.update_mileage(5000)

print(car1.display_info())
print(car2.display_info())