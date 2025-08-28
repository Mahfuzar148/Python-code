
---

# 🐍 Inheritance in Python — বিস্তারিত

---

## 🔹 Inheritance কী?

👉 Inheritance মানে হলো **একটা class অন্য একটা class-এর বৈশিষ্ট্য (attributes + methods) উত্তরাধিকার হিসেবে পাওয়া**।
👉 Parent/Base/Super Class → যেখান থেকে বৈশিষ্ট্য পাওয়া হয়।
👉 Child/Derived/Sub Class → যে ক্লাস parent class থেকে উত্তরাধিকার পায়।

📌 কেন দরকার?

* কোড পুনঃব্যবহার (reusability)
* কোড কম লেখা (DRY principle)
* Maintain করা সহজ

---

## 🔹 Inheritance Syntax

```python
class Parent:
    # parent class code

class Child(Parent):
    # child class code
```

---

## 1️⃣ Single Inheritance

```python
class Animal:      # Parent
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal): # Child
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Dog barks
```

👉 `Dog` ক্লাস `Animal` থেকে method পেয়েছে, আবার নিজের মতো override করেছে।

---

## 2️⃣ Multilevel Inheritance

```python
class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Animal(LivingBeing):
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

d = Dog()
d.breathe()   # Breathing... (LivingBeing থেকে)
d.eat()       # Eating... (Animal থেকে)
d.bark()      # Barking... (নিজের)
```

👉 এখানে `Dog` → `Animal` → `LivingBeing` তিন স্তরে inheritance হয়েছে।

---

## 3️⃣ Multiple Inheritance

👉 Python এ একটি child class একাধিক parent class থেকেও inherit করতে পারে।

```python
class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, Sewing")

class Child(Father, Mother):
    def skills(self):
        print("Child has: ")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()
```

Output:

```
Child has: 
Gardening, Driving
Cooking, Sewing
```

👉 একাধিক parent এর বৈশিষ্ট্য পাওয়া যাচ্ছে।

---

## 4️⃣ Hierarchical Inheritance

👉 এক parent class → একাধিক child class।

```python
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

c = Car()
b = Bike()

c.info(); c.wheels()
b.info(); b.wheels()
```

---

## 5️⃣ Hybrid Inheritance

👉 একাধিক inheritance স্টাইল একসাথে (multiple + multilevel)।

```python
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):   # Hybrid
    def showD(self):
        print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()
```

---

## 6️⃣ Method Overriding

👉 Child class নিজের মতো করে parent class-এর method define করতে পারে।

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):   # overriding
        print("Cat meows")

c = Cat()
c.speak()   # Cat meows
```

---

## 7️⃣ `super()` Function

👉 Child class থেকে parent class-এর constructor বা method কল করার জন্য `super()` ব্যবহার হয়।

```python
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # parent constructor কল করা হলো
        self.roll = roll

    def show(self):
        super().show()   # parent method কল
        print("Roll:", self.roll)

s = Student("Rahim", 101)
s.show()
```

Output:

```
Name: Rahim
Roll: 101
```

---

## 🔹 Inheritance এর ধরন (Python এ)

| ধরন              | ব্যাখ্যা                        | উদাহরণ                     |
| ---------------- | ------------------------------- | -------------------------- |
| **Single**       | এক parent → এক child            | Animal → Dog               |
| **Multilevel**   | এক parent → child → grandchild  | LivingBeing → Animal → Dog |
| **Multiple**     | এক child → একাধিক parent        | Father, Mother → Child     |
| **Hierarchical** | এক parent → একাধিক child        | Vehicle → Car, Bike        |
| **Hybrid**       | একাধিক inheritance style একসাথে | A → B, C → D               |

---

# ✅ সারসংক্ষেপ

* Inheritance = একটি class অন্য class থেকে বৈশিষ্ট্য পায়।
* কোড পুনঃব্যবহার সহজ হয়।
* Python এ Inheritance এর ধরন: **Single, Multilevel, Multiple, Hierarchical, Hybrid**।
* Child class parent method override করতে পারে।
* `super()` ব্যবহার করে parent এর constructor/method কল করা যায়।

---

