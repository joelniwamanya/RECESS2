class Person:
    def __init__(self, name, Id_no):
        self.name = name
        self.Id_no = Id_no

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.Id_no}")

class Student(Person):
    def __init__(self, name, Id_no, major):
        super().__init__(name, Id_no)
        self.major = major

    def display_details(self):
        self.display_person()
        print(f"Major: {self.major}")
        
student1 = Student("Joel", "24/U/10192", "Software Engineering")
student1.display_details()
class Lecturer(Person):
    def __init__(self, name, Id_no, department):
        super().__init__(name, Id_no)
        self.department = department

    def display_details(self):
        self.display_person()
        print(f"Department: {self.department}")

lecturer1 = Lecturer("Dr. Smith", "24/L/292292", "Computer Science")
lecturer1.display_details()