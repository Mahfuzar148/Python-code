
---

# 🐍 Python Class এবং Object — বিস্তারিত

---

## 🔹 Class কী?

👉 Class হলো একটা **blueprint** বা **নকশা**।
এর ভেতরে আমরা attributes (ডেটা/ভ্যারিয়েবল) আর methods (function) ডিফাইন করি।

## 🔹 Object কী?

👉 Object হলো **class এর instance**।
একটা class থেকে আমরা অনেকগুলো object বানাতে পারি, যেগুলোর আলাদা আলাদা ডেটা থাকে কিন্তু একই blueprint ব্যবহার করে।

---

## 📝 Simple Class এবং Object Example

```python
class Student:
    # constructor (__init__) -> object বানানোর সময় initialize করে
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method (object এর কাজ)
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

# object তৈরি
s1 = Student("Rahim", 20)
s2 = Student("Karim", 22)

s1.introduce()   # My name is Rahim, I am 20 years old.
s2.introduce()   # My name is Karim, I am 22 years old.
```

---

## 🔹 Multiple Objects from Same Class

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show(self):
        print(f"{self.brand} {self.model}")

c1 = Car("Toyota", "Corolla")
c2 = Car("Tesla", "Model 3")

c1.show()   # Toyota Corolla
c2.show()   # Tesla Model 3
```

---

## 🔹 Adding Methods (behavior)

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New balance = {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}, Remaining balance = {self.balance}")
        else:
            print("Insufficient funds!")

# Object ব্যবহার
acc1 = BankAccount("Rahim", 1000)
acc1.deposit(500)      # Deposited 500, New balance = 1500
acc1.withdraw(700)     # Withdrew 700, Remaining balance = 800
```

---

## 🔹 Object Attributes Dynamically Add করা

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Hasan")
p1.age = 25    # object এর বাইরে থেকে নতুন attribute add করা হলো
print(p1.name, p1.age)   # Hasan 25
```

---

## 🔹 Class Variable বনাম Instance Variable

```python
class Employee:
    company = "ABC Ltd"    # class variable (সব object এর জন্য একই)

    def __init__(self, name, salary):
        self.name = name        # instance variable
        self.salary = salary    # instance variable

e1 = Employee("Rahim", 20000)
e2 = Employee("Karim", 25000)

print(e1.company, e1.name, e1.salary)  # ABC Ltd Rahim 20000
print(e2.company, e2.name, e2.salary)  # ABC Ltd Karim 25000

# class variable update করলে সব object এ প্রভাব পড়ে
Employee.company = "XYZ Ltd"
print(e1.company)  # XYZ Ltd
print(e2.company)  # XYZ Ltd
```

---

## 🔹 Methods এর ধরন

1. **Instance Method** → object এর data নিয়ে কাজ করে
2. **Class Method** → পুরো class এর data নিয়ে কাজ করে
3. **Static Method** → helper function, class/object data দরকার নেই

```python
class MathOps:
    def __init__(self, x):
        self.x = x

    def square(self):          # Instance method
        return self.x * self.x

    @classmethod
    def info(cls):             # Class method
        print("This is MathOps class")

    @staticmethod
    def add(a, b):             # Static method
        return a + b

m = MathOps(5)
print(m.square())        # 25
MathOps.info()           # This is MathOps class
print(MathOps.add(4, 6)) # 10
```

---

## 🔹 Special (Magic) Methods সহ Example

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

# ✅ সারসংক্ষেপ

* **Class** → blueprint (attributes + methods)
* **Object** → class এর instance (বাস্তব entity)
* **Instance Variable** → আলাদা আলাদা object এর data
* **Class Variable** → সব object এর জন্য একই data
* **Methods** → instance method, class method, static method
* **Special Methods** → object এর behavior override করতে ব্যবহার হয়

---

