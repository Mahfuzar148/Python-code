
---

# 🐍 Python Class Attributes — বিস্তারিত

---

## 🔹 Class Attribute কী?

* Class attribute হলো এমন ভ্যারিয়েবল যা **class-এর ভেতরে define করা হয়**, কিন্তু কোনো instance (object)-এর ভেতরে নয়।
* অর্থাৎ এটি **সব object এর জন্য শেয়ারড হয়**।
* একে আমরা `ClassName.attribute` বা `object.attribute` দুইভাবেই access করতে পারি।

---

## 📝 Example 1: Basic Class Attribute

```python
class Student:
    school = "ABC High School"   # class attribute

    def __init__(self, name, age):
        self.name = name         # instance attribute
        self.age = age

# Object তৈরি
s1 = Student("Rahim", 20)
s2 = Student("Karim", 22)

print(s1.school)   # ABC High School
print(s2.school)   # ABC High School

print(s1.name, s1.age)  # Rahim 20
print(s2.name, s2.age)  # Karim 22
```

👉 এখানে `school` হলো class attribute → সব object একই মান ব্যবহার করছে।
👉 কিন্তু `name` এবং `age` হলো instance attribute → আলাদা object এর আলাদা মান।

---

## 🔹 Instance Attribute বনাম Class Attribute

```python
class Employee:
    company = "XYZ Ltd"   # class attribute

    def __init__(self, name, salary):
        self.name = name        # instance attribute
        self.salary = salary    # instance attribute

e1 = Employee("Rahim", 20000)
e2 = Employee("Karim", 25000)

print(e1.company, e1.name, e1.salary)
# XYZ Ltd Rahim 20000

print(e2.company, e2.name, e2.salary)
# XYZ Ltd Karim 25000
```

---

## 🔹 Class Attribute Update করা

```python
print(Employee.company)  # XYZ Ltd
Employee.company = "ABC Ltd"   # class attribute আপডেট
print(Employee.company)  # ABC Ltd

# সব object এ প্রভাব পড়বে
print(e1.company)  # ABC Ltd
print(e2.company)  # ABC Ltd
```

👉 যদি class attribute update করা হয়, তাহলে সব object সেই নতুন মান পাবে।

---

## 🔹 Object দিয়ে Class Attribute Override করা

```python
e1.company = "My Company"   # নতুন instance attribute তৈরি হলো

print(e1.company)  # My Company   (instance attribute)
print(e2.company)  # ABC Ltd      (class attribute)
print(Employee.company)  # ABC Ltd
```

👉 যদি object এর মাধ্যমে class attribute পরিবর্তন করা হয়, তখন সেটা **শুধু ওই object এর জন্য নতুন instance attribute তৈরি করে**। মূল class attribute অপরিবর্তিত থাকে।

---

## 🔹 Example: Counter with Class Attribute

```python
class Counter:
    count = 0   # class attribute (সব object শেয়ার করবে)

    def __init__(self):
        Counter.count += 1   # প্রতিবার object তৈরি হলে বাড়বে

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)  # 3
```

👉 `Counter.count` প্রতিবার object তৈরি হলে বেড়ে যাচ্ছে।

---

## 🔹 Example: Store All Objects in Class Attribute

```python
class Student:
    all_students = []   # class attribute

    def __init__(self, name):
        self.name = name
        Student.all_students.append(self)

s1 = Student("Rahim")
s2 = Student("Karim")
s3 = Student("Hasan")

for stu in Student.all_students:
    print(stu.name)
```

👉 Output:

```
Rahim
Karim
Hasan
```

🟢 এখানে `all_students` class attribute সব object কে track করছে।

---

## 🔹 Class Attribute বনাম Instance Attribute Difference (Summary)

