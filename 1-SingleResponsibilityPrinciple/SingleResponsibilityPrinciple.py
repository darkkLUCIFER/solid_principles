# Single Responsibility Principle (SRP) example

class Person:
    # This class has a single responsibility: to represent a person with a name and age.

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # This method shows the person's details in a human-readable format.
    def show(self):
        return f"{self.name} is {self.age} years old"


class Db:
    # This class has a single responsibility: to interact with the database.
    def __init__(self):
        # Note that we don't need to pass name and age to the Db class, as it's not its responsibility.
        pass

    # This method saves data to the database.
    def db_save(self, person: Person):
        # Here, we're assuming that we have a person object with name and age attributes.
        # We can save this data to the database.
        print(f"Saving {person.name} and {person.age} to the database")

    # This method represents a new feature that we might want to add to the Db class.
    # For example, it could be a method to retrieve data from the database.
    def new_feature(self):
        pass


# Now, let's create a person and save it to the database.
p1 = Person("John", 25)
db = Db()
db.db_save(p1)

# Output:
# Saving John and 25 to the database
