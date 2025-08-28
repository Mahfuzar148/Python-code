
---

# 🐍 Method Overloading in Python — বিস্তারিত

---

## 🔹 Method Overloading কী?

👉 **একই ক্লাসে একই নামে একাধিক method define করা**, কিন্তু আলাদা parameter list (argument সংখ্যা/টাইপ) দিয়ে → এটাকে বলে **Method Overloading**।

📌 উদাহরণ (Java/C++ এ সাধারণভাবে সম্ভব):

```java
class Math {
    int add(int a, int b) { return a+b; }
    int add(int a, int b, int c) { return a+b+c; }
}
```

👉 Python এ কিন্তু একই ক্লাসে একি নামে দুইটা method লিখলে **শেষেরটা আগেরটাকে override করে দেয়**।
মানে Python এ **traditional method overloading নেই**।

---

## 🔹 Python এ Method Overloading কিভাবে করা হয়?

Python এ আমরা কয়েকভাবে Method Overloading simulate করতে পারি:

1. **Default Arguments** ব্যবহার করে
2. **Variable-length Arguments (`*args`, `**kwargs`)** ব্যবহার করে
3. **Manual type-checking** করে

---

## 📝 Example 1: Default Argument দিয়ে Overloading

```python
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))       # 15 (দুইটা argument)
print(calc.add(2, 3, 4))     # 9  (তিনটা argument)
print(calc.add())            # 0  (কোনো argument নাই)
```

👉 এখানে একটিই `add()` method আছে, কিন্তু default arguments থাকার কারণে এটা multiple cases handle করতে পারছে।

---

## 📝 Example 2: `*args` দিয়ে Overloading

```python
class MathOps:
    def add(self, *args):
        return sum(args)

m = MathOps()
print(m.add(5, 10))           # 15
print(m.add(1, 2, 3, 4, 5))   # 15
print(m.add())                # 0
```

👉 `*args` ব্যবহার করলে যত খুশি argument পাঠানো যায়।

---

## 📝 Example 3: Type-based Overloading

👉 Argument এর টাইপ চেক করে behavior আলাদা করা যায়।

```python
class Display:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print("Two values:", a, b)
        elif a is not None:
            print("One value:", a)
        else:
            print("No value")

d = Display()
d.show()         # No value
d.show(10)       # One value: 10
d.show(10, 20)   # Two values: 10 20
```

---

## 📝 Example 4: Operator Overloading (Special Case)

👉 Python এ operator (+, -, \*, / ইত্যাদি) আসলে method (`__add__`, `__sub__`, `__mul__`) দিয়ে কাজ করে। এগুলো override করলে এটাও এক ধরনের overloading।

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print(b1 + b2)   # 300
```

👉 এখানে `+` operator overloaded হয়েছে।

---

## 🔹 Method Overloading vs Method Overriding

| বিষয়       | Method Overloading                | Method Overriding                             |
| ---------- | --------------------------------- | --------------------------------------------- |
| ঘটে কোথায়  | একই class এর ভেতরে                | Inheritance এ (Parent → Child)                |
| Method নাম | একই                               | একই                                           |
| Parameter  | আলাদা সংখ্যা/টাইপ হতে হবে         | সাধারণত parent এর মতোই, তবে কাস্টমাইজ করা যায় |
| Python এ   | ❌ Directly নেই (simulate করতে হয়) | ✅ পুরোপুরি supported                          |

---

## ✅ সারসংক্ষেপ

* **Traditional Method Overloading** Python এ নেই।
* Python এ overloading **simulate করা যায়**:

  1. Default arguments
  2. `*args`, `**kwargs`
  3. Type-checking
* Operator Overloading (`__add__`, `__sub__`, ইত্যাদি) হলো আরেক রকম polymorphism।
* Overloading = এক class এ একি নামের method → multiple behavior।

---

