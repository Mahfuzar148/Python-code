
---

# 📌 Python Function এর ধরন + অনেক Example

---

## 1. **Built-in Function**

Python এ আগে থেকেই তৈরি করা ফাংশন।

```python
print("Bangladesh")        # আউটপুট: Bangladesh
print(len("Dhaka"))        # আউটপুট: 5
print(max([2, 7, 3]))      # আউটপুট: 7
print(min([2, 7, 3]))      # আউটপুট: 2
print(sum([1, 2, 3, 4]))   # আউটপুট: 10
print(type(100))           # আউটপুট: <class 'int'>
print(abs(-10))            # আউটপুট: 10
```

---

## 2. **User-defined Function**

নিজে function বানিয়ে ব্যবহার করা।

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Fahim"))   # আউটপুট: Hello, Fahim

# আরেকটা Example: যোগফল
def add(a, b):
    return a + b

print(add(5, 7))   # আউটপুট: 12
```

---

## 3. **Lambda Function (Anonymous Function)**

এক লাইনের ছোট function।

```python
square = lambda x: x*x
print(square(6))   # আউটপুট: 36

add = lambda a, b: a + b
print(add(4, 9))   # আউটপুট: 13

# লিস্ট sort করার সময়
numbers = [(1, 'one'), (3, 'three'), (2, 'two')]
numbers.sort(key=lambda x: x[0])
print(numbers)   # আউটপুট: [(1, 'one'), (2, 'two'), (3, 'three')]
```

---

## 4. **Recursive Function**

নিজেকেই কল করে।

```python
# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))   # আউটপুট: 120

# Fibonacci সিরিজ
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(6)])  # আউটপুট: [0, 1, 1, 2, 3, 5]
```

---

## 5. **Higher-order Function**

একটা function আরেকটা function কে প্যারামিটার হিসেবে নেয়।

```python
def square(x):
    return x*x

def cube(x):
    return x*x*x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))  # আউটপুট: 25
print(apply_function(cube, 3))    # আউটপুট: 27

# Python এ ready-made higher-order function
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*2, nums)))   # আউটপুট: [2, 4, 6, 8, 10]
print(list(filter(lambda x: x%2==0, nums))) # আউটপুট: [2, 4]
```

---

## 6. **Generator Function**

`yield` ব্যবহার করে একে একে ভ্যালু দেয়।

```python
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)

# Example 2: Even number generator
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

print(list(even_numbers(10)))  # আউটপুট: [0, 2, 4, 6, 8, 10]
```

---

## 7. **Nested Function**

ফাংশনের ভিতরে আরেকটা function থাকে।

```python
def outer(name):
    def inner():
        return f"Hello, {name}"
    return inner()

print(outer("Sakib"))  # আউটপুট: Hello, Sakib

# Example 2
def math_operation(a, b):
    def add():
        return a + b
    def multiply():
        return a * b
    return add(), multiply()

print(math_operation(5, 10))  # আউটপুট: (15, 50)
```

---

## 8. **Anonymous Function**

নামের দরকার হয় না। (lambda দিয়েই হয়)

```python
print((lambda x: x+10)(5))   # আউটপুট: 15
print((lambda a, b: a*b)(3, 4))  # আউটপুট: 12
```

---

## 9. **OOP Method**

### 🔹 Instance Method

```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        return f"Name: {self.name}"

s = Student("Rahim")
print(s.show())   # আউটপুট: Name: Rahim
```

### 🔹 Class Method

```python
class Student:
    count = 0
    def __init__(self):
        Student.count += 1
    
    @classmethod
    def total_students(cls):
        return cls.count

s1 = Student()
s2 = Student()
print(Student.total_students())  # আউটপুট: 2
```

### 🔹 Static Method

```python
class Math:
    @staticmethod
    def add(a, b):
        return a+b

print(Math.add(5, 7))   # আউটপুট: 12
```

---

# ✅ সারসংক্ষেপ

| Function Type | Example কাজ                |
| ------------- | -------------------------- |
| Built-in      | `print(), len(), sum()`    |
| User-defined  | নিজের function বানানো      |
| Lambda        | ছোট এক লাইনের function     |
| Recursive     | Factorial, Fibonacci       |
| Higher-order  | `map(), filter()`          |
| Generator     | `yield` দিয়ে value দেয়   |
| Nested        | Function এর ভিতরে function |
| Anonymous     | নাম ছাড়া lambda           |
| OOP Methods   | Instance, Class, Static    |

---



---

# 📌 Python Function Parameter Types with Example

---

## 1. **Single Parameter Function**

একটি parameter ব্যবহার করা হয়।

```python
def square(x):
    return x * x

