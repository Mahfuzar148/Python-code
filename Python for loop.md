
---

# 🔹 For Loop—মূল ধারণা (খুব সংক্ষেপে)

* **Iterable**: যেগুলো থেকে একে একে আইটেম পাওয়া যায় — `list`, `tuple`, `str`, `dict`, `set`, `range`, file object, `itertools` ইত্যাদি।
* **Iterator protocol**: `iter(obj)` দিলে iterator পাওয়া যায়; `next(it)` করলে পরের আইটেম। `for` লুপ ভেতরে ভেতরে এটিই করে।
* **Loop control**: `break`, `continue`, এবং `for … else:` (লুপ **স্বাভাবিকভাবে শেষ হলে** `else` চলে; `break` হলে চলে না)।
* **সহায়ক টুল**: `range`, `enumerate`, `zip`, `reversed`, `sorted`, `dict.items()/keys()/values()`, `itertools` ইত্যাদি।
* **Comprehension**: লুপ-লজিক এক লাইনে—`[... for ... in ... if ...]` (ডেটা গড়ার জন্য; side-effect হলে সাধারণ `for` ভালো)।

---

# 🔹 ২৫টি ভিন্ন উদাহরণ + ব্যাখ্যা

### 1) বেসিক ইটারেশন (লিস্ট)

```python
nums = [10, 20, 30]
for n in nums:
    print(n)
```

**ব্যাখ্যা:** লিস্ট থেকে একে একে আইটেম নেয়।

---

### 2) `range()` দিয়ে সংখ্যার সিরিজ

```python
for i in range(1, 6):
    print(i)   # 1..5
```

**ব্যাখ্যা:** `range(start, stop)` — stop বাদ।

---

### 3) স্টেপসহ `range`

```python
for i in range(0, 10, 2):
    print(i)   # 0 2 4 6 8
```

**ব্যাখ্যা:** তৃতীয় আর্গুমেন্ট = step।

---

### 4) স্ট্রিং ইটারেশন

```python
for ch in "Python":
    print(ch)
```

**ব্যাখ্যা:** স্ট্রিংও iterable।

---

### 5) ডিকশনারি—keys (ডিফল্ট)

```python
user = {"name": "Rahim", "age": 20}
for k in user:
    print(k, user[k])
```

**ব্যাখ্যা:** ডিফল্টে `for` → keys ইটারেট করে।

---

### 6) ডিকশনারি—`items()` দিয়ে key+value

```python
for k, v in user.items():
    print(k, "=", v)
```

**ব্যাখ্যা:** টিউপল আনপ্যাক করে key, value আলাদা ভ্যারিয়েবলে পায়।

---

### 7) ডিকশনারি—`values()`

```python
for v in user.values():
    print(v)
```

**ব্যাখ্যা:** কেবল মানগুলোর উপর লুপ।

---

### 8) `enumerate()` দিয়ে ইনডেক্স + ভ্যালু

```python
fruits = ["apple", "banana", "mango"]
for i, f in enumerate(fruits, start=1):
    print(i, f)
```

**ব্যাখ্যা:** `start` দিয়ে ইনডেক্স শুরু বদলানো যায়।

---

### 9) `zip()` দিয়ে একাধিক সিকোয়েন্স একসাথে

```python
names = ["A", "B", "C"]
marks = [80, 75, 90]
for n, m in zip(names, marks):
    print(n, "=>", m)
```

**ব্যাখ্যা:** সবচেয়ে ছোট সিকোয়েন্স পর্যন্ত ইটারেট করে।


---

## 🔹 Example: 3টা list

```python
names = ["A", "B", "C"]
marks = [80, 75, 90]
grades = ["B+", "C", "A"]

for n, m, g in zip(names, marks, grades):
    print(n, "=>", m, "=>", g)
```

👉 Output:

```
A => 80 => B+
B => 75 => C
C => 90 => A
```

---

## 🔹 Example: 4টা list

```python
names = ["A", "B", "C"]
marks = [80, 75, 90]
grades = ["B+", "C", "A"]
roll = [101, 102, 103]

for n, m, g, r in zip(names, marks, grades, roll):
    print(r, "-", n, "=>", m, "=>", g)
```

👉 Output:

```
101 - A => 80 => B+
102 - B => 75 => C
103 - C => 90 => A
```

---

## 🔹 Important Note

* `zip()` সবচেয়ে **ছোট list** পর্যন্ত iterate করে, extra elements বাদ যাবে।

```python
a = [1, 2, 3]
b = [10, 20]
c = [100, 200, 300, 400]

for x, y, z in zip(a, b, c):
    print(x, y, z)
```

👉 Output:

```
1 10 100
2 20 200
```

(কারণ সবচেয়ে ছোট `b` এর size = 2)

---

## ✅ সারসংক্ষেপ

* `zip()` দিয়ে **২, ৩, ৪ বা তার বেশি list একসাথে iterate করা যায়**।
* কিন্তু iteration সবসময় **shortest list** এর length অনুযায়ী চলবে।
* চাইলে `itertools.zip_longest()` ব্যবহার করে extra elements বাদ না দিয়ে **fillvalue** সহ রাখতে পারো।

---




---

### 10) `reversed()` দিয়ে উল্টো ইটারেশন

```python
nums = [1, 2, 3, 4]
for x in reversed(nums):
    print(x)   # 4 3 2 1
```

**ব্যাখ্যা:** কপি না করেই উল্টোদিকে ইটারেট।

---

### 11) `sorted()` দিয়ে সাজিয়ে ইটারেশন

```python
langs = {"python", "go", "rust"}  # set unordered
for s in sorted(langs):
    print(s)
```

