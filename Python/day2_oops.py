""" OOPs - Object Oriented Programming System"""

class Student:
    def __init__(self, Roll_No, name, age, gpa):
        self.Roll_No = Roll_No
        self.name = name
        self.age = age
        self.gpa = gpa

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old. i got {self.gpa} gpa in my clg")

    def is_topper(self):
        if self.gpa >= 9.0:
            print(f"{self.name} is a topper student.")
        else:
            print(f"{self.name} is not a topper student.")

    def __str__(self):
        return f" Student: (Roll_No= {self.Roll_No}, name={self.name}, age={self.age}, gpa={self.gpa})"

student1 = Student(132,"Punj", 20, 9.4)
student2 = Student(133,"Raghav", 21, 8.7)

student1.gpa = 9.8
student1.introduce()
student1.is_topper()
student2.introduce()
student2.is_topper()
print(student1)
