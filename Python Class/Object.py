class Student :
    roll = ""
    gpa =""


Rahim = Student()
#check whether a variable is object or not of a particular class
print(isinstance(Rahim,Student))
Rahim.roll = 101
Rahim.gpa = 3.70
print(f"Roll : {Rahim.roll},gpa : {Rahim.gpa}")

Karim = Student()
Karim.roll = 102
Karim.gpa = 3.75
print(f"Roll : {Karim.roll},gpa : {Karim.gpa}")
