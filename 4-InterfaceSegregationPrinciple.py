# Interface Segregation Principle (ISP) example
from abc import ABC, abstractmethod


# Incorrect usage of ISP
class WrongShape(ABC):
    # This interface is trying to define multiple shapes (circle, square, rectangle) at once
    # This is a problem because not all shapes will implement all of these methods

    @abstractmethod
    def circle(self):
        # This method is specific to circles
        pass

    @abstractmethod
    def square(self):
        # This method is specific to squares
        pass

    @abstractmethod
    def rectangle(self):
        # This method is specific to rectangles
        pass


class WrongCircle(WrongShape):
    # This class is trying to implement the WrongShape interface
    # But it's only implementing the circle method, and leaving the others unimplemented
    def circle(self):
        print("Circle")

    def square(self):
        # This method is not implemented for circles
        pass

    def rectangle(self):
        # This method is not implemented for circles
        pass


# Correct usage of ISP
class CorrectShape(ABC):
    # This interface is more general and only defines a single method (draw)
    # This allows different shapes to implement this method in their own way
    @abstractmethod
    def draw(self):
        # This method can be implemented by any shape
        pass


class CorrectCircle(CorrectShape):
    # This class is implementing the CorrectShape interface
    # It's only implementing the draw method, which is specific to circles
    def draw(self):
        print("Circle")


class CorrectSquare(CorrectShape):
    # This class is also implementing the CorrectShape interface
    # It's implementing the draw method in a way that's specific to squares
    def draw(self):
        print("Square")
