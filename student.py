class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20) #object 1
student2 = Student("Bob", 22) #object 2
print(student1.name)  # Output: Alice
print(student2.name)   # Output: Bob