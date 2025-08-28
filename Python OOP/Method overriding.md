
---

# 🐍 Method Overriding in Python — বিস্তারিত

---

## 🔹 Method Overriding কী?

👉 যখন কোনো **child class (subclass)** তার **parent class (superclass)** এর method কে **আবার লিখে ফেলে (redefine করে)**, তখন সেটাকে **Method Overriding** বলে।

👉 এর ফলে child class এর object দিয়ে method কল করলে সবসময় **child class এর method execute হবে**, parent এরটা নয়।

---

## 🔹 কেন দরকার?

1. Parent এর behavior কে নিজের মতো কাস্টমাইজ করার জন্য
2. একি নামের method → ভিন্ন ভিন্ন কাজ (Polymorphism)
3. কোড reuse করা এবং flexible design করা

---

## 📝 Example 1: Basic Method Overriding

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   # overriding
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Object
a = Animal()
d = Dog()
c = Cat()

a.speak()   # Animal makes a sound
d.speak()   # Dog barks
c.speak()   # Cat meows
```

👉 Parent এ `speak()` ছিল, কিন্তু child classes নতুনভাবে লিখেছে।

---

## 📝 Example 2: Constructor Overriding

```python
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # parent constructor কল
        self.roll = roll
        print("Student constructor")

s = Student("Rahim", 101)
```

👉 এখানে child constructor parent এর constructor কে override করেছে, তবে `super()` দিয়ে পুরোনোটা কল করেছে।

---

## 📝 Example 3: Method Overriding with `super()`

👉 মাঝে মাঝে আমরা চাই parent এর behavior পুরোপুরি বাদ না দিয়ে, তার সাথে নতুন কিছু যোগ করতে।

```python
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def info(self):
        super().info()   # parent method call
        print("This is a car")

c = Car()
c.info()
```

Output:

```
This is a vehicle
This is a car
```

👉 এখানে child method parent এর method কে extend করেছে।

---

## 📝 Example 4: Banking Example

```python
class Account:
    def interest_rate(self):
        return 5

class SavingsAccount(Account):
    def interest_rate(self):   # overriding
        return 7

class CurrentAccount(Account):
    def interest_rate(self):
        return 3

accounts = [SavingsAccount(), CurrentAccount(), Account()]
for acc in accounts:
    print(acc.__class__.__name__, ":", acc.interest_rate(), "%")
```

Output:

```
SavingsAccount : 7 %
CurrentAccount : 3 %
Account : 5 %
```

👉 একই `interest_rate()` method, কিন্তু account type ভেদে আলাদা আচরণ করছে।

---

## 📝 Example 5: Real-life Shape Example

```python
class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4), Shape()]
for s in shapes:
    print(s.__class__.__name__, "Area:", s.area())
```

Output:

```
Circle Area: 78.5
Square Area: 16
Shape Area: Area not defined
```

👉 Child classes নিজেদের মতো করে `area()` লিখে দিয়েছে।

---

## 🔹 Method Overriding এর বৈশিষ্ট্য

1. Parent class এ method থাকে, child class একই নাম দিয়ে আবার define করে।
2. Child object দিয়ে method কল করলে সবসময় child এরটা কল হবে।
3. `super()` ব্যবহার করলে parent এরটা retain করা যায়।
4. এটি **Polymorphism** এর প্রধান রূপ।

---

## 🔹 Method Overriding vs Method Overloading

| বিষয়       | Overriding                          | Overloading                                                    |
| ---------- | ----------------------------------- | -------------------------------------------------------------- |
| ঘটে কোথায়  | Inheritance এর সময়                  | এক class এর ভেতর                                               |
| Method নাম | একই                                 | একই                                                            |
| Parameter  | parent এর মতো বা পরিবর্তিত হতে পারে | আলাদা সংখ্যা/টাইপের হতে পারে                                   |
| Python এ   | ✅ পুরোপুরি supported                | ❌ Directly নেই, কিন্তু default arguments দিয়ে simulate করা যায় |

---

# ✅ সারসংক্ষেপ

* **Method Overriding** = Parent এর method → Child এ নতুনভাবে লেখা।
* একি নাম → ভিন্ন আচরণ = Polymorphism।
* `super()` দিয়ে parent এর method কল করা যায়।
* Real-life ব্যবহার → Banking system, Shapes, Vehicles ইত্যাদি।

---

