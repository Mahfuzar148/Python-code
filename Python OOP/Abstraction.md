
---

# 🐍 Abstraction in Python — বিস্তারিত

---

## 🔹 Abstraction কী?

👉 **Abstraction** মানে হলো —
**অপ্রয়োজনীয় জিনিস লুকিয়ে রেখে শুধু প্রয়োজনীয় অংশ ব্যবহার করা।**

* User শুধু **কাজটা কীভাবে করতে হবে সেটা জানে না**, শুধু জানে কাজটা *করতে হবে*।
* জটিল implemention (backend logic) → লুকানো থাকে।
* শুধু interface / outer view → user এর সামনে থাকে।

📌 উদাহরণ:

* তুমি যখন `car.start()` চাপো → ভেতরে engine কীভাবে start হচ্ছে সেটা জানো না।
* তুমি যখন `len([1,2,3])` কল করো → Python ভেতরে কিভাবে length বের করছে সেটা জানো না।

---

## 🔹 Python এ Abstraction কিভাবে করা হয়?

Python এ abstraction করা যায় —

1. **Abstract Base Class (ABC module)**
2. **Abstract Methods (@abstractmethod decorator)**

---

## 📝 Example 1: Abstract Class & Abstract Method

```python
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):      # Abstract method
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Subclass must implement methods
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
```

👉 এখানে `Shape` হলো abstract class → এর methods implement না করলে object বানানো যাবে না।

---

## 📝 Example 2: Multiple Abstract Methods

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    
    def stop(self):
        print("Bike stopped")

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
    v.stop()
```

👉 Output:

```
Car started
Car stopped
Bike started
Bike stopped
```

---

## 📝 Example 3: Abstract Class with Constructor

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        return 50000

class Manager(Employee):
    def salary(self):
        return 80000

e1 = Developer("Rahim")
e2 = Manager("Karim")

print(e1.name, e1.salary())   # Rahim 50000
print(e2.name, e2.salary())   # Karim 80000
```

---

## 📝 Example 4: Real-life Payment System

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in Cash")

def process_payment(payment, amount):
    payment.pay(amount)

process_payment(CardPayment(), 500)
process_payment(CashPayment(), 1000)
```

👉 এখানে **Payment** হলো abstract class, আর CardPayment/CashPayment implement করেছে।

---

## 🔹 Abstraction এর সুবিধা

1. **Implementation hide করে** → user শুধু interface জানে।
2. **Security বাড়ে** → sensitive logic লুকানো যায়।
3. **Polymorphism এ কাজে লাগে** → একই interface, ভিন্ন behavior।
4. **Code Maintainability** → বড় project এ structure ভালো থাকে।

---

## 🔹 Abstraction বনাম Encapsulation

| বিষয়     | Abstraction              | Encapsulation                 |
| -------- | ------------------------ | ----------------------------- |
| কাজ      | জটিল logic লুকানো        | Data কে সুরক্ষিত রাখা         |
| Focus    | “কী করা হবে”             | “কীভাবে data protect হবে”     |
| Python এ | Abstract class / methods | Private, protected attributes |

---

# ✅ সারসংক্ষেপ

* **Abstraction** → জটিল implementation লুকিয়ে শুধু interface expose করা।
* Python এ **ABC (Abstract Base Class)** + `@abstractmethod` দিয়ে করা হয়।
* Child class অবশ্যই abstract methods implement করবে, নাহলে object বানানো যাবে না।
* Real-life Example → Shape, Vehicle, Payment system ইত্যাদি।

---

