class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

person = Person("Abdul Hakim", 25)
print(person.get_name())  # Output: Abdul Hakim
print(person.get_age())   # Output: 25

person.set_name("Ryan Hakim")
person.set_age(30)

print(person.get_name())  # Output: Ryan Hakim
print(person.get_age())   # Output: 30

# Attempting to access private attribute directly will result in an AttributeError
# print(person.__name)  # This line will raise an AttributeError
