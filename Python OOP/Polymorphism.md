
---

# 🐍 Polymorphism in Python — বিস্তারিত

---

## 🔹 Polymorphism কী?

**Polymorphism** শব্দটা এসেছে গ্রিক থেকে — *poly* (অনেক) + *morph* (রূপ)।
👉 অর্থাৎ **একই জিনিস বিভিন্ন রূপে ব্যবহার হওয়া**।

📌 সহজভাবে:
একই method নাম → ভিন্ন ভিন্ন class এ → আলাদা আচরণ করবে।

---

## 🔹 Polymorphism এর ধরন

Python এ polymorphism কয়েকভাবে কাজ করে:

1. **Method Polymorphism (Overriding)**
2. **Function Polymorphism (Duck Typing)**
3. **Operator Overloading**
4. **Method Overloading (Pythonically)**

---

## 1️⃣ Method Overriding (Subclass এ method নতুনভাবে লেখা)

```python
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):   # overriding
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()
```

👉 Output:

```
Dog barks
Cat meows
Animal makes sound
```

---

## 2️⃣ Function Polymorphism (Duck Typing)

👉 Python এ কোনো object কে তার **behavior (method)** এর ভিত্তিতে ব্যবহার করা হয়, তার class এর ভিত্তিতে নয়।

```python
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane flies in the sky")

class Fish:
    def swim(self):
        print("Fish swims in water")

def make_it_fly(thing):
    thing.fly()

make_it_fly(Bird())      # Bird can fly
make_it_fly(Airplane())  # Airplane flies in the sky
# make_it_fly(Fish())    # ❌ Error (কারণ swim আছে, fly নেই)
```

👉 একি function → বিভিন্ন object → আলাদা আচরণ।
এটাকেই বলে **Duck Typing** → "If it looks like a duck, swims like a duck, and quacks like a duck → it’s a duck!"

---

## 3️⃣ Operator Overloading (Polymorphism in Operators)

👉 Python এ operator গুলো আসলে method। এগুলোকে override করলে operator গুলো ভিন্নভাবে behave করতে পারে।

```python
class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):     # + operator overload
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)   # 300 (operator overloaded)
```

---

## 4️⃣ Method Overloading (Pythonically)

👉 Python এ **same name method** একাধিক বার define করলে শেষেরটা কাজ করে।
👉 কিন্তু আমরা default argument দিয়ে method overloading-এর মতো behavior বানাতে পারি।

```python
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))       # 15
print(calc.add(2, 3, 4))     # 9
print(calc.add())            # 0
```

👉 এখানে `add()` method একবারই লেখা হয়েছে, কিন্তু arguments ভেদে আলাদা কাজ করছে।

---

## 🔹 Polymorphism with Abstract Class

👉 Abstract class ব্যবহার করলে নিশ্চিত হওয়া যায় যে child class গুলো নির্দিষ্ট method অবশ্যই implement করবে।

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

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.area())
```

👉 Output:

```
78.5
16
```

---

## 🔹 Polymorphism এর Summary Table

| ধরন                      | ব্যাখ্যা                                      | Example                        |
| ------------------------ | --------------------------------------------- | ------------------------------ |
| **Method Overriding**    | Subclass এ method redefine                    | `Dog.speak()` vs `Cat.speak()` |
| **Duck Typing**          | Behavior অনুযায়ী কাজ                          | `make_it_fly(Bird)`            |
| **Operator Overloading** | Operator কে customize করা                     | `__add__`, `__sub__`           |
| **Method Overloading**   | Default arguments দিয়ে এক method এ একাধিক কাজ | `add(a,b,c=0)`                 |

---

# ✅ সারসংক্ষেপ

* **Polymorphism** = একই নাম → বিভিন্ন রূপ
* Python এ Polymorphism হয়:

  1. Method Overriding
  2. Duck Typing
  3. Operator Overloading
  4. Method Overloading (default arguments দিয়ে)
* এটার মূল সুবিধা হলো → **একই code দিয়ে ভিন্ন ভিন্ন object কে handle করা যায়।**

---