print(square(5))   # আউটপুট: 25
```

---

## 2. **Multiple Parameter Function**

একাধিক parameter নেয়।

```python
def add(a, b, c):
    return a + b + c

print(add(2, 3, 4))   # আউটপুট: 9
```

---

## 3. **List as Parameter**

ফাংশনের মধ্যে লিস্ট পাঠানো।

```python
def total(numbers):
    return sum(numbers)

print(total([1, 2, 3, 4, 5]))   # আউটপুট: 15
```

---

## 4. **Tuple as Parameter**

```python
def show_tuple(data):
    for item in data:
        print(item)

show_tuple((10, 20, 30))  
# আউটপুট: 10, 20, 30
```

---

## 5. **Set as Parameter**

```python
def show_set(items):
    for item in items:
        print(item)

show_set({1, 2, 3, 4})  
# আউটপুট: 1 2 3 4 (order fixed না)
```

---

## 6. **Dictionary as Parameter**

```python
def show_dict(data):
    for key, value in data.items():
        print(f"{key}: {value}")

show_dict({"name": "Rahim", "age": 25, "city": "Dhaka"})
# আউটপুট:
# name: Rahim
# age: 25
# city: Dhaka
```

---

## 7. **Default Parameter Value**

কোনো argument না দিলেও কাজ করবে।

```python
def greet(name="Guest"):
    return f"Hello {name}"

print(greet())          # আউটপুট: Hello Guest
print(greet("Fahim"))   # আউটপুট: Hello Fahim
```

---

## 8. \**Variable-length Arguments (*args)**

যত খুশি argument পাঠানো যায় (tuple আকারে ধরে)।

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4, 5))   # আউটপুট: 15
```

---

## 9. \*\*Keyword Arguments (**kwargs)**

Dictionary আকারে parameter নেয়।

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Rahim", age=20, city="Dhaka")
# আউটপুট:
# name: Rahim
# age: 20
# city: Dhaka
```

---

## 10. **Mixed Parameters**

সব একসাথে ব্যবহার করা যায়।

```python
def student_info(name, *subjects, **details):
    print("Name:", name)
    print("Subjects:", subjects)
    print("Details:", details)

student_info("Karim", "Math", "English", age=22, city="Khulna")
# আউটপুট:
# Name: Karim
# Subjects: ('Math', 'English')
# Details: {'age': 22, 'city': 'Khulna'}
```

---

## 11. **Function Parameter as List Processing**

```python
def double_list(numbers):
    return [x*2 for x in numbers]

print(double_list([1, 2, 3]))   # আউটপুট: [2, 4, 6]
```

---

## 12. **Unpacking Arguments**

লিস্ট/টuple থেকে value unpack করে পাঠানো যায়।

```python
def add(a, b, c):
    return a+b+c

nums = [2, 3, 4]
print(add(*nums))   # আউটপুট: 9

