# write realtime example program using multiple & multilevel inheritance.

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Intermediate class for multilevel inheritance (Employee inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_employee_details(self):
        self.show_details()
        print(f"Employee ID: {self.employee_id}")

# Multiple inheritance: Developer inherits from Employee and TechSkill
class TechSkill:
    def __init__(self, skill):
        self.skill = skill

    def show_skill(self):
        print(f"Technical Skill: {self.skill}")

class Developer(Employee, TechSkill):
    def __init__(self, name, age, employee_id, skill):
        super().__init__(name, age, employee_id)
        TechSkill.__init__(self,skill)

    def show_developer_details(self):
        self.show_employee_details()
        self.show_skill()

# Another class for multiple inheritance: Manager
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def show_manager_details(self):
        self.show_employee_details()
        print(f"Department: {self.department}")

# Multilevel Inheritance: Intern -> Junior Developer -> Senior Developer
class Intern(Developer):
    def __init__(self, name, age, employee_id, skill, duration):
        super().__init__(name, age, employee_id, skill)
        self.duration = duration

    def show_intern_details(self):
        self.show_developer_details()
        print(f"Internship Duration: {self.duration} months")

class JuniorDeveloper(Intern):
    def __init__(self, name, age, employee_id, skill, duration, project):
        super().__init__(name, age, employee_id, skill, duration)
        self.project = project

    def show_junior_developer_details(self):
        self.show_intern_details()
        print(f"Project Assigned: {self.project}")

class SeniorDeveloper(JuniorDeveloper):
    def __init__(self, name, age, employee_id, skill, duration, project, level):
        super().__init__(name, age, employee_id, skill, duration, project)
        self.level = level

    def show_senior_developer_details(self):
        self.show_junior_developer_details()
        print(f"Seniority Level: {self.level}")

# Example of Multiple Inheritance
print("=== Multiple Inheritance Example ===")
developer = Developer("Alice", 28, "D123", "Python")
developer.show_developer_details()

print("\n=== Multiple Inheritance with Manager ===")
manager = Manager("Bob", 35, "M234", "Sales")
manager.show_manager_details()

# Example of Multilevel Inheritance
print("\n=== Multilevel Inheritance Example ===")
senior_dev = SeniorDeveloper("Charlie", 32, "SD456", "Java", 12, "AI Project", "Level 2")
senior_dev.show_senior_developer_details()

print(SeniorDeveloper.__mro__)

""" # Base class
class A:
    def __init__(self):
        print("Initializing A")
    
    def method(self):
        print("Method in A")

# Intermediate classes
class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing B")
    
    def method(self):
        print("Method in B")
        super().method()

class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing C")
    
    def method(self):
        print("Method in C")
        super().method()

# Diamond inheritance
class D(B, C):
    def __init__(self):
        super().__init__()
        print("Initializing D")
    
    def method(self):
        print("Method in D")
        super().method()

# Instantiate D
print("=== Diamond Problem Example ===")
d = D()
d.method()

# View MRO
print("\nMRO of class D:")
for cls in D.__mro__:
    print(cls)
 """