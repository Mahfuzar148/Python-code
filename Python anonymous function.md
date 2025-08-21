
---

# 🔹 Anonymous Function কী?

👉 Python-এ **Anonymous Function** হলো এমন ফাংশন যার **কোনো নাম থাকে না**।
এগুলোকে সাধারণত **lambda function** বলা হয়।

* সাধারণ ফাংশন বানাতে `def` ব্যবহার হয়।
* Anonymous function বানাতে `lambda` কীওয়ার্ড ব্যবহার হয়।

---

## 🔸 Syntax:

```python
lambda arguments : expression
```

* `lambda` → কীওয়ার্ড
* `arguments` → ইনপুট প্যারামিটার
* `expression` → এক লাইনের এক্সপ্রেশন, যেটি রিটার্ন ভ্যালু হয়

---

# 🔹 10 টি Example with Explanation

---

### 1) বেসিক ল্যাম্বডা

```python
f = lambda x: x + 10
print(f(5))  # 15
```

**ব্যাখ্যা:** `lambda x: x+10` একটি ফাংশন তৈরি করে, যেটি `x+10` ফেরত দেয়।

---

### 2) একাধিক আর্গুমেন্ট

```python
sum_two = lambda a, b: a + b
print(sum_two(3, 7))  # 10
```

**ব্যাখ্যা:** ল্যাম্বডা ফাংশনে একাধিক ইনপুট নেওয়া যায়।

---

### 3) ল্যাম্বডা সরাসরি কল

```python
print((lambda x, y: x*y)(5, 6))  # 30
```

**ব্যাখ্যা:** নাম ছাড়া ল্যাম্বডা ডিফাইন করে সরাসরি কল করা যায়।

---

### 4) Sort-এ ব্যবহার

```python
nums = [(1, 3), (2, 1), (4, 2)]
nums.sort(key=lambda x: x[1])
print(nums)  # [(2,1), (4,2), (1,3)]
```

**ব্যাখ্যা:** `key=lambda x: x[1]` → টিউপলের দ্বিতীয় উপাদান ধরে sort করে।

---

### 5) `map()` এর সাথে

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]
```

**ব্যাখ্যা:** `map` প্রতিটি উপাদানকে ল্যাম্বডা ফাংশনের মাধ্যমে ট্রান্সফর্ম করে।

---

### 6) `filter()` এর সাথে

```python
nums = [5, 8, 12, 15, 19]
evens = list(filter(lambda x: x%2==0, nums))
print(evens)  # [8, 12]
```

**ব্যাখ্যা:** `filter` কেবল শর্ত-সাপেক্ষ উপাদান রাখে।

---

### 7) `reduce()` এর সাথে

```python
from functools import reduce
nums = [1, 2, 3, 4]
prod = reduce(lambda x, y: x*y, nums)
print(prod)  # 24
```

**ব্যাখ্যা:** সব উপাদানকে একত্রিত করে এক ভ্যালু বানায়।

---

### 8) শর্তযুক্ত (ternary operator style)

```python
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # 20
```

**ব্যাখ্যা:** এক লাইনে `if-else` লজিকও দেওয়া যায়।

---

### 9) Dictionary sort

```python
students = {"Rahim": 80, "Karim": 95, "Salma": 70}
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
print(sorted_students)  # [('Karim', 95), ('Rahim', 80), ('Salma', 70)]
```

**ব্যাখ্যা:** ল্যাম্বডা ফাংশন দিয়ে dictionary value অনুযায়ী sort করা।

---

### 10) Function argument হিসেবে

```python
def apply_func(fn, value):
    return fn(value)