data = {"a": 5, "b": 7, "c": 8}
print(add(**data))  # আউটপুট: 20
```

---

# ✅ Quick Summary

| Parameter Type       | Example                     |
| -------------------- | --------------------------- |
| Single Parameter     | `def f(x)`                  |
| Multi Parameter      | `def f(a, b, c)`            |
| List Parameter       | `def f(lst)`                |
| Tuple Parameter      | `def f(tup)`                |
| Set Parameter        | `def f(st)`                 |
| Dictionary Parameter | `def f(dic)`                |
| Default Parameter    | `def f(name="Guest")`       |
| \*args (tuple)       | `def f(*args)`              |
| \*\*kwargs (dict)    | `def f(**kwargs)`           |
| Mixed                | `def f(a, *args, **kwargs)` |
| Unpacking            | `f(*list), f(**dict)`       |

---


অসাধারণ প্রশ্ন 👌
Python এ **একটা function থেকে একাধিক value return** করা যায়। এটা খুবই useful যখন একসাথে অনেক তথ্য দরকার হয়।

---

# 📌 Multiple Value Return in Python

## 1. **Tuple আকারে return করা** (সবচেয়ে সাধারণ পদ্ধতি)

```python
def calc(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul   # একসাথে তিনটা value return করবে

result = calc(10, 5)
print(result)        # আউটপুট: (15, 5, 50)

# আলাদা আলাদা ভেরিয়েবলেও রাখা যায়
x, y, z = calc(10, 5)
print("Add:", x)     # 15
print("Sub:", y)     # 5
print("Mul:", z)     # 50
```

---

## 2. **List আকারে return করা**

```python
def even_odd(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return [even, odd]

nums = [1, 2, 3, 4, 5, 6]
result = even_odd(nums)
print("Even:", result[0])   # [2, 4, 6]
print("Odd:", result[1])    # [1, 3, 5]
```

---

## 3. **Dictionary আকারে return করা** (key দিয়ে সহজে access করা যায়)

```python
def student_info():
    return {"name": "Rahim", "age": 20, "cgpa": 3.85}

info = student_info()
print(info["name"])   # Rahim
print(info["cgpa"])   # 3.85
```

---

## 4. **Set আকারে return করা**

```python
def unique_numbers():
    return {1, 2, 3, 4}

print(unique_numbers())   # {1, 2, 3, 4}
```

---

## 5. **Mixed Data Return**

```python
def details():
    name = "Karim"
    marks = [85, 90, 78]
    address = {"city": "Dhaka", "zip": 1207}
    return name, marks, address

n, m, a = details()
print(n)          # Karim
print(m)          # [85, 90, 78]
print(a["city"])  # Dhaka
```

---

## 6. **Real-life Example: Shopping Cart**

```python
def checkout(prices):
    total = sum(prices)
    count = len(prices)
    avg = total / count
    return total, count, avg

t, c, a = checkout([100, 200, 300, 400])
print("Total:", t)      # 1000
print("Items:", c)      # 4
print("Average:", a)    # 250.0
```

---

# ✅ সারসংক্ষেপ

Python function return করতে পারে:

* **Tuple** → `return a, b, c`
* **List** → `return [a, b, c]`
* **Dictionary** → `return {"x": a, "y": b}`
* **Set** → `return {a, b, c}`
* **Mixed data** → (string, list, dict ইত্যাদি)

---




# Python Functions & Modules — বিস্তারিত + ৩০ উদাহরণ

## A) Functions (Basics)

### 1) বেসিক ফাংশন ও রিটার্ন

```python
def add(a, b):
    return a + b

print(add(2, 3))  # 5
```

**ব্যাখ্যা:** `def` দিয়ে ফাংশন ডিফাইন, `return` দিয়ে মান ফেরত।

### 2) ডকস্ট্রিং ও সাহায্য

```python
def area_circle(r):
    """Return area of a circle of radius r."""
    from math import pi
    return pi * r * r

print(area_circle.__doc__)
```

**ব্যাখ্যা:** প্রথম ট্রিপল-কোটেড স্ট্রিং = ডকস্ট্রিং। IDE/`help()` এ দেখা যায়।

### 3) একাধিক রিটার্ন ভ্যালু (টিউপল প্যাক/আনপ্যাক)

```python
def divmod2(a, b):
    q = a // b
    r = a % b
    return q, r

q, r = divmod2(17, 5)
print(q, r)  # 3 2
```

**ব্যাখ্যা:** একসাথে একাধিক মান ফেরত—টিউপল হিসেবে।

---

## B) Default Arguments

### 4) ডিফল্ট আর্গুমেন্ট

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()            # Hello, Guest!
greet("Sami")      # Hello, Sami!
```

**ব্যাখ্যা:** আর্গুমেন্ট না দিলে ডিফল্ট ভ্যালু ব্যবহার।

### 5) মিউটেবল ডিফল্টের সমস্যা ও সমাধান

```python
# ভুল প্যাটার্ন
def add_item_bad(x, bucket=[]):
    bucket.append(x)
    return bucket

# সঠিক প্যাটার্ন
def add_item(x, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(x)
    return bucket

print(add_item(1))  # [1]
print(add_item(2))  # [2]  (প্রতি কলে নতুন লিস্ট)
```

**ব্যাখ্যা:** মিউটেবল ডিফল্ট একবারই ইভ্যালুয়েট হয়—শেয়ারিং বাগ এড়াতে `None`-গার্ড।

---

## C) Keyword Arguments

### 6) কীওয়ার্ড আর্গুমেন্ট ও অর্ডার-স্বাধীনতা

```python
def power(base, exp):
    return base ** exp

print(power(exp=3, base=2))  # 8
```

**ব্যাখ্যা:** আর্গুমেন্টের নাম দিয়ে দিলে অর্ডার মিক্স হলেও কাজ করে।

---

## D) Keyword-Only Arguments

### 7) `*` দিয়ে keyword-only বানানো

```python
def connect(host, *, port=5432, ssl=True):
    return f"host={host}, port={port}, ssl={ssl}"

print(connect("db.local", port=5433))  # keyword দিয়ে দিতে হবে
```

**ব্যাখ্যা:** `*`-এর পরের সব আর্গুমেন্ট keyword-only।

### 8) মিক্সড সিগনেচার

```python
def paginate(items, /, page, *, per_page=10):
    start = (page-1) * per_page
    return items[start:start+per_page]

print(paginate(list(range(1,31)),  page=2, per_page=5))
```

**ব্যাখ্যা:** এখানে `items` positional-only (নিচে বিস্তারিত), `page` ফ্রি, `per_page` keyword-only।

---

## E) Positional Arguments

### 9) সাধারণ positional ব্যবহার

```python
def rect_area(w, h):
    return w * h

print(rect_area(4, 6))  # 24
```

**ব্যাখ্যা:** অর্ডার গুরুত্বপূর্ণ; নাম না দিলে পজিশন ধরে মিলাতে হয়।

---

## F) Positional-Only Arguments (Python 3.8+)

### 10) `/` দিয়ে positional-only

```python
def ratio(x, y, /):
    return x / y

print(ratio(10, 2))   # 5.0
# ratio(x=10, y=2)   # TypeError: keyword নেওয়া যাবে না
```

**ব্যাখ্যা:** `/`-এর বামের আর্গুমেন্ট শুধু পজিশনাল।

### 11) `/` ও `*` একসাথে

```python
def f(a, b, /, c, *, d):
    return a, b, c, d

print(f(1, 2, 3, d=4))     # (1,2,3,4)
# f(a=1, b=2, c=3, d=4)   # TypeError
```

**ব্যাখ্যা:** `/` → a,b শুধু পজিশনাল; `*` → d keyword-only।

---

## G) Arbitrary Arguments (`*args`, `**kwargs`)

### 12) `*args` — অনির্দিষ্ট সংখ্যক পজিশনাল

```python
def total(*nums):
    return sum(nums)

print(total(1,2,3,4))  # 10
```

**ব্যাখ্যা:** `*args` টিউপল হিসেবে সব বাড়তি পজিশনাল ধরে।

### 13) `**kwargs` — অনির্দিষ্ট সংখ্যক কীওয়ার্ড

```python
def show(**info):
    for k, v in info.items():
        print(k, "=", v)

show(name="Rakib", age=21)
```

**ব্যাখ্যা:** `**kwargs` ডিকশনারি হিসেবে বাড়তি কীওয়ার্ড ধরে।

### 14) উভয় একসাথে + অর্ডার রুল

```python
def demo(a, b=0, *args, c=10, **kw):
    return a, b, args, c, kw

print(demo(1, 2, 3, 4, c=99, x=7))  
# a=1, b=2, args=(3,4), c=99, kw={'x':7}
```

**ব্যাখ্যা:** অর্ডার: positional → defaulted → \*args → keyword-only → \*\*kwargs।

### 15) আর্গুমেন্ট আনপ্যাকিং করে কল

```python
def fmt(a, b, c):
    return f"{a}-{b}-{c}"

t = (1, 2, 3)
d = {"a":10, "b":20, "c":30}
print(fmt(*t))      # 1-2-3
print(fmt(**d))     # 10-20-30
```

**ব্যাখ্যা:** কলের সময় `*`/`**` দিয়ে আনপ্যাকিং।

---

## H) Variables Scope (LEGB), `global`, `nonlocal`

### 16) লোকাল বনাম গ্লোবাল

```python
x = 10  # global

def foo():
    x = 5   # local
    return x

print(foo(), x)  # 5 10
```

**ব্যাখ্যা:** একই নাম স্কোপভেদে আলাদা হয়।

### 17) `global` দিয়ে গ্লোবাল বদলানো

```python
count = 0
def inc():
    global count
    count += 1

inc(); inc()
print(count)  # 2
```

**ব্যাখ্যা:** গ্লোবাল নামের রিবাইন্ড করতে `global` লাগবে।

### 18) ক্লোজার + `nonlocal`

```python
def make_counter():
    n = 0
    def step():
        nonlocal n
        n += 1
        return n
    return step

c = make_counter()
print(c(), c(), c())  # 1 2 3
```

**ব্যাখ্যা:** ইননার ফাংশন এনক্লোজিং স্কোপের ভ্যারিয়েবল আপডেট করতে `nonlocal`।

---

## I) Function Annotations (Type Hints)

### 19) বেসিক অ্যানোটেশন

```python
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

**ব্যাখ্যা:** রানটাইমে বাধ্যতামূলক না; টুলিং/IDE/স্ট্যাটিক চেকারে কাজে দেয়।

### 20) কলেবল টাইপ, Optional, Iterable

```python
from typing import Callable, Optional, Iterable

def apply(xs: Iterable[int], fn: Callable[[int], int]) -> list[int]:
    return [fn(x) for x in xs]

def maybe_len(s: Optional[str]) -> int:
    return len(s) if s else 0
```

**ব্যাখ্যা:** উন্নত টাইপ-হিন্ট—রিডেবিলিটি ও টুলিং উন্নত।

---

## J) Higher-Order, Lambda, Decorators

### 21) হাইয়ার-অর্ডার ফাংশন (ফাংশন পাস)

```python
def twice(fn, x):
    return fn(fn(x))

def inc(n): return n + 1

print(twice(inc, 3))  # 5
```

**ব্যাখ্যা:** ফাংশনও অবজেক্ট—আর্গুমেন্ট/রিটার্নে ব্যবহার হয়।

### 22) ল্যাম্বডা ও `sorted(key=...)`

```python
pairs = [("b", 3), ("a", 5), ("c", 1)]
print(sorted(pairs, key=lambda kv: kv[1]))  # মান ধরে sort
```

**ব্যাখ্যা:** অ্যানোনিমাস ফাংশন ছোট কাজের জন্য।

### 23) সিম্পল ডেকোরেটর

```python
def log(fn):
    def inner(*args, **kw):
        print("calling:", fn.__name__, args, kw)
        return fn(*args, **kw)
    return inner

@log
def mul(a, b): return a*b

print(mul(3, 4))
```

**ব্যাখ্যা:** ফাংশন র‍্যাপ করে অতিরিক্ত আচরণ যোগ করা।

### 24) প্যারামিটারাইজড ডেকোরেটর

```python
def repeat(n):
    def deco(fn):
        def inner(*args, **kw):
            res = None
            for _ in range(n):
                res = fn(*args, **kw)
            return res
        return inner
    return deco

@repeat(3)
def ping(): print("ping")

ping()
```

**ব্যাখ্যা:** ডেকোরেটরও ফ্যাক্টরি হতে পারে।

---

## K) Modules

### 25) মডিউল ইমপোর্ট (স্ট্যান্ডার্ড)

```python
import math
print(math.sqrt(16), math.pi)
```

**ব্যাখ্যা:** পুরো মডিউল ইমপোর্ট; নামস্পেস `math.` দিয়ে অ্যাক্সেস।

### 26) `from ... import ...` ও এলিয়াস

```python
from math import sqrt as rt
print(rt(25))  # 5.0
```

**ব্যাখ্যা:** নির্দিষ্ট মেম্বার ইমপোর্ট; `as` দিয়ে এলিয়াস।

### 27) নিজের মডিউল (ধরা যাক `utils.py`)

```python
# utils.py
def shout(s): return s.upper() + "!"

# main.py
import utils
print(utils.shout("hello"))
```

**ব্যাখ্যা:** একই ফোল্ডারের `.py` ফাইল = মডিউল; ইমপোর্ট করে ফাংশন ব্যবহার।

---

## L) Built-in Functions (টপিক-রিলেটেড)

### 28) `map`, `filter`, `sum`

```python
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))
print(doubled, evens, sum(nums))
```

**ব্যাখ্যা:** ফাংশনাল স্টাইলে ট্রান্সফরমেশন/ফিল্টারিং।

### 29) `any`, `all`, `enumerate`, `zip`

```python
flags = [True, True, False]
print(any(flags), all(flags))  # True False

