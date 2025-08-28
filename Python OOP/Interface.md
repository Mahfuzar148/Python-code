
---

# 🐍 Interface in Python — বিস্তারিত

---

## 🔹 Interface কী?

👉 **Interface হলো একটা contract (চুক্তি)** — যেটা বলে দেয় কোনো class যদি এই Interface implement করে, তবে তাকে নির্দিষ্ট কিছু method অবশ্যই লিখতে হবে।

* Interface এ শুধু method এর নাম/ঘোষণা থাকে → কোনো implementation থাকে না।
* Implementation কাজটা করবে subclass।
* Abstraction এর মতোই, তবে interface ১০০% abstract (শুধু rules)।

📌 উদাহরণ:

* `Shape` interface → সব shape class কে `area()` আর `perimeter()` method implement করতেই হবে।
* তুমি `Circle`, `Square`, `Rectangle` যাই বানাও → এই দুই method থাকতেই হবে।

---

## 🔹 Python এ Interface কিভাবে করা হয়?

Python এ Java/C++ এর মতো আলাদা keyword নেই (`interface`)।
তবে আমরা **Abstract Base Class (ABC module)** ব্যবহার করে Interface বানাতে পারি।

---

## 📝 Example 1: Basic Interface

```python
from abc import ABC, abstractmethod

# Interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Implementing classes
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side

# Usage
shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.__class__.__name__, "Area:", s.area(), "Perimeter:", s.perimeter())
```

👉 Output:

```
Circle Area: 78.5 Perimeter: 31.4
Square Area: 16 Perimeter: 16
```

🔹 এখানে `Shape` হলো interface → `Circle` ও `Square` কে বাধ্যতামূলকভাবে `area()` ও `perimeter()` লিখতে হয়েছে।

---

## 📝 Example 2: Multiple Interfaces

👉 Python এ multiple inheritance এর মাধ্যমে এক class একাধিক interface implement করতে পারে।

```python
from abc import ABC, abstractmethod

class Readable(ABC):
    @abstractmethod
    def read(self):
        pass

class Writable(ABC):
    @abstractmethod
    def write(self, data):
        pass

class File(Readable, Writable):
    def read(self):
        print("Reading file content")
    
    def write(self, data):
        print("Writing data:", data)

f = File()
f.read()
f.write("Hello Python")
```

👉 Output:

```
Reading file content
Writing data: Hello Python
```

🔹 এখানে `File` একসাথে **Readable** আর **Writable** দুইটা interface implement করেছে।

---

## 📝 Example 3: Payment System (Real-world Interface)

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

def process_payment(payment: Payment, amount):
    payment.pay(amount)

process_payment(CardPayment(), 500)
process_payment(CashPayment(), 1000)
```

👉 Output:

```
Paid 500 using Card
Paid 1000 in Cash
```

🔹 এখানে **Payment** হলো interface → সব payment class কে `pay()` method implement করতেই হবে।

---

## 🔹 Interface এর বৈশিষ্ট্য

1. শুধুমাত্র method এর নাম থাকে, implementation থাকে না।
2. যেই class interface implement করবে, তাকে সব method লিখতেই হবে।
3. Loose coupling করে (client শুধু interface জানে, implementation জানে না)।
4. Multiple interface একসাথে implement করা যায়।

---

## 🔹 Interface বনাম Abstract Class

| বিষয়     | Interface                      | Abstract Class                               |
| -------- | ------------------------------ | -------------------------------------------- |
| উদ্দেশ্য | Contract define করা (rules)    | Partial abstraction + default implementation |
| Method   | সব method abstract             | কিছু method abstract, কিছু implemented       |
| Variable | সাধারণত constant থাকে          | Instance variable থাকতে পারে                 |
| Python এ | ABC class + সব method abstract | ABC class + কিছু method implemented          |

---

## ✅ সারসংক্ষেপ

* **Interface** = Contract → নির্দিষ্ট কিছু method implement করতে হবে।
* Python এ interface করা যায় **ABC (Abstract Base Class)** দিয়ে।
* বাস্তব ব্যবহার: Shape, Payment, File Handling ইত্যাদি।
* সুবিধা: Code flexible হয়, Polymorphism সহজ হয়, নতুন class যোগ করা সহজ হয়।

---
