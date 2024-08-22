# Open-Closed Principle (OCP) example

from abc import ABC, abstractmethod


# Wrong usage: modifying the existing class to add new behavior
class AnimalWrong:
    """
        Represents an animal with a name.
    """

    def __init__(self, name):
        self.name = name

    def sound(self):
        """
            Makes the animal sound.
        """
        # This is a bad practice, as we're modifying the existing class to add new behavior
        if self.name == "cat":
            print("wrong: meow")
        elif self.name == "dog":
            print("wrong: woof")
        # What if we want to add a new animal? We'd have to modify this class again!


cat_1 = AnimalWrong("cat")
cat_1.sound()

dog_1 = AnimalWrong("dog")
dog_1.sound()


# Correct usage: using inheritance and polymorphism to add new behavior
class AnimalCorrect(ABC):
    """
        Represents an animal with a name.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        """
            Makes the animal sound.
        """
        pass


class Snake(AnimalCorrect):
    """
        Represents a snake.
    """

    def sound(self):
        print("correct: hiss")


class Dog(AnimalCorrect):
    """
        Represents a dog.
    """

    def sound(self):
        print("correct: woof")


snake = Snake("snake")
snake.sound()

dog = Dog("dog")
dog.sound()


# Now, if we want to add a new animal, we can simply create a new class without modifying the existing code!
class Lion(AnimalCorrect):
    """
        Represents a lion.
    """

    def sound(self):
        print("correct: roar")


lion = Lion("lion")
lion.sound()
