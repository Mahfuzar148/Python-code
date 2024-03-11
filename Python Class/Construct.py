class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa


    def display(self):
       print(f"Roll : {self.roll},gpa : {self.gpa}")


Rahim = Student(101, 3.70)
Rahim.display()

Karim = Student(102, 3.75)
Karim.display()
