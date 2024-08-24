# Liskov Substitution Principle (LSP) example


# Incorrect usage of LSP
class WrongBird:
    def __init__(self, name: str):
        self.name = name

    def fly(self):
        # This method assumes all birds can fly, which is incorrect
        print(f"wrong_usage {self.name} is flying.")


bird_1 = WrongBird("eagle")
bird_2 = WrongBird("penguin")

# This will print a message saying the penguin is flying, which is incorrect
bird_2.fly()


# Correct usage of LSP
class CorrectBird:
    def __init__(self, name: str):
        self.name = name


# Create a subclass of CorrectBird for birds that can fly
class FlyingBird(CorrectBird):
    def fly(self):
        # This method is specific to birds that can fly
        print(f"correct_usage {self.name} is flying.")


# Create instances of CorrectBird and FlyingBird
b1 = CorrectBird("penguin")
# This instance of CorrectBird does not have a fly method

b2 = FlyingBird("eagle")
# This instance of FlyingBird has a fly method

# This will print a message saying the eagle is flying
b2.fly()
