
---

# 🔹 Python এর Basic Syntax Discussion

### ১. Python এ Indentation (স্পেস/ট্যাব) খুব গুরুত্বপূর্ণ

```python
if True:
    print("Hello World")   # সঠিক
# যদি ইনডেন্টেশন ঠিক না থাকে তাহলে error দিবে
```

---

### ২. Comment লেখা

```python
# এটা single line comment
"""
এটা multi-line comment
একাধিক লাইন এ লেখা যায়
"""
```

---

### ৩. Print Function

```python
print("Hello Python!")
print(10 + 20)
```

---

### ৪. Variable

```python
name = "Rahim"
age = 20
print(name, age)
```

---

### ৫. Data Types

```python
a = 10        # integer
b = 10.5      # float
c = "Python"  # string
d = True      # boolean
```

---

### ৬. Type Checking

```python
x = 100
print(type(x))   # <class 'int'>
```

---

### ৭. Input নেওয়া

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

### ৮. Arithmetic Operators

```python
a, b = 10, 3
print(a + b)   # যোগ
print(a - b)   # বিয়োগ
print(a * b)   # গুণ
print(a / b)   # ভাগ (ভগ্নাংশ সহ)
print(a // b)  # ভাগফল (ইন্টিজার)
print(a % b)   # ভাগশেষ
print(a ** b)  # ঘাত
```

---

### ৯. Comparison Operators

```python
print(5 > 3)   # True
print(5 == 5)  # True
print(5 != 3)  # True
```

---

### ১০. Logical Operators

```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

---

### ১১. if-else

```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Child")
```

---

### ১২. elif

```python
mark = 65
if mark >= 80:
    print("A+")
elif mark >= 60:
    print("B")
else:
    print("Fail")
```

---

### ১৩. While Loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

### ১৪. For Loop

```python
for i in range(1, 6):
    print(i)
```

---

### ১৫. Break & Continue

```python
for i in range(1, 6):
    if i == 3:
        continue   # ৩ বাদ যাবে
    if i == 5:
        break      # ৫ আসার আগেই থামবে
    print(i)
```

---

### ১৬. List

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
fruits.append("orange")
print(fruits)
```

---

### ১৭. Tuple

```python
numbers = (1, 2, 3)
print(numbers[1])   # 2
```

---

### ১৮. Set

```python
s = {1, 2, 3, 3}
print(s)   # {1, 2, 3} (ডুপ্লিকেট বাদ যাবে)
```

---

### ১৯. Dictionary

```python
student = {"name": "Rahim", "age": 20}
print(student["name"])  # Rahim
```

---

### ২০. Function

```python
def greet(name):
    return "Hello " + name

print(greet("Sami"))
```

---

### ২১. Lambda Function

```python
square = lambda x: x*x
print(square(5))   # 25
```

---

### ২২. Class & Object

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rahim")
print(s1.name)
```

---

### ২৩. Exception Handling

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero not allowed!")
```

---

### ২৪. File Handling

```python
f = open("test.txt", "w")
f.write("Hello Python File")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()
```

---

### ২৫. Module Import

```python
import math
print(math.sqrt(16))   # 4.0
```

---


---

# 🔹 Python Extra 25 Examples with Explanation

---

### ১. Multiple Assignment

```python
a, b, c = 10, 20, 30
print(a, b, c)
```

👉 একসাথে একাধিক ভেরিয়েবলে ভ্যালু দেওয়া যায়।

---

### ২. Swap Variables

```python
x, y = 5, 10
x, y = y, x
print(x, y)   # 10 5
```

👉 এক লাইনে দুইটা ভেরিয়েবল swap করা যায়।

---

### ৩. String Concatenation

```python
first = "Hello"
second = "World"
print(first + " " + second)
```

👉 `+` দিয়ে স্ট্রিং যোগ করা যায়।

---

### ৪. String Formatting (f-string)

```python
name = "Rahim"
age = 20
print(f"My name is {name}, I am {age} years old.")
```

👉 f-string ব্যবহার করলে সহজে ভ্যালু ইনসার্ট করা যায়।

---

### ৫. String Methods

```python
text = "  python programming  "
print(text.upper())     # বড় হাতের অক্ষর
print(text.strip())     # ফাঁকা স্পেস কেটে দেয়
print(text.replace("python", "java"))
```

---

### ৬. Membership Operator

```python
fruits = ["apple", "banana"]
print("apple" in fruits)   # True
print("mango" not in fruits) # True
```

👉 `in` এবং `not in` দিয়ে কোন ভ্যালু আছে কিনা চেক করা যায়।

---

### ৭. List Slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[-2:])   # [40, 50]
```

---

### ৮. Nested List

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])   # 6
```

👉 লিস্টের ভিতরে লিস্ট।

---

### ৯. List Comprehension

```python
squares = [x*x for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

👉 এক লাইনে লিস্ট বানানোর শর্টকাট।

---

### ১০. Dictionary Methods

```python
student = {"name":"Sami","age":18}
print(student.keys())
print(student.values())
print(student.items())
```

---

### ১১. Dictionary Update

```python
student = {"name":"Rahim"}
student["age"] = 20
print(student)
```

---

### ১২. Set Operations

```python
a = {1,2,3}
b = {3,4,5}
print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
```

---

### ১৩. enumerate() Function

```python
fruits = ["apple","banana","mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

👉 index + value একসাথে পাওয়া যায়।

---

### ১৪. zip() Function

```python
names = ["Rahim","Karim"]
ages = [20, 22]
for n, a in zip(names, ages):
    print(n, a)
```

👉 একাধিক লিস্ট একসাথে iterate করা যায়।

---

### ১৫. Any & All

```python
print(any([False, True, False]))  # True
print(all([True, True, True]))    # True
```

👉 `any()` → যেকোনো একটা True হলে True
👉 `all()` → সব True হলে True

---

### ১৬. Map Function

```python
numbers = [1, 2, 3]
squares = list(map(lambda x: x*x, numbers))
print(squares)
```

---

### ১৭. Filter Function

```python
numbers = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, numbers))
print(even)   # [2,4,6]
```

---

### ১৮. Reduce Function

```python
from functools import reduce
numbers = [1,2,3,4]
sum_all = reduce(lambda x,y: x+y, numbers)
print(sum_all)   # 10
```

---

### ১৯. Recursive Function

```python
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
```

---

### ২০. Default Parameter in Function

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rahim")
```

---

### ২১. \*args ব্যবহার

```python
def add(*numbers):
    return sum(numbers)

print(add(1,2,3,4))   # 10
```

👉 একাধিক ভ্যালু function এ পাঠানো যায়।

---

### ২২. \*\*kwargs ব্যবহার

```python
def info(**data):
    for key, value in data.items():
        print(key, ":", value)

info(name="Sami", age=20, city="Dhaka")
```

---

### ২৩. Global vs Local Variable

```python
x = 10  # global

def show():
    x = 5   # local
    print(x)

show()
print(x)
```

---

### ২৪. List Copy (shallow copy problem)

```python
a = [1,2,3]
b = a
b[0] = 100
print(a)   # [100,2,3] (কারণ একই রেফারেন্স)
```

---

### ২৫. Proper List Copy

```python
a = [1,2,3]
b = a.copy()
b[0] = 100
print(a)   # [1,2,3]
print(b)   # [100,2,3]
```

---


