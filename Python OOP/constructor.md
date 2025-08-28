
---

# 🐍 Constructor in Python — বিস্তারিত

---

## 🔹 Constructor কী?

* **Constructor** হলো একটি বিশেষ method যা কোনো **object তৈরি হওয়ার সময় স্বয়ংক্রিয়ভাবে কল হয়**।
* Python-এ constructor হলো `__init__()` method।
* এর কাজ হলো object initialize করা (অর্থাৎ object বানানোর সময় ভেতরের data/variable গুলোকে মান দেওয়া)।

---

## 🔹 Constructor Syntax

```python
class ClassName:
    def __init__(self, parameters):
        # initialize object
        self.attribute = parameters
```

---

## 📝 Example 1: Basic Constructor

```python
class Student:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

s1 = Student("Rahim", 20)
s2 = Student("Karim", 22)

print(s1.name, s1.age)  # Rahim 20
print(s2.name, s2.age)  # Karim 22
```

👉 এখানে `__init__()` constructor object বানানোর সাথে সাথেই name ও age initialize করেছে।

---

## 🔹 Constructor এর বৈশিষ্ট্য

1. নাম সবসময় `__init__` হয়।
2. Object বানানোর সময় স্বয়ংক্রিয়ভাবে কল হয়।
3. প্রথম parameter সবসময় `self` → object কে বোঝায়।
4. constructor এর মাধ্যমে **instance attribute set করা হয়**।

---

## 📝 Example 2: Default Constructor (no args)

```python
class Demo:
    def __init__(self):   # default constructor
        print("Object Created!")

d1 = Demo()   # Object বানালেই __init__() কল হবে
```

---

## 📝 Example 3: Parameterized Constructor

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("Toyota", "Corolla")
c2 = Car("Tesla", "Model 3")

print(c1.brand, c1.model)  # Toyota Corolla
print(c2.brand, c2.model)  # Tesla Model 3
```

👉 এখানে constructor parameters নিয়েছে object attributes initialize করার জন্য।

---

## 📝 Example 4: Default Parameter সহ Constructor

```python
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

s1 = Student("Rahim")
s2 = Student("Karim", 22)

print(s1.name, s1.age)  # Rahim 18
print(s2.name, s2.age)  # Karim 22
```

👉 যদি age না দেওয়া হয়, তাহলে default মান `18` ধরা হবে।

---

## 📝 Example 5: Multiple Objects

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Hasan", 20000)
e2 = Employee("Rakib", 30000)

print(e1.name, e1.salary)   # Hasan 20000
print(e2.name, e2.salary)   # Rakib 30000
```

---

## 🔹 Special Constructors

Python এ constructor ছাড়াও কিছু বিশেষ method আছে যেগুলো object lifecycle এর সাথে জড়িত:

### 1. **`__init__` (Constructor)**

Object তৈরি হলে initialize হয়।

### 2. **`__del__` (Destructor)**

Object destroy হলে কল হয়।

```python
class Test:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")

t = Test()
del t
```

---

## 🔹 Constructor বনাম Normal Method

| বৈশিষ্ট্য    | Constructor (`__init__`)             | Normal Method                |
| ------------ | ------------------------------------ | ---------------------------- |
| কল হওয়ার সময় | Object তৈরি হওয়ার সময় স্বয়ংক্রিয়ভাবে | যখন manually কল করা হয়       |
| উদ্দেশ্য     | Object initialize করা                | Object এর কাজ করা            |
| Return       | কিছু return করে না                   | যেকোনো কিছু return করতে পারে |

---

# ✅ সারসংক্ষেপ

* **Constructor (`__init__`)** → object তৈরি হলে স্বয়ংক্রিয়ভাবে চালু হয়।
* **Parameterized Constructor** → object এর attribute initialize করতে সাহায্য করে।
* **Default Constructor** → কোনো parameter ছাড়াই কাজ করে।
* **Destructor (`__del__`)** → object destroy হলে চালু হয়।
* Constructor object-এর শুরু আর end lifecycle manage করতে সাহায্য করে।

---

