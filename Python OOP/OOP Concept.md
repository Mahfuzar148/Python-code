
---

# 🐍 Python OOP (অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং)

Python-এ **OOP** এমন এক programming approach যেখানে কোডকে **object** আর **class** দিয়ে সাজানো হয়।
Object হলো বাস্তব জীবনের কোনো entity (যেমন: ছাত্র, গাড়ি, ব্যাংক অ্যাকাউন্ট), আর Class হলো তার **blueprint** বা **design**।

---

## 🔹 OOP এর চারটি মূল স্তম্ভ (4 Pillars of OOP)

1. **Encapsulation (সংবদ্ধকরণ)**
2. **Inheritance (উত্তরাধিকার)**
3. **Polymorphism (বহুরুপিতা)**
4. **Abstraction (পর্দার আড়াল)**

---

## 1️⃣ Class এবং Object

* **Class** → নকশা/Blueprint যেখানে attributes (data) ও methods (behavior) লেখা থাকে।
* **Object** → সেই নকশা থেকে বানানো বাস্তব entity।

```python
class Student:       # Class
    def __init__(self, name, age):   # Constructor
        self.name = name
        self.age = age

    def show(self):   # Method
        print(f"Name: {self.name}, Age: {self.age}")

# Object তৈরি
s1 = Student("Rahim", 21)
s1.show()
```

🟢 এখানে `Student` হলো class আর `s1` হলো object।

---

## 2️⃣ Encapsulation (সংবদ্ধকরণ)

👉 ডেটা ও তার উপর কাজ করা মেথডগুলোকে একসাথে একটি ক্লাসে রাখা।
👉 private variable ব্যবহার করে বাইরের থেকে direct access বন্ধ করা হয়।

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

🟢 `__balance` কে বাইরে থেকে access করা যাবে না → encapsulation।

---

## 3️⃣ Inheritance (উত্তরাধিকার)

👉 একটি class অন্য class এর বৈশিষ্ট্য/মেথড পায়।
👉 কোড পুনঃব্যবহার (reusability) সহজ হয়।

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # Inherits Animal
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

Dog().speak()  # Dog barks
Cat().speak()  # Cat meows
```

🟢 `Dog` এবং `Cat` → `Animal` থেকে উত্তরাধিকার পেয়ে তাদের নিজস্ব behavior দিয়েছে।

---

## 4️⃣ Polymorphism (বহুরুপিতা)

👉 একই নামের method ভিন্ন ভিন্ন ক্লাসে আলাদা আলাদা কাজ করে।

```python
animals = [Dog(), Cat()]
for a in animals:
    a.speak()
```

🟢 Output:

```
Dog barks
Cat meows
```

---

## 5️⃣ Abstraction (পর্দার আড়াল)

👉 ভেতরের জটিলতা লুকিয়ে শুধু দরকারি অংশ দেখা।
👉 Python-এ `abc` (Abstract Base Class) module ব্যবহার করে করা যায়।

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

c = Circle(5)
print(c.area())  # 78.5
```

🟢 এখানে `Shape` হলো abstract class, যেটা সরাসরি object বানাতে পারি না।

---

## 6️⃣ Special (Magic/Dunder) Methods

👉 Python এ **`__init__`, `__str__`, `__len__`** ইত্যাদি special methods আছে যেগুলো object এর default behavior override করতে পারে।

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
print(b)        # Python Basics (250 pages)
print(len(b))   # 250
```

---

## 7️⃣ Class vs Instance vs Static Method

* **Instance Method** → object এর জন্য কাজ করে।
* **Class Method** → class লেভেলের data নিয়ে কাজ করে (`@classmethod`)।
* **Static Method** → independent utility function (`@staticmethod`)।

```python
class MathOps:
    def __init__(self, x):
        self.x = x

    def square(self):        # Instance method
        return self.x * self.x

    @classmethod
    def cube(cls, num):      # Class method
        return num ** 3

    @staticmethod
    def add(a, b):           # Static method
        return a + b

m = MathOps(5)
print(m.square())        # 25
print(MathOps.cube(3))   # 27
print(MathOps.add(4, 6)) # 10
```

---

# ✅ সারসংক্ষেপ

Python OOP এর মূল ধারণাগুলো হলো:

* **Class & Object** → নকশা ও বাস্তব রূপ
* **Encapsulation** → ডেটা লুকিয়ে রাখা
* **Inheritance** → কোড পুনঃব্যবহার
* **Polymorphism** → একই method, ভিন্ন আচরণ
* **Abstraction** → জটিলতা লুকানো
* **Special Methods** → Pythonic way object customize করা
* **Class/Static Methods** → ভিন্ন scope এর utility

---