print(apply_func(lambda x: x**3, 4))  # 64
```

**ব্যাখ্যা:** ফাংশনের আর্গুমেন্ট হিসেবেও ল্যাম্বডা পাঠানো যায়।

---

# ✅ সারসংক্ষেপ

* **Anonymous Function / Lambda** → নামবিহীন ফাংশন।
* সাধারণত এক লাইনের এক্সপ্রেশন রাখতে হয়।
* **ব্যবহার:**

  * `map`, `filter`, `reduce`
  * sorting (`key` parameter)
  * ছোট temporary ফাংশন যেখানে নাম দরকার নেই



---

### 1) তালিকার প্রতিটি সংখ্যার স্কয়ার (map+lambda)

```python
nums = [1,2,3,4,5]
squares = list(map(lambda x: x*x, nums))
print(squares)  # [1, 4, 9, 16, 25]
```

ব্যাখ্যা: `map` প্রতিটি আইটেমে λ প্রয়োগ করে ট্রান্সফর্ম করে।

---

### 2) জোড় সংখ্যা ফিল্টার (filter+lambda)

```python
nums = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6, 8]
```

ব্যাখ্যা: `filter` শর্ত True এমন আইটেম রাখে।

---

### 3) স্কয়ারের যোগফল (reduce+lambda)

````python
from functools import reduce
nums = [1,2,3,4]
sum_sq = reduce(lambda acc, x: acc + x*x, nums, 0)
print(sum_sq)  # 30
``)
ব্যাখ্যা: `reduce` অ্যাকিউমুলেটর দিয়ে এক মানে নামায়।

---

### 4) টিউপল তালিকা দ্বিতীয় উপাদান ধরে sort
```python
pairs = [(1,3), (2,1), (4,2)]
pairs.sort(key=lambda t: t[1])
print(pairs)  # [(2,1), (4,2), (1,3)]
````

ব্যাখ্যা: `key` হিসেবে λ দিলে কাস্টম সোর্ট হয়।

---

### 5) সবচেয়ে লম্বা স্ট্রিং (max with key)

```python
words = ["cat","elephant","bee"]
longest = max(words, key=lambda s: len(s))
print(longest)  # elephant
```

ব্যাখ্যা: তুলনার ভিত্তি λ দিয়ে নির্ধারণ।

---

### 6) গ্রেডিং (map + λ ternary)

```python
marks = [35, 55, 80, 67]
grades = list(map(lambda m: "Fail" if m<40 else ("B" if m<70 else "A"), marks))
print(grades)  # ['Fail','B','A','B']
```

ব্যাখ্যা: λ-তে এক লাইনের `if-else`।

---

### 7) ইমেইল থেকে ডোমেইন

```python
emails = ["a@x.com","b@y.org","c@x.com"]
domains = list(map(lambda e: e.split("@")[1], emails))
print(domains)  # ['x.com','y.org','x.com']
```

ব্যাখ্যা: স্ট্রিং প্রসেসিংয়ে λ সহ `map`।

---

### 8) ডিকশনারি মান ধরে descending sort

```python
scores = {"A":88,"B":95,"C":70}
top = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
print(top)  # [('B',95), ('A',88), ('C',70)]
```

ব্যাখ্যা: `items()` + `key` λ দিয়ে value-সোর্ট।

---

### 9) শেষ অক্ষর ধরে স্ট্রিং sort

```python
names = ["mona","reza","amir","sofi"]
print(sorted(names, key=lambda s: s[-1]))
```

ব্যাখ্যা: `key` হিসেবে শেষ অক্ষর।

---

### 10) বয়স>১৮ এমন নামগুলো (filter+map)

```python
people = [{"name":"Rafi","age":17},{"name":"Toma","age":22},{"name":"Luna","age":19}]
adults = list(map(lambda p: p["name"], filter(lambda p: p["age"]>18, people)))
print(adults)  # ['Toma','Luna']
```

ব্যাখ্যা: আগে `filter`, পরে `map`—চেইনিং।

---

### 11) লিস্ট of লিস্ট ফ্ল্যাট (reduce)

```python
from functools import reduce
data = [[1,2],[3],[4,5]]
flat = reduce(lambda acc, x: acc + x, data, [])
print(flat)  # [1,2,3,4,5]
```

ব্যাখ্যা: লিস্ট কনক্যাট করে ফ্ল্যাট।

---

### 12) স্ট্রিং নাম্বার → int (invalid হলে None)

```python
raw = ["10","7","x","25"]
nums = list(map(lambda s: int(s) if s.isdigit() else None, raw))
print(nums)  # [10, 7, None, 25]
```

ব্যাখ্যা: কন্ডিশনাল কাস্টিং λ-তে।

---

### 13) প্যালিনড্রোম ফিল্টার

```python
words = ["madam","level","python","noon"]
pals = list(filter(lambda w: w == w[::-1], words))
print(pals)  # ['madam','level','noon']
```

ব্যাখ্যা: স্ট্রিং উল্টে মিলছে কিনা।

---

### 14) ভাওয়েল সংখ্যা ধরে সোর্ট

