class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} located in {self.location}"
class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def __str__(self):
        return f"{self.name}, {self.age} years old, attends {self.school}"
    