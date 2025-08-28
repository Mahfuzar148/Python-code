```markdown
---
# 🐍 Python Object-Oriented Programming (OOP)

This README provides a **complete overview of OOP in Python** with theory, code examples, and best practices.

---

## 📑 Table of Contents
1. [Introduction](#introduction)
2. [Key Concepts](#key-concepts)
3. [Class and Object](#class-and-object)
4. [Encapsulation](#encapsulation)
5. [Inheritance](#inheritance)
6. [Polymorphism](#polymorphism)
7. [Abstraction](#abstraction)
8. [Magic (Dunder) Methods](#magic-dunder-methods)
9. [Class vs Instance vs Static Methods](#class-vs-instance-vs-static-methods)
10. [Factory Example](#factory-example)
11. [Practice Questions](#practice-questions)
12. [Conclusion](#conclusion)

---

## 🔹 Introduction
**OOP (Object-Oriented Programming)** organizes code around **objects** and **classes**.  
Python fully supports OOP and makes programs more modular, reusable, and maintainable.

---

## 🔹 Key Concepts
- **Class** → Blueprint for objects  
- **Object** → Instance of a class  
- **Encapsulation** → Hiding data & providing controlled access  
- **Inheritance** → Reuse code from parent classes  
- **Polymorphism** → Same method name, different behavior  
- **Abstraction** → Hiding implementation details, exposing only essentials  

---

## 🔹 Class and Object
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Rahim", 21)
s1.show()
````

---

## 🔹 Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
```

---

## 🔹 Inheritance

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

Dog().speak()  # Dog barks
Cat().speak()  # Cat meows
```

---

## 🔹 Polymorphism

```python
animals = [Dog(), Cat()]
for a in animals:
    a.speak()
```

---

## 🔹 Abstraction

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

print(Circle(5).area())  # 78.5
```

---

## 🔹 Magic (Dunder) Methods

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

b = Book("Python Basics", 250)
print(b)       # Python Basics (250 pages)
print(len(b))  # 250
```

---

## 🔹 Class vs Instance vs Static Methods

```python
class MathOps:
    def __init__(self, x):
        self.x = x

    def square(self):          # Instance method
        return self.x * self.x

    @classmethod
    def cube(cls, num):        # Class method
        return num ** 3

    @staticmethod
    def add(a, b):             # Static method
        return a + b

m = MathOps(5)
print(m.square())        # 25
print(MathOps.cube(3))   # 27
print(MathOps.add(4, 6)) # 10
```

---

## 🔹 Factory Example

```python
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            return None

factory = ShapeFactory()
s1 = factory.get_shape("circle")
s1.draw()
```

---

## 📝 Practice Questions

1. Create a `Car` class with attributes and methods.
2. Implement single and multiple inheritance.
3. Use polymorphism with a `Bird` and `Fish` class.
4. Implement abstraction with `Payment` (CreditCard, PayPal).
5. Override `__str__` and `__len__` in a `Playlist` class.

---

## ✅ Conclusion

Python OOP follows the **four pillars**:

* **Encapsulation**
* **Inheritance**
* **Polymorphism**
* **Abstraction**

