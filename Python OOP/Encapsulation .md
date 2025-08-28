
---

# 🐍 Encapsulation in Python — বিস্তারিত

---

## 🔹 Encapsulation কী? (Basic Idea)

👉 **Encapsulation** শব্দের অর্থ হলো **কোনো কিছু একটি capsule এর মধ্যে ঢুকিয়ে রাখা**।
OOP এ **Encapsulation মানে হলো Data (attributes) + Methods (functions) কে একসাথে একটি class এর ভেতরে রাখা এবং বাইরের access নিয়ন্ত্রণ করা**।

📌 সহজভাবে:

* **Encapsulation = Data Hiding + Data Protection + Controlled Access**
* মানে object এর ভেতরে ডেটা private/protected করে রাখা হয় → direct access করা যায় না।
* Access করতে হলে অবশ্যই method (getter/setter) ব্যবহার করতে হবে।

---

## 🔹 Encapsulation এর উদ্দেশ্য

1. Data লুকানো (Data Hiding)
2. Data কে অবৈধভাবে পরিবর্তন থেকে রক্ষা করা (Protection)
3. Controlled Access (getter & setter এর মাধ্যমে নির্দিষ্টভাবে access দেওয়া)
4. Maintainability বাড়ানো

---

## 🔹 Python এ Access Modifiers দিয়ে Encapsulation

Python এ Encapsulation করার জন্য **Access Modifiers** ব্যবহার হয়:

* **Public** → সবার জন্য উন্মুক্ত
* **Protected (`_var`)** → subclass এ access হয়, বাইরে convention অনুযায়ী avoid
* **Private (`__var`)** → class এর বাইরে থেকে সরাসরি access করা যায় না

---

## 📝 Example 1: Basic Encapsulation

```python
class Student:
    def __init__(self, name, roll):
        self.__name = name     # private
        self.__roll = roll     # private
    
    # getter (accessor)
    def get_name(self):
        return self.__name
    
    # setter (mutator)
    def set_name(self, new_name):
        if len(new_name) > 0:
            self.__name = new_name
        else:
            print("Invalid name")

s = Student("Rahim", 101)

# Direct access ❌
# print(s.__name)    # AttributeError

# Controlled access ✅
print(s.get_name())   # Rahim
s.set_name("Karim")
print(s.get_name())   # Karim
```

👉 এখানে `__name` private → বাইরে থেকে সরাসরি access করা যাবে না, শুধু getter/setter দিয়ে হবে।

---

## 📝 Example 2: Bank Account (Real-life Encapsulation)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private
    
    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, New Balance = {self.__balance}")
        else:
            print("Invalid deposit")
    
    # withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}, New Balance = {self.__balance}")
        else:
            print("Insufficient balance")
    
    # getter
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)     # Deposited 500, New Balance = 1500
acc.withdraw(200)    # Withdraw 200, New Balance = 1300
print(acc.get_balance())  # 1300
```

👉 এখানে balance ডেটা hidden আছে। user চাইলে সরাসরি balance পরিবর্তন করতে পারবে না, শুধু deposit/withdraw এর মাধ্যমে পারবে।

---

## 📝 Example 3: Property Decorator দিয়ে Encapsulation

Python এ Encapsulation করার modern উপায় হলো `@property` decorator → getter & setter কে সহজ করা।

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    
    @property
    def salary(self):      # getter
        return self.__salary
    
    @salary.setter
    def salary(self, amount):   # setter
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

e = Employee(20000)
print(e.salary)     # getter call → 20000
e.salary = 25000    # setter call
print(e.salary)     # 25000
e.salary = -100     # Invalid salary
```

---

## 🔹 Encapsulation বনাম Abstraction

| বিষয়     | Encapsulation                                          | Abstraction                                  |
| -------- | ------------------------------------------------------ | -------------------------------------------- |
| কাজ      | Data + Method কে একসাথে বেঁধে রাখা, access control করা | Implementation লুকানো, শুধু interface দেখানো |
| Focus    | Data Protection                                        | Implementation Hiding                        |
| Python এ | Private, Protected attributes + Getter/Setter          | Abstract Class + Abstract Method             |

---

## ✅ সারসংক্ষেপ

* **Encapsulation** = Class এর ভেতরে Data + Method রাখা + বাইরের access control করা।
* Python এ করা যায় → `public`, `protected (_var)`, `private (__var)` attributes দিয়ে।
* Controlled Access এর জন্য **Getter & Setter** ব্যবহার হয়।
* সুবিধা → Data security, code maintainability, ভুল কম হয়।

---

