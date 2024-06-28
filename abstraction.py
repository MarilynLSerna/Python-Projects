

from abc import ABC, abstractmethod  

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name  

    # Abstract method for making a sound 
    @abstractmethod
    def make_sound(self):
        pass

    # Regular method to display the name of the animal
    def display_name(self):
        return "Animal name: {}".format(self.name)

# Subclass implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Creating an object that utilizes both parent and child methods
dog = Dog("Buddy")
print(dog.display_name())   
print(dog.make_sound())     
