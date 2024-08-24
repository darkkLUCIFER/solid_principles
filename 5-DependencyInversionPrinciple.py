# Dependency Inversion Principle (DIP) example
from abc import ABC, abstractmethod


# Without DIP
class Database:
    # This class represents a low-level module (database access)
    def save_employee(self, name):
        # This method saves an employee to the database
        print(f"Saving employee {name} to database")


class Employee:
    # This class represents a high-level module (business logic)
    def __init__(self, name):
        # Initialize the employee with a name
        self.name = name

    def save(self):
        # This method saves the employee to the database
        # However, it creates a tight coupling with the Database class
        # This is a problem because it makes the Employee class dependent on the Database class
        database = Database()
        database.save_employee(self.name)


# With DIP
class EmployeeRepository(ABC):
    # This class represents an abstraction (interface) for employee repositories
    @abstractmethod
    def save_employee(self, name):
        # This method is an abstract method that must be implemented by any concrete repository
        pass


class DatabaseEmployeeRepository(EmployeeRepository):
    # This class represents a concrete implementation of the EmployeeRepository interface
    # It uses the Database class to save employees to the database
    def save_employee(self, name):
        # This method saves an employee to the database using the Database class
        print(f"Saving employee {name} to database")


class Employee:
    # This class represents a high-level module (business logic)
    def __init__(self, name, repository: EmployeeRepository):
        # Initialize the employee with a name and a repository
        # The repository is an instance of EmployeeRepository, which is an abstraction
        self.name = name
        self.repository = repository

    def save(self):
        # This method saves the employee to the repository
        # The repository is responsible for saving the employee to the database
        self.repository.save_employee(self.name)


# Usage
repository = DatabaseEmployeeRepository()
# Create a concrete instance of the EmployeeRepository interface
employee = Employee("John Doe", repository)
# Create an instance of the Employee class, passing in the repository
employee.save()
# Save the employee to the repository
