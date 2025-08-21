
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

