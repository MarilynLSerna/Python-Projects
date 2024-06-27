
class Person:
    def __init__(self, name, age):
        self.name = name        # Public attribute
        self._age = age         # Protected attribute
        self.__password = "secret"  # Private attribute

    # Public method to get person's details
    def get_details(self):
        return "Name: {}, Age: {}".format(self.name, self._age)

    # Protected method to change the age
    def _set_age(self, age):
        self._age = age

    # Public method to set the password, modifies private attribute
    def set_password(self, password):
        self.__password = password


# Creating an object of the Person class
person = Person("Alice", 30)

# Utilizing public method
print(person.get_details())  

# Utilizing public method to set password
person.set_password("new_secret")

# Utilizing protected method 
person._set_age(35)
print(person.get_details()) 
