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

Person.set(person_instance)
Person.get(person_instance)