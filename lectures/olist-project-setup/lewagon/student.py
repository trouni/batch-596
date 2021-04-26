from datetime import date


class Student:
    # class attribute
    school = "Le Wagon"

    # The constructor is run when calling Student()
    def __init__(self, name, age):
        # instance variables (STATE)
        self.name = name
        self.age = age

    # BEHAVIOR - instance methods
    def says(self, something):
        print(f"{self.name} says {something}")

    def becomes_one_year_older(self):
        # instance variables are accessible throughout the instance
        # all instance methods can access the instance variables
        self.age += 1

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # cls represents the class Student
        age = date.today().year - birth_year
        return cls(name, age)