```python
def vowel_count(s): 
    return sum(1 for ch in s.lower() if ch in 'aeiou')

words = ["sky","idea","queue","beta"]
print(sorted(words, key=lambda s: vowel_count(s)))
```

ব্যাখ্যা: `key` λ থেকে অন্য ফাংশন কল।

---

### 15) কেস-ইনসেনসিটিভ ইউনিক নাম (reduce)

```python
from functools import reduce
names = ["Alice","alice","ALICE","Bob","bob"]
unique = reduce(
    lambda acc, n: acc + [n] if n.lower() not in {x.lower() for x in acc} else acc, 
    names, []
)
print(unique)  # ['Alice','Bob']
```

ব্যাখ্যা: কাস্টম ইউনিকনেস ক্রাইটেরিয়া।

---

### 16) রানিং সাম (reduce)

```python
from functools import reduce
nums = [1,2,3,4]
running = reduce(lambda acc, x: acc + [acc[-1] + x], nums[1:], [nums[0]])
print(running)  # [1, 3, 6, 10]
```

ব্যাখ্যা: পূর্বের যোগফল জমিয়ে লিস্ট বানানো।

---

### 17) সবচেয়ে ঘনঘন অক্ষর (λ key)

```python
s = "bananabandana"
most = max(set(s), key=lambda ch: s.count(ch))
print(most)
```

ব্যাখ্যা: `max` + `key` λ দিয়ে ফ্রিকোয়েন্সি ভিত্তিক নির্বাচন।

---

### 18) ডিকশনারির তালিকায় মিন/ম্যাক্স (key)

```python
students = [{"n":"A","m":72},{"n":"B","m":88},{"n":"C","m":64}]
topper = max(students, key=lambda d: d["m"])
print(topper)  # {'n': 'B', 'm': 88}
```

ব্যাখ্যা: জটিল অবজেক্টে `key` λ।

---

### 19) সেফ-ডিভাইড (০ হলে None)

```python
safe_div = lambda a, b: (a/b) if b else None
print(safe_div(10,2), safe_div(5,0))  # 5.0 None
```

ব্যাখ্যা: ছোট guard সহ λ।

---

### 20) ট্রান্সফর্ম পাইপলাইন (ফাংশন পাস)

```python
def apply(xs, fn): 
    return [fn(x) for x in xs]

print(apply([1,2,3], lambda x: x**3))  # [1, 8, 27]
```

ব্যাখ্যা: λ আর্গুমেন্ট হিসেবে পাস।

---

### 21) স্ট্রিং নরমালাইজ (strip/lower)

```python
raw = ["  Hello ","WORLD  ","  PyThOn"]
clean = list(map(lambda s: s.strip().lower(), raw))
print(clean)  # ['hello','world','python']
```

ব্যাখ্যা: স্ট্রিং চেইনড অপারেশন।

---

### 22) কাস্টম সোর্ট: বহু-কী (tuple key)

```python
records = [("A",2),("B",2),("A",1),("B",1)]
print(sorted(records, key=lambda t: (t[0], -t[1])))
# [('A', 2), ('A', 1), ('B', 2), ('B', 1)]
```

ব্যাখ্যা: `key` λ টিউপল রিটার্ন করে—মাল্টি-লেভেল sort।

---

### 23) লিস্ট → ডিকশনারি (ক্যালকুলেটেড ভ্যালু)

```python
nums = [1,2,3,4]
d = dict(map(lambda x: (x, x*x), nums))
print(d)  # {1: 1, 2: 4, 3: 9, 4: 16}
```

ব্যাখ্যা: `map`-এ (key, value) জোড়া জেনারেট।

---

### 24) গ্রুপিং কী (sorted + groupby)

```python
import itertools as it
words = sorted(["ant","apple","bat","ball","car"], key=lambda w: w[0])
for k, grp in it.groupby(words, key=lambda w: w[0]):
    print(k, list(grp))
```

ব্যাখ্যা: `groupby` কাজ করার আগে `sorted` দরকার—একই key ধারাবাহিক হয়।

---

### 25) কারিং-স্টাইল মেকার (λ রিটার্ন ফাংশন)

```python
make_adder = lambda n: (lambda x: x + n)
add5 = make_adder(5)
print(add5(10))  # 15
```

ব্যাখ্যা: λ থেকে আরেক λ রিটার্ন—ফাংশন ফ্যাক্টরি (ক্লোজার).

---

