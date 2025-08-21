
---

# Python Variables: বিস্তারিত আলোচনা

* **ভ্যারিয়েবল কী?**
  ভ্যারিয়েবল হলো নাম, যা কোনো মান/অবজেক্টকে রেফার করে। Python-এ ভ্যারিয়েবল টাইপ আগে থেকে ঘোষণা করতে হয় না (dynamic typing)।
* **Assignment (মান দেওয়া):** `name = "Alice"` মানে `name` নামটা `"Alice"` স্ট্রিং অবজেক্টকে রেফার করছে।
* **Name rule:** অক্ষর, সংখ্যা, আন্ডারস্কোর (`_`) ব্যবহার করা যায়; সংখ্যা দিয়ে শুরু করা যাবে না; কেস-সেন্সিটিভ।
* **Object model:** সবকিছু অবজেক্ট; ভ্যারিয়েবল শুধু রেফারেন্স। একই অবজেক্টে একাধিক নাম পয়েন্ট করতে পারে।
* **Mutability:** `int/float/str/tuple` ইমিউটেবল; `list/dict/set` মিউটেবল।
* **Scope:** লোকাল, গ্লোবাল, এনক্লোজিং (nonlocal), বিল্ট-ইন—LEGB রুল।
* **Lifecyle:** কোনো নাম শেষ স্কোপে না থাকলে/`del` করলে রেফারেন্স কমে যায়; গারবেজ কালেক্টর পরে মেমরি ফ্রি করে।
* **Typing aids:** টাইপ হিন্ট (PEP 484) কোড পড়া/টুলিংয়ে সাহায্য করে, রানটাইমে বাধ্যতামূলক না।
* **Best practice:** `UPPER_SNAKE_CASE` = কনস্ট্যান্ট কনভেনশন, তবে সত্যিকারের কনস্ট্যান্ট গ্যারান্টি করে না।

---

## ২০টি Example + Explanation

### 1) বেসিক অ্যাসাইনমেন্ট

```python
x = 10
y = "Python"
print(x, y)
```

**ব্যাখ্যা:** `x` ইন্টিজার অবজেক্ট 10 কে, `y` স্ট্রিং `"Python"` কে রেফার করছে।

---

### 2) এক লাইনে বহু অ্যাসাইনমেন্ট

```python
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
```

**ব্যাখ্যা:** ডানপাশের টিউপলটা আনপ্যাক হয়ে বামপাশের নামগুলোতে যায়।

---

### 3) ভ্যারিয়েবল swap (অস্থায়ী ভ্যারিয়েবল ছাড়াই)

```python
x, y = 5, 9
x, y = y, x
print(x, y)  # 9 5
```

**ব্যাখ্যা:** Python tuple packing/unpacking দিয়ে সহজে swap।

---

### 4) Augmented assignment

```python
count = 0
count += 1
print(count)  # 1
```

**ব্যাখ্যা:** `count = count + 1` এর সংক্ষিপ্ত রূপ।

---

### 5) ইমিউটেবল আচরণ (str)

```python
s = "Hi"
print(id(s))           # e.g. 140...
s += "!"
print(s, id(s))       # "Hi!" এবং ভিন্ন id
```

**ব্যাখ্যা:** স্ট্রিং ইমিউটেবল; `+=` নতুন স্ট্রিং অবজেক্ট তৈরি করে।

---

### 6) মিউটেবল আচরণ (list)

```python
nums = [1, 2]
print(id(nums))        # e.g. 140...
nums += [3]
print(nums, id(nums)) # [1,2,3] এবং সাধারণত একই id
```

**ব্যাখ্যা:** লিস্ট মিউটেবল; `+=` ইন-প্লেস পরিবর্তন করে।

---

### 7) Aliasing (একই অবজেক্টে একাধিক নাম)

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)  # [99, 2, 3]
```

**ব্যাখ্যা:** `a` ও `b` একই লিস্টকে রেফার করছে; এক জায়গার পরিবর্তন অন্যটাতে দেখা যায়।

---

### 8) কপি বনাম রেফারেন্স

```python
import copy
a = [[1, 2], [3, 4]]
b = a.copy()          # shallow copy
c = copy.deepcopy(a)  # deep copy
a[0][0] = 99
print(b)  # [[99, 2], [3, 4]]  -> inner shared
print(c)  # [[1, 2], [3, 4]]   -> fully independent
```

**ব্যাখ্যা:** শ্যালো কপিতে ভিতরের অবজেক্ট শেয়ার হয়; ডিপ কপি সম্পূর্ণ আলাদা কপি তৈরি করে।

---

### 9) `is` বনাম `==`

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True  (value equal)
print(x is y)  # False (different objects)
```

**ব্যাখ্যা:** `==` মান তুলনা; `is` অবজেক্ট আইডেন্টিটি তুলনা।

---