| বৈশিষ্ট্য   | Class Attribute                                    | Instance Attribute                  |
| ----------- | -------------------------------------------------- | ----------------------------------- |
| সংজ্ঞা      | ক্লাসের ভেতরে define করা (constructor এর বাইরে)    | `__init__()` বা method এ define করা |
| Scope       | সব object এর জন্য common                           | প্রতিটি object এর জন্য আলাদা        |
| Access      | `ClassName.attr` বা `obj.attr`                     | শুধু `obj.attr`                     |
| Update করলে | সব object প্রভাবিত হয় (যদি object override না করে) | শুধু নির্দিষ্ট object প্রভাবিত হয়   |

---

# ✅ সারসংক্ষেপ

* **Class Attribute** → সব object এর জন্য common value
* **Instance Attribute** → প্রতিটি object এর জন্য আলাদা value
* Object দিয়ে attribute assign করলে সেটা **override হয়ে যায়**
* Useful for → counters, shared data, caching, registry ইত্যাদি

---


---

# 🐍 Python Class Attributes এর ধরন

Python-এ মূলত ৪ ধরনের **class attributes**/variables ব্যবহৃত হয়:

1. **Public Attribute (সবার জন্য উন্মুক্ত)**
2. **Protected Attribute (আংশিক সুরক্ষিত)**
3. **Private Attribute (সম্পূর্ণ লুকানো)**
4. **Static Attribute (class level shared)**

---

## 1️⃣ Public Attribute

👉 Public attribute সবার জন্য উন্মুক্ত।
👉 যেকোনো জায়গা থেকে (class এর ভেতর বা বাইরে) access করা যায়।

```python
class Student:
    school = "ABC School"   # public class attribute
    
    def __init__(self, name):
        self.name = name    # public instance attribute

s1 = Student("Rahim")
print(s1.name)      # Rahim
print(Student.school) # ABC School
```

✅ Public attribute = normal variable (default by design)।

---

## 2️⃣ Protected Attribute (`_single_underscore`)

👉 Python এ **protected attribute** বোঝাতে নামের শুরুতে `_` (single underscore) ব্যবহার করা হয়।
👉 Convention: এগুলোকে **class বা subclass এর ভেতরে ব্যবহার করাই উচিত**।
👉 বাইরে থেকে access technically possible, কিন্তু **প্রোগ্রামারের জন্য সতর্ক সংকেত**।

```python
class Employee:
    _company_name = "XYZ Ltd"   # protected class attribute
    
    def __init__(self, name, salary):
        self._salary = salary   # protected instance attribute
        self.name = name

e1 = Employee("Karim", 25000)
print(e1._salary)   # ⚠️ যদিও পাওয়া যাচ্ছে, কিন্তু convention অনুযায়ী বাইরে থেকে ব্যবহার না করাই ভালো
```

✅ Protected → subclass এ ব্যবহার safe, বাইরে থেকে avoid করতে হবে।

---

## 3️⃣ Private Attribute (`__double_underscore`)

👉 Python এ private attribute declare করতে `__` (double underscore) ব্যবহার করা হয়।
👉 এগুলো **name mangling** এর মাধ্যমে ক্লাসের বাইরে থেকে direct access করা যায় না।

```python
class BankAccount:
    __bank_name = "BD Bank"   # private class attribute
    
    def __init__(self, balance):
        self.__balance = balance   # private instance attribute

    def get_balance(self):   # accessor method
        return self.__balance

acc = BankAccount(5000)
print(acc.get_balance())     # 5000

# print(acc.__balance)   ❌ AttributeError
# Name mangling দিয়ে access করা যায়:
print(acc._BankAccount__balance)   # 5000
```

✅ Private attribute → সরাসরি বাইরে থেকে access করা যাবে না।

---

## 4️⃣ Static Attribute (Shared by all objects)

👉 Static/Class attributes হলো **class level variable** → সব object একই data share করে।
👉 এগুলোকে আমরা সাধারণত **class এর ভেতরে method দিয়ে define করি না, constructor এর বাইরেই define করি**।
👉 Access করা যায় → `ClassName.attribute` বা `object.attribute` দিয়ে।