for i, v in enumerate(["a","b"], start=1):
    print(i, v)

for a, b in zip([1,2], [10, 20, 30]):
    print(a, b)  # ৩য় আইটেম কাটবে
```

**ব্যাখ্যা:** বুলিয়ান অ্যাগ্রিগেশন, ইনডেক্সিং, পেয়ারিং।

### 30) `dir`, `callable`, `help` (ইনস্পেকশন)

```python
import math
print(callable(math.sqrt))  # True
print([name for name in dir(math) if name.startswith('s')][:5])
# help(math)  # ইন্টারঅ্যাক্টিভ কনসোলে দেখা ভালো
```

**ব্যাখ্যা:** অবজেক্ট ইন্সপেক্ট করা—কি কি অ্যাট্রিবিউট/কলেবল আছে।

---

## দ্রুত রিক্যাপ

* **Arguments System**: positional, keyword, keyword-only (`*`), positional-only (`/`), default, `*args`, `**kwargs`, আনপ্যাকিং।
* **Scope**: LEGB, `global`, `nonlocal`, closures।
* **Annotations**: টাইপ হিন্ট—রিডেবিলিটি/টুলিং।
* **Modules**: import প্যাটার্ন, নিজের মডিউল।
* **Built-ins**: map/filter/zip/enumerate/any/all/sum/dir/help…

---

