
---

# 🐍 Inner Class in Python — বিস্তারিত

---

## 🔹 Inner Class কী?

👉 যখন একটি class এর ভেতরে আরেকটি class define করা হয়, সেটাকে **Inner Class** বা **Nested Class** বলে।

📌 অর্থাৎ —

* Outer Class → বাইরের বড় ক্লাস
* Inner Class → ভেতরে থাকা ক্লাস

**Use Case:**

* কোনো class এর সাথে strongly related sub-class লাগলে Inner Class ব্যবহার করা হয়।
* Data structure, GUI, Database, ইত্যাদিতে nested class অনেক দরকার হয়।

---

## 🔹 Inner Class Syntax

```python
class Outer:
    class Inner:
        pass
```

---

## 📝 Example 1: Basic Inner Class

```python
class Outer:
    def __init__(self):
        self.name = "Outer Class"
    
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        
        def show(self):
            print("This is Inner Class")

# Outer এর object
outer = Outer()
print(outer.name)

# Inner এর object
inner = Outer.Inner()
inner.show()
```

👉 Output:

```
Outer Class
This is Inner Class
```

---

## 📝 Example 2: Inner Class as Helper

```python
class Person:
    def __init__(self, name, city):
        self.name = name
        self.address = self.Address(city)   # Inner Class object
    
    def show(self):
        print("Name:", self.name)
        self.address.show()
    
    # Inner Class
    class Address:
        def __init__(self, city):
            self.city = city
        
        def show(self):
            print("City:", self.city)

p = Person("Rahim", "Dhaka")
p.show()
```

👉 Output:

```
Name: Rahim
City: Dhaka
```

🔹 এখানে `Address` হলো `Person` এর inner class → অর্থাৎ address class শুধুই person এর জন্য।

---

## 📝 Example 3: Multiple Inner Classes

```python
class University:
    def __init__(self, name):
        self.name = name
        self.department = self.Department("CSE")
        self.library = self.Library("Central Library")
    
    def show(self):
        print("University:", self.name)
        self.department.show()
        self.library.show()
    
    class Department:
        def __init__(self, dept):
            self.dept = dept
        def show(self):
            print("Department:", self.dept)
    
    class Library:
        def __init__(self, lib_name):
            self.lib_name = lib_name
        def show(self):
            print("Library:", self.lib_name)

u = University("DU")
u.show()
```

👉 Output:

```
University: DU
Department: CSE
Library: Central Library
```

---

## 📝 Example 4: Access Control in Inner Class

```python
class Company:
    def __init__(self):
        self.emp = self.Employee("Rahim", 25000)
    
    def show(self):
        self.emp.details()
    
    class Employee:
        def __init__(self, name, salary):
            self.__name = name        # private attribute
            self.__salary = salary    # private attribute
        
        def details(self):
            print(f"Employee: {self.__name}, Salary: {self.__salary}")

c = Company()
c.show()
```

👉 Output:

```
Employee: Rahim, Salary: 25000
```

🔹 এখানে `Employee` inner class এর private data শুধুমাত্র method এর মাধ্যমে access করা যাচ্ছে (Encapsulation এর সাথে ব্যবহার হয়েছে)।

---

## 🔹 কেন Inner Class ব্যবহার করা হয়?

1. Outer class এর সাথে সম্পর্কিত sub-class কে আলাদা না রেখে একই জায়গায় রাখতে।
2. কোড **readability ও organization** বাড়ানোর জন্য।
3. বড় Project এ class গুলো logically group করার জন্য।
4. Encapsulation ও data hiding সহজ হয়।

---

## 🔹 Inner Class বনাম Normal Class

| বিষয়    | Normal Class                      | Inner Class                                |
| ------- | --------------------------------- | ------------------------------------------ |
| অবস্থান | আলাদা ফাইল বা module এ থাকতে পারে | Outer Class এর ভেতরে define করা হয়         |
| সম্পর্ক | স্বাধীনভাবে ব্যবহার করা যায়       | Outer class এর সাথে strongly related       |
| Import  | সহজেই import করা যায়              | সাধারণত outer class ছাড়া ব্যবহার করা হয় না |

---

# ✅ সারসংক্ষেপ

* **Inner Class** = Outer class এর ভেতরে define করা class।
* Directly `Outer.Inner()` দিয়ে object তৈরি করা যায়।
* Outer class object এর property/method এর মাধ্যমে inner class ব্যবহার করা যায়।
* ব্যবহার: **Helper class**, **Logical grouping**, **Encapsulation**।

---