### 10) `id()` দিয়ে অবজেক্ট আইডি দেখা

```python
a = 256
b = 256
print(id(a), id(b), a is b)  # CPython small int caching এর কারণে True হতে পারে
```

**ব্যাখ্যা:** কিছু অবজেক্ট ইন্টার্ন/ক্যাশড থাকতে পারে; কিন্তু লজিকে `is` ধরে নেওয়া ঠিক না (শুধু আইডেন্টিটি দরকার হলে)।

---

### 11) Unpacking ও Starred Expressions

```python
first, *middle, last = [10, 20, 30, 40, 50]
print(first, middle, last)  # 10 [20, 30, 40] 50
```

**ব্যাখ্যা:** `*middle` বাকিটা লিস্ট আকারে ধরে।

---

### 12) Walrus operator (`:=`) – assign while using

```python
if (n := len("python")) > 3:
    print(n)  # 6
```

**ব্যাখ্যা:** এক্সপ্রেশন এর মধ্যেই ভ্যারিয়েবল অ্যাসাইন করা যায় (Python 3.8+)।

---

### 13) `global` কীওয়ার্ড (গ্লোবাল ভ্যারিয়েবল ব্যবহার)

```python
x = 10
def inc():
    global x
    x += 1

inc()
print(x)  # 11
```

**ব্যাখ্যা:** ফাংশনের ভিতরে গ্লোবাল নাম পরিবর্তন করতে `global` লাগবে।

---

### 14) `nonlocal` কীওয়ার্ড (ইনার-ফাংশন ও এনক্লোজিং স্কোপ)

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    return x

print(outer())  # 1
```

**ব্যাখ্যা:** `nonlocal` নিলে ইননার ফাংশন এনক্লোজিং স্কোপের `x` পরিবর্তন করতে পারে।

---

### 15) টাইপ হিন্ট (রানটাইমে বাধ্যতামূলক না)

```python
from typing import List

def total(xs: List[int]) -> int:
    return sum(xs)

print(total([1, 2, 3]))
```

**ব্যাখ্যা:** টাইপ হিন্ট টুলিং/রিডেবিলিটিতে সাহায্য করে; Python নিজে না মানলেও লিন্টার/IDE ধরতে পারে।

---

### 16) কনস্ট্যান্ট কনভেনশন

```python
PI = 3.14159
MAX_USERS = 100
```

**ব্যাখ্যা:** বড়হাতের নাম কনস্ট্যান্ট হিসেবে ব্যবহারের প্রচলন; টেকনিক্যালি পরিবর্তন করা সম্ভব, কিন্তু না করাই রীতি।

---

### 17) `None` ও truthiness

```python
result = None
if not result:
    print("No value yet")  # প্রিন্ট হবে
```

**ব্যাখ্যা:** `None`, `0`, `''`, `[]`, `{}` — এগুলো Falsey; বাকিগুলো Truthy।

---

### 18) `del` দিয়ে নাম মুছা

```python
x = 42
del x
# print(x)  # NameError: name 'x' is not defined
```

**ব্যাখ্যা:** `del` নামটাকে বর্তমান স্কোপ থেকে সরায়; অবজেক্ট রেফারেন্স 0 হলে পরে ফ্রি হয়।

---

### 19) Mutable default argument—পিটফল

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  <-- অপ্রত্যাশিত শেয়ারিং
```

**ব্যাখ্যা:** ডিফল্ট আর্গুমেন্ট শুধু একবার ইভ্যালুয়েট হয়; মিউটেবল হলে কলগুলোর মধ্যে শেয়ার হয়—বাগের উৎস।

**সঠিক প্যাটার্ন:**

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

---

### 20) Shadowing (উপরের নাম ঢেকে ফেলা)

```python
len = 5
# print(len([1,2,3]))  # TypeError: 'int' object is not callable
```

**ব্যাখ্যা:** বিল্ট-ইন ফাংশনের নামে ভ্যারিয়েবল দিলে আসল ফাংশনটা শ্যাডো হয়ে যায়। এমন নাম এড়িয়ে চলা উচিত; দরকার হলে `del len` করে ঠিক করা যায়।

---

## টিপস (Best Practices)

* অর্থবহ নাম দিন: `user_count`, `total_price`
* বিল্ট-ইন নাম (যেমন `list`, `dict`, `len`, `sum`) ভ্যারিয়েবল হিসেবে ব্যবহার করবেন না
* ইমিউটেবল বনাম মিউটেবল পার্থক্য বুঝে ব্যবহার করুন
* শেয়ারিং/কপি প্রয়োজন বুঝে `copy()`/`deepcopy()` নিন
* স্কোপ (local/global/nonlocal) সম্পর্কে পরিষ্কার থাকুন
* টাইপ হিন্ট যোগ করলে টিমে কাজ/বড় প্রজেক্টে লাভ হয়

---