**ব্যাখ্যা:** `set`-কে সাজিয়ে ডিটারমিনিস্টিক অর্ডারে লুপ।

---

### 12) `for … else` ব্যবহার

```python
nums = [2, 4, 6, 8]
for x in nums:
    if x % 2 == 1:
        print("Found odd")
        break
else:
    print("No odd found")  # চলবে (break হয়নি)
```

**ব্যাখ্যা:** `break` না হলে `else` ব্লক চালে।

---

### 13) `break` ও `continue`

```python
for i in range(1, 6):
    if i == 3:
        continue  # 3 স্কিপ
    if i == 5:
        break     # 5 এ থামো
    print(i)      # 1,2,4
```

**ব্যাখ্যা:** `continue` ইটারেশনের বাকি অংশ স্কিপ; `break` লুপ থামায়।

---

### 14) Nested loops (টেবিল/ম্যাট্রিক্স)

```python
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i*j)
    print(row)
```

**ব্যাখ্যা:** ভিতরে ভিতরে লুপ চালানো।

---

### 15) আনপ্যাকিং ইন লoop (টিউপল/পেয়ার)

```python
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, ch in pairs:
    print(num, ch)
```

**ব্যাখ্যা:** টিউপল পেয়ে সরাসরি ভ্যারিয়েবলে ভাগ করে নেয়।

---

### 16) ফাইলে লাইন ধরে ইটারেশন

```python
# with open("data.txt") as f:
#     for line in f:
#         print(line.strip())
```

**ব্যাখ্যা:** ফাইল অবজেক্ট iterable; লাইনে লাইনে পড়ে (কমেন্ট খুলে চালাতে হবে)।

---

### 17) লিস্ট কপি করে ইটারেট (মডিফাই-টাইম সেফটি)

```python
items = [1, 2, 3, 4]
for x in items[:]:    # কপি স্লাইস
    if x % 2 == 0:
        items.remove(x)
print(items)  # [1, 3]
```

**ব্যাখ্যা:** মূল লিস্টে পরিবর্তন দরকার হলে কপি/সেফ স্ট্র্যাটেজি ব্যবহার করুন।

---

### 18) কমপ্রিহেনশন সমতুল্য for (শিক্ষণীয় তুলনা)

```python
# comprehension
squares = [x*x for x in range(5)]

# সমান কাজ for লুপে
squares2 = []
for x in range(5):
    squares2.append(x*x)
```

**ব্যাখ্যা:** comprehension ডেটা তৈরি করতে সংক্ষিপ্ত; side-effect থাকলে সাধারণ `for` ভালো।

---

### 19) `itertools.product` (কার্টেসিয়ান প্রডাক্ট)

```python
import itertools as it
for a, b in it.product([1, 2], ["x", "y"]):
    print(a, b)
```

**ব্যাখ্যা:** সব কম্বিনেশন জেনারেট করে: (1,x), (1,y), (2,x), (2,y)।

---

### 20) `itertools.permutations`

```python
import itertools as it
for p in it.permutations([1, 2, 3], r=2):
    print(p)   # (1,2) (1,3) (2,1) ...
```

**ব্যাখ্যা:** ক্রমানুসার-সংবেদী ২-দৈর্ঘ্যের পারমুটেশন।

---

### 21) `itertools.combinations`

```python
import itertools as it
for c in it.combinations([1, 2, 3], r=2):
    print(c)   # (1,2) (1,3) (2,3)
```

**ব্যাখ্যা:** ক্রমানুসার-অসংবেদী কম্বিনেশন (পুনরাবৃত্তি ছাড়া)।

---

### 22) `itertools.groupby` (সাজানো ডেটা গ্রুপ)

```python
import itertools as it
data = sorted("aaabbccdddbb")
for key, group in it.groupby(data):
    print(key, len(list(group)))
```

**ব্যাখ্যা:** ধারাবাহিক সমান আইটেম গ্রুপ করে—সাজানো ডেটা ধরেই কাজ ভালো হয়।

---

### 23) কাস্টম iterable (নিজস্ব `__iter__`)

```python
class CountDown:
    def __init__(self, n): self.n = n
    def __iter__(self):
        x = self.n
        while x > 0:
            yield x
            x -= 1

for v in CountDown(3):
    print(v)  # 3 2 1
```

**ব্যাখ্যা:** জেনারেটর `yield` দিয়ে নিজস্ব iterable বানানো।

---

### 24) একাধিক শর্ত সহ লুপ ফিল্টার

```python
nums = range(1, 21)
for x in nums:
    if x % 2 == 0 and x % 3 == 0:
        print(x)  # 6, 12, 18
```

**ব্যাখ্যা:** `and`/`or` দিয়ে শর্ত মিলিয়ে ফিল্টার।

---

### 25) Early-exit সার্চ + for-else প্যাটার্ন

```python
target = 29
for n in range(2, target):
    if target % n == 0:
        print("Composite")
        break
else:
    print("Prime")   # break না হলে এটিই চলবে
```

**ব্যাখ্যা:** সার্চে না-পেলে `else` চলবে—প্রাইম চেকের ক্লাসিক প্যাটার্ন।

---

## ✅ সংক্ষিপ্ত টিপস

* লুপে **ইনডেক্স দরকার**? → `enumerate`
* **একসাথে বহু সিকোয়েন্স**? → `zip`
* **অর্ডার দরকার**? → `sorted` / `reversed`
* **ডিকশনারি**? → `items()/keys()/values()`
* **বড় কম্বিনেটরিক্স**? → `itertools`
* **লুপ শেষের পর অ্যাকশন**? → `for … else`
* **লুপ চলাকালীন কালেকশন বদলাতে হলে** কপি নিয়ে কাজ করুন

---

