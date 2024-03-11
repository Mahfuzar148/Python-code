class Student:
    roll = ""
    gpa = ""

    def setValue(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll},gpa : {self.gpa}")


Rahim = Student()
Rahim.setValue(101, 3.70)
Rahim.display()

Karim = Student()
Karim.setValue(102, 3.75)
Karim.display()