```python
class Counter:
    count = 0   # static/class attribute
    
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)  # 3 → তিনটা object তৈরি হয়েছে
```

✅ Static attribute → সব object এর জন্য common থাকে।

---

# 📝 মিলিয়ে দেখা

| Attribute Type   | Declaration Style           | Access Level                                                       | Example                |
| ---------------- | --------------------------- | ------------------------------------------------------------------ | ---------------------- |
| **Public**       | `name`                      | Anywhere                                                           | `obj.name`             |
| **Protected**    | `_name`                     | Class + Subclass (but accessible outside by convention avoid)      | `obj._name`            |
| **Private**      | `__name`                    | Only inside class (outside থেকে access হয় না, name mangling দরকার) | `obj._ClassName__name` |
| **Static/Class** | Defined outside constructor | Shared across all objects                                          | `ClassName.attr`       |

---

# ⚡ Real-life Combined Example

```python
class Student:
    school = "ABC School"       # static/public
    
    def __init__(self, name, age):
        self.name = name         # public
        self._age = age          # protected
        self.__roll = 101        # private
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Roll: {self.__roll}")

s1 = Student("Rahim", 20)
s1.show_info()

print(s1.name)        # Public → Rahim
print(s1._age)        # Protected → conventionally avoid
# print(s1.__roll)    # ❌ Error
print(s1._Student__roll)  # ✅ Name mangling access → 101

print(Student.school)  # Static attribute → ABC School
```

---

# ✅ সারসংক্ষেপ

* **Public** → ডিফল্ট, সবখানে access করা যায়।
* **Protected** (`_var`) → subclass এ use করা যায়, বাইরে থেকে avoid করতে হবে।
* **Private** (`__var`) → বাইরের থেকে access করা যায় না, শুধু class এর ভেতরে।
* **Static/Class Attribute** → সব object এর জন্য একটাই থাকে, class level এ define হয়।

---



## 🐍 Static Method & Object Creation — Concept

👉 Python-এ যখন তুমি কোনো **object create করো**, তখন শুধু **instance attributes (self দিয়ে যেগুলো define হয়)** তার জন্য নতুন মেমোরি স্পেস পায়।

👉 কিন্তু **static method** এবং **class attribute** গুলো আলাদা কোনো space নেয় না, কারণ এগুলো **class-level এ define করা থাকে**।
মানে:

* Instance attribute → প্রতি object এ আলাদা কপি তৈরি হয়
* Static method → class এর সাথে একবারই থাকে, সব object একইটা ব্যবহার করে

---

## 🔹 Example দিয়ে দেখা যাক

```python
class MathOps:
    def __init__(self, x):
        self.x = x   # instance attribute (প্রতিটি object এর জন্য আলাদা)

    def square(self):     # instance method
        return self.x * self.x

    @staticmethod
    def add(a, b):        # static method (class level এ shared)
        return a + b

m1 = MathOps(5)
m2 = MathOps(10)

print(m1.square())   # 25
print(m2.square())   # 100

print(MathOps.add(3, 7))  # 10
print(m1.add(2, 4))       # 6 (object থেকেও কল করা যাবে, কিন্তু method একই)
```

---

## 🔹 মেমোরি পার্থক্য

* `m1` আর `m2` object এর জন্য `self.x` আলাদা জায়গায় রাখা হয়েছে (instance variable)।
* কিন্তু `add()` static method → class এর সাথে একবারই memory তে থাকে।
* তাই **object যত তৈরি করো না কেন, static method এর জন্য নতুন করে জায়গা নেয় না।**

---

## ✅ সারসংক্ষেপ

* **Static method → class-level এ থাকে, object তৈরি করলে আলাদা কপি হয় না।**
* **Instance attributes/methods → প্রতিটি object আলাদা কপি পায়।**
* এজন্য static method বেশি efficient, কারণ একবারই লোড হয় আর সব object share করে।

---

