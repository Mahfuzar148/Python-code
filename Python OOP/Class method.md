
---

# 🐍 Python Method — বিস্তারিত

---

## 🔹 Method কী?

* Method হলো **class এর ভেতরে ডিফাইন করা function**।
* Function আর Method প্রায় একই জিনিস, পার্থক্য হলো → method সবসময় কোনো object (বা class) এর সাথে **bound** থাকে।
* Method প্রথম parameter হিসেবে সাধারণত **`self`** (instance method), অথবা **`cls`** (class method) নেয়।

---

## 🔹 Python-এ Method এর ধরন

Python-এ প্রধানত ৩ ধরনের method আছে:

1. **Instance Method**
2. **Class Method**
3. **Static Method**

---

## 1️⃣ Instance Method

👉 সবচেয়ে সাধারণ method।
👉 প্রথম parameter সবসময় `self` হয় → যা object (instance) কে বোঝায়।
👉 এর মাধ্যমে instance attribute (data) access করা যায়।

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):   # instance method
        print(f"My name is {self.name}, age {self.age}")

s1 = Student("Rahim", 20)
s1.introduce()   # My name is Rahim, age 20
```

🟢 এখানে `introduce()` হলো instance method → প্রতিটি object নিজের তথ্য print করছে।

---

## 2️⃣ Class Method (`@classmethod`)

👉 Class এর সাথে bound হয়, object এর সাথে না।
👉 প্রথম parameter হয় `cls` → যেটা class নিজেকে বোঝায়।
👉 এর মাধ্যমে class attributes modify বা access করা যায়।

```python
class Student:
    school = "ABC School"   # class attribute
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_school(cls, new_name):   # class method
        cls.school = new_name

s1 = Student("Rahim")
print(s1.school)  # ABC School

Student.change_school("XYZ School")
print(s1.school)  # XYZ School
```

---

## 3️⃣ Static Method (`@staticmethod`)

👉 Static method class বা object এর সাথে bound হয় না।
👉 কোনো default parameter (`self` বা `cls`) নেয় না।
👉 সাধারণত **utility functions** এর জন্য ব্যবহার হয়।

```python
class MathOps:
    @staticmethod
    def add(a, b):     # static method
        return a + b

print(MathOps.add(5, 7))   # 12
```

---

## 🔹 Special (Magic / Dunder) Methods

Python এ কিছু **built-in methods** আছে যেগুলো double underscore (`__`) দিয়ে শুরু হয়।
এগুলোকে **special methods** বলা হয়।

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
print(b)        # Python Basics (250 pages)  -> __str__ কল হয়েছে
print(len(b))   # 250  -> __len__ কল হয়েছে
```

---

## 🔹 Accessor, Mutator & Property Methods

1. **Accessor Method (Getter)** → ডেটা বের করতে
2. **Mutator Method (Setter)** → ডেটা পরিবর্তন করতে
3. **Property Method** → `@property` দিয়ে attribute-এর মতো access করা যায়

```python
class Person:
    def __init__(self, name):
        self.__name = name
    
    # getter
    @property
    def name(self):
        return self.__name
    
    # setter
    @name.setter
    def name(self, new_name):
        self.__name = new_name

p = Person("Rahim")
print(p.name)     # getter কল হচ্ছে
p.name = "Karim"  # setter কল হচ্ছে
print(p.name)
```

---

# ✅ সারসংক্ষেপ

Python এ Method এর ধরন ও কাজ:

* **Instance Method** → object level data access করে (`self`)
* **Class Method** → class level data access/update করে (`cls`)
* **Static Method** → utility function, self/cls লাগে না
* **Special Methods** → যেমন `__init__`, `__str__`, `__len__` ইত্যাদি
* **Accessor/Mutator** → getter & setter (property দিয়ে control করা যায়)

---

