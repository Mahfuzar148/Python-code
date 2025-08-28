
---

# 🐍 Dynamic Typing in Class — বিস্তারিত

---

## 🔹 Concept

Python যেহেতু **dynamically typed language**, তাই class এর object/attribute গুলোও runtime এ type পরিবর্তন করতে পারে।

👉 অর্থাৎ –

* Object বানানোর পরও আমরা নতুন attribute যোগ করতে পারি।
* একই attribute এর value বিভিন্ন সময়ে **ভিন্ন type** হতে পারে।

এটাকেই বলে **Dynamic Typing in Class**।

---

## 📝 Example 1: Attribute type পরিবর্তন

```python
class Student:
    def __init__(self, data):
        self.data = data   # dynamic typing

s1 = Student("Rahim")     
print(s1.data, type(s1.data))   # str

s1.data = 101                  
print(s1.data, type(s1.data))   # int

s1.data = [80, 90, 85]          
print(s1.data, type(s1.data))   # list
```

👉 একই object `s1` এর `data` attribute → প্রথমে string, পরে integer, পরে list হলো।
এটাই class এ dynamic typing।

---

## 📝 Example 2: New attribute runtime এ add করা

```python
class Employee:
    def __init__(self, name):
        self.name = name

e1 = Employee("Karim")

# runtime এ নতুন attribute যোগ করা
e1.salary = 25000

print(e1.name)     # Karim
print(e1.salary)   # 25000
```

👉 Python এ object বানানোর পর নতুন attribute add করা যায়। অন্য ভাষায় (C++, Java) এটা সম্ভব না।

---

## 📝 Example 3: Method এ dynamic typing

```python
class Box:
    def __init__(self, value):
        self.value = value

    def show(self):
        print("Value:", self.value, "| Type:", type(self.value))

b = Box(10)
b.show()        # int

b.value = "Hello"
b.show()        # str

b.value = [1,2,3]
b.show()        # list
```

👉 একই method → attribute এর type অনুযায়ী ভিন্নভাবে behave করছে।

---

## 📝 Example 4: Duck Typing (Dynamic Typing এর সাথে সম্পর্কিত)

👉 Class এ dynamic typing এর একটা extension হলো **Duck Typing**।

```python
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane flies in sky")

def make_it_fly(obj):
    obj.fly()   # কোন class সেটা matter করে না

make_it_fly(Bird())      
make_it_fly(Airplane())
```

👉 এখানে `obj` এর type runtime এ নির্ধারণ হচ্ছে। Object এ `fly()` থাকলেই কাজ করবে।

---

## 🔹 Dynamic Typing in Class এর সুবিধা

1. খুব flexible (একই attribute → ভিন্ন type)
2. runtime এ নতুন property/method যোগ করা যায়
3. duck typing এর মাধ্যমে polymorphism সহজ

---

## 🔹 অসুবিধা

1. runtime এ error ধরতে দেরি হয়
2. বড় project এ bug খুঁজে বের করা কঠিন
3. type stability থাকে না

---

## 🔹 Static Typed Language vs Python Class

| বিষয়           | Static Typing (Java/C++)           | Dynamic Typing (Python)               |
| -------------- | ---------------------------------- | ------------------------------------- |
| Attribute type | fix থাকে                           | runtime এ পরিবর্তন হয়                 |
| নতুন attribute | compile time এ error               | runtime এ add করা যায়                 |
| Flexibility    | কম                                 | বেশি                                  |
| Example        | `int roll=10; roll="abc"; ❌ error` | `self.roll=10; self.roll="abc"; ✅ ok` |

---

# ✅ সারসংক্ষেপ

* Python class এ attribute/method গুলো runtime এ type পরিবর্তন করতে পারে → এটিই dynamic typing।
* একই ভ্যারিয়েবল একবার string, পরে int, পরে list হতে পারে।
* runtime এ object এ নতুন attribute/method add করা যায়।
* সুবিধা → flexibility, polymorphism; অসুবিধা → runtime error, maintainability সমস্যা।

---

