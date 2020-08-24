# Python comes with a module called abc which provides useful stuff
#  for abstract class.
# We can define a class as an abstract class by abc.ABC and define a 
# method as an abstract method by abc.abstractmethod. ABC is the 
# abbreviation of abstract base class.

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
# a=Animal()

class Cat(Animal):
    def move(self):
        print("Cat Moves")

c=Cat()
c.move()