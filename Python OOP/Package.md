
---

# 🐍 Python Package — বিস্তারিত গাইড

---

## 🔹 Package কী?

👉 Python এ **Package** হলো অনেকগুলো **module** (অর্থাৎ `.py` ফাইল) কে **একসাথে সংগঠিত করার একটি ফোল্ডার**।

* **Module** = একটা `.py` ফাইল (যেখানে functions, classes, variables থাকে)
* **Package** = এক বা একাধিক module এর ফোল্ডার + সাথে একটি `__init__.py` ফাইল থাকে

📌 সহজভাবে:

* Module = একটা বই
* Package = অনেক বইয়ের লাইব্রেরি

---

## 🔹 কেন Package দরকার?

1. কোড **organization** ভালো হয়
2. বড় project **maintain** করা সহজ হয়
3. **Code reusability** বাড়ে
4. অন্য project এ import করে ব্যবহার করা যায়

---

## 📝 Example 1: Simple Package Structure

ধরা যাক আমরা একটা **maths\_package** বানাচ্ছি।

```
maths_package/          # package folder
    __init__.py         # package initializer
    add_module.py       # module 1
    multiply_module.py  # module 2
```

### 👉 `add_module.py`

```python
def add(a, b):
    return a + b
```

### 👉 `multiply_module.py`

```python
def multiply(a, b):
    return a * b
```

### 👉 `__init__.py`

```python
from .add_module import add
from .multiply_module import multiply
```

### 👉 ব্যবহার (main.py)

```python
import maths_package

print(maths_package.add(5, 10))       # 15
print(maths_package.multiply(3, 4))   # 12
```

---

## 📝 Example 2: Sub-Package

Package এর ভিতরে আবার sub-package থাকতে পারে।

```
ecommerce/
    __init__.py
    shopping/
        __init__.py
        cart.py
        payment.py
```

### 👉 `cart.py`

```python
def add_to_cart(item):
    print(f"{item} added to cart")
```

### 👉 `payment.py`

```python
def pay(amount):
    print(f"Paid {amount} successfully")
```

### 👉 ব্যবহার

```python
from ecommerce.shopping import cart, payment

cart.add_to_cart("Laptop")
payment.pay(50000)
```

👉 Output:

```
Laptop added to cart
Paid 50000 successfully
```

---

## 📝 Example 3: Alias এবং Selective Import

```python
from maths_package.add_module import add as addition

print(addition(7, 8))   # 15
```

👉 এখানে `as` ব্যবহার করে alias করা হয়েছে।

---

## 📝 Example 4: Built-in Packages

Python এ অনেক বিল্ট-ইন প্যাকেজ আছে যেগুলো আমরা import করে ব্যবহার করি:

```python
import math
import os
import random

print(math.sqrt(25))     # 5.0
print(os.getcwd())       # current directory দেখাবে
print(random.randint(1, 10))  # random সংখ্যা
```

---

## 🔹 Package vs Module

| বিষয়       | Module               | Package                           |
| ---------- | -------------------- | --------------------------------- |
| Definition | একটি `.py` ফাইল      | এক বা একাধিক module এর ফোল্ডার    |
| Example    | `math.py`            | `numpy`, `pandas`                 |
| Usage      | `import module_name` | `import package_name.module_name` |
| Scope      | ছোট                  | বড় project এর জন্য                |

---

## 🔹 জনপ্রিয় Python Package

1. **NumPy** → numerical computation
2. **Pandas** → data analysis
3. **Matplotlib** → data visualization
4. **Requests** → HTTP requests
5. **Django / Flask** → web development

```python
import numpy as np
import pandas as pd

arr = np.array([1,2,3])
print(arr*2)

df = pd.DataFrame({"Name":["Rahim","Karim"], "Age":[21,22]})
print(df)
```

---

# ✅ সারসংক্ষেপ

* **Module** = `.py` ফাইল
* **Package** = module এর ফোল্ডার (`__init__.py` সহ)
* Sub-package ও থাকতে পারে
* Import করার মাধ্যমে অন্য ফাইলের functions/class ব্যবহার করা যায়
* Popular packages: `numpy`, `pandas`, `requests`, `django`, `flask`

---

