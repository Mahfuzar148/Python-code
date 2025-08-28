
---

# 🐍 Dynamic Binding in Python — বিস্তারিত

---

## 🔹 Binding কী?

**Binding** মানে হলো কোনো **function call** বা **method call** কে আসল implementation এর সাথে "bind" বা "লিঙ্ক" করে দেওয়া।

👉 দুই ধরনের binding হয়:

1. **Static Binding (Early Binding)** → Compile time এ method resolve হয়ে যায় (Java/C++ এ দেখা যায় বেশি)
2. **Dynamic Binding (Late Binding)** → Runtime এ কোন method কল হবে সেটা resolve হয় (Python, Java, etc এ OOP এর সুবিধা)

---

## 🔹 Dynamic Binding কী?

👉 Dynamic Binding মানে হলো: **কোন method কল হবে সেটা runtime এ ঠিক হবে, object এর type অনুযায়ী।**

* Parent reference → Child object → Child এর method execute হবে।
* এটাকে Python এ খুব সহজে করা যায়, কারণ Python পুরোপুরি **dynamically typed language**।

---

## 📝 Example 1: Basic Dynamic Binding

```python
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Dynamic binding in action
animals = [Animal(), Dog(), Cat()]
for a in animals:
    a.speak()
```

👉 Output:

```
Animal makes sound
Dog barks
Cat meows
```

🔹 এখানে loop এর ভেতরে একই `speak()` method কল করা হচ্ছে, কিন্তু runtime এ object এর type দেখে ভিন্ন method execute হচ্ছে। এটিই **Dynamic Binding**।

---

## 📝 Example 2: Constructor সহ Dynamic Binding

```python
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car engine started")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

def run_vehicle(v):
    v.start()   # dynamic binding

run_vehicle(Car())   # Car engine started
run_vehicle(Bike())  # Bike engine started
```

👉 Function `run_vehicle()` শুধু `start()` কল করছে, কিন্তু কোন version রান হবে সেটা runtime এ ঠিক হচ্ছে।

---

## 📝 Example 3: Real-life Payment System

```python
class Payment:
    def pay(self, amount):
        print("Generic Payment of", amount)

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")

class CashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Cash")

def process_payment(payment, amount):
    payment.pay(amount)   # dynamic binding

process_payment(CardPayment(), 500)
process_payment(CashPayment(), 1000)
```

👉 Output:

```
Paid 500 using Card
Paid 1000 using Cash
```

🔹 একি `pay()` method → object type ভেদে runtime এ behavior আলাদা হচ্ছে।

---

## 🔹 কেন দরকার Dynamic Binding?

1. **Polymorphism** implement করতে
2. **Code flexibility** – client code কে না বদলিয়েই নতুন behavior add করা যায়
3. **Loose Coupling** – parent এর মাধ্যমে child কে handle করা যায়
4. **Reusability** – একই function অনেক class এর object এর সাথে কাজ করতে পারে

---

## 🔹 Static বনাম Dynamic Binding তুলনা

| বিষয়        | Static Binding            | Dynamic Binding                     |
| ----------- | ------------------------- | ----------------------------------- |
| সময়         | Compile time এ resolve হয় | Runtime এ resolve হয়                |
| Flexibility | কম                        | বেশি                                |
| Python এ    | নেই (কারণ Python dynamic) | সব method call runtime এ resolve হয় |
| Example     | Java এর `final` method    | Python এর method overriding         |

---

# ✅ সারসংক্ষেপ

* **Dynamic Binding** মানে হলো method call এর সাথে কোন implementation যুক্ত হবে সেটা runtime এ ঠিক হয়।
* Python এ সব method call ডিফল্টভাবে **Dynamic Binding** হয়, এজন্য Polymorphism খুব সহজে কাজ করে।
* উদাহরণ: Parent reference → Child object → Child এর method execute হবে।

---

