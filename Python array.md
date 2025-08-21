
---

## 🔹 Python Array Functions / Methods List

(Python এর `array` module থেকে পাওয়া যায়)

1. **append(x)** → array-তে নতুন আইটেম যোগ করে
2. **extend(iterable)** → একসাথে একাধিক আইটেম যোগ করে
3. **insert(i, x)** → নির্দিষ্ট index-এ item যোগ করে
4. **remove(x)** → প্রথম যে item টা মিলে, সেটাকে মুছে ফেলে
5. **pop(\[i])** → index দিয়ে item মুছে ফেলে, default এ শেষ item
6. **index(x)** → কোনো item প্রথম কোথায় আছে index রিটার্ন করে
7. **count(x)** → কোনো item কয়বার আছে সেটা রিটার্ন করে
8. **reverse()** → পুরো array উল্টে দেয়
9. **sort()** → array কে ascending order এ সাজায়
10. **buffer\_info()** → array এর memory ঠিকানা ও length দেয়
11. **typecode** → array-র data type code (যেমন 'i', 'f')
12. **itemsize** → প্রতিটি item কয় byte ব্যবহার করছে সেটা বলে
13. **tolist()** → array কে list এ রূপান্তর করে
14. **fromlist(list)** → list থেকে array বানায়
15. **tobytes()** → array কে bytes এ রূপান্তর করে
16. **frombytes(bytes)** → bytes থেকে array বানায়

---

## 🔹 এখন প্রতিটার Example + ব্যাখ্যা

### 1) append(x)

```python
import array as arr

numbers = arr.array('i', [1, 2, 3])
numbers.append(4)
print(numbers)   # array('i', [1, 2, 3, 4])
```

👉 শেষে নতুন item যোগ হলো।

---

### 2) extend(iterable)

```python
nums = arr.array('i', [1, 2])
nums.extend([3, 4, 5])
print(nums)   # array('i', [1, 2, 3, 4, 5])
```

👉 একসাথে একাধিক element add হলো।

---

### 3) insert(i, x)

```python
nums = arr.array('i', [1, 3, 4])
nums.insert(1, 2)
print(nums)   # array('i', [1, 2, 3, 4])
```

👉 index `1` এ মান ঢুকল।

---

### 4) remove(x)

```python
nums = arr.array('i', [1, 2, 3, 2])
nums.remove(2)
print(nums)   # array('i', [1, 3, 2])
```

👉 প্রথম 2 মুছে গেল।

---

### 5) pop(\[i])

```python
nums = arr.array('i', [10, 20, 30])
nums.pop(1)
print(nums)   # array('i', [10, 30])
```

👉 index `1` এর মান delete হলো।

---

### 6) index(x)

```python
nums = arr.array('i', [5, 10, 15, 10])
print(nums.index(10))   # 1
```

👉 প্রথমবার 10 index `1` এ আছে।

---

### 7) count(x)

```python
nums = arr.array('i', [2, 2, 3, 4, 2])
print(nums.count(2))   # 3
```

👉 2 মোট ৩ বার আছে।

---

### 8) reverse()

```python
nums = arr.array('i', [1, 2, 3])
nums.reverse()
print(nums)   # array('i', [3, 2, 1])
```

👉 পুরো array উল্টে গেল।

---

### 9) sort() → **Note:** array module-এ নেই, list-এ আছে। array sort করতে চাইলে আগে list বানাতে হয়।

```python
nums = arr.array('i', [5, 1, 3])
nums = arr.array('i', sorted(nums))
print(nums)   # array('i', [1, 3, 5])
```

👉 sorted() দিয়ে sort করলাম।

---

### 10) buffer\_info()

```python
nums = arr.array('i', [1, 2, 3])
print(nums.buffer_info())  
# (মেমোরি ঠিকানা, length)
```

👉 array কোথায় আছে (address) ও কয়টা element আছে, সেটা দেয়।

---

### 11) typecode

```python
nums = arr.array('i', [1, 2, 3])
print(nums.typecode)   # i
```

👉 integer টাইপ array।

---

### 12) itemsize

```python
nums = arr.array('i', [1, 2, 3])
print(nums.itemsize)   # 4
```

👉 প্রতিটি int 4 byte।

---

### 13) tolist()

```python
nums = arr.array('i', [1, 2, 3])
lst = nums.tolist()
print(lst)   # [1, 2, 3]
```

👉 array → list।

---

### 14) fromlist(list)

```python
nums = arr.array('i', [])
nums.fromlist([10, 20, 30])
print(nums)   # array('i', [10, 20, 30])
```

👉 list → array।

---

### 15) tobytes()

```python
nums = arr.array('i', [1, 2])
b = nums.tobytes()
print(b)
```

👉 array কে raw bytes বানিয়ে দিল।

---

### 16) frombytes(bytes)

```python
nums = arr.array('i')
b = arr.array('i', [1, 2, 3]).tobytes()
nums.frombytes(b)
print(nums)   # array('i', [1, 2, 3])
```

👉 bytes থেকে আবার array তৈরি হলো।

---

# 🔹 Python Arrays – Topics with Examples

---

## 1) Python - Arrays

```python
import array as arr
nums = arr.array('i', [1, 2, 3, 4])
print(nums)   # array('i', [1, 2, 3, 4])
```

👉 এখানে `'i'` মানে integer array।

---

## 2) Access Array Items

```python
nums = arr.array('i', [10, 20, 30])
print(nums[0])   # 10
print(nums[-1])  # 30
```

👉 index ব্যবহার করে element access করা যায়।

---

## 3) Add Array Items

```python
nums = arr.array('i', [1, 2])
nums.append(3)   # একক item যোগ
nums.extend([4, 5])  # একাধিক যোগ
print(nums)   # array('i', [1, 2, 3, 4, 5])
```

---

## 4) Remove Array Items

```python
nums = arr.array('i', [1, 2, 3, 2])
nums.remove(2)   # প্রথম 2 মুছে যাবে
nums.pop()       # শেষ element মুছে যাবে
print(nums)      # array('i', [1, 3])
```

---

## 5) Loop Arrays

```python
nums = arr.array('i', [1, 2, 3])
for x in nums:
    print(x)
```

👉 for loop দিয়ে সব element traverse করা যায়।

---

## 6) Copy Arrays

```python
nums = arr.array('i', [1, 2, 3])
copy_nums = nums[:]
print(copy_nums)   # array('i', [1, 2, 3])
```

👉 slicing করে shallow copy করা যায়।

---

## 7) Reverse Arrays

```python
nums = arr.array('i', [1, 2, 3])
nums.reverse()
print(nums)   # array('i', [3, 2, 1])
```

---

## 8) Sort Arrays

array module-এ সরাসরি `sort()` নেই, তাই list-এ কনভার্ট করতে হয়:

```python
nums = arr.array('i', [5, 2, 8, 1])
nums = arr.array('i', sorted(nums))
print(nums)   # array('i', [1, 2, 5, 8])
```

---

## 9) Join Arrays

```python
a1 = arr.array('i', [1, 2])
a2 = arr.array('i', [3, 4])
a3 = arr.array('i', a1.tolist() + a2.tolist())
print(a3)   # array('i', [1, 2, 3, 4])
```

👉 দুই array join করার জন্য list এ convert করে যোগ করা হয়।

---

## 10) Array Methods

আগেই আলোচনা করা হয়েছিলো — `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `reverse()`, `tolist()`, `fromlist()`, `tobytes()`, `frombytes()` ইত্যাদি।

---



---

# 📌 Array Slicing in Python

### ✅ Basic Syntax

```python
array[start : stop : step]
```

* **start** → কোন index থেকে শুরু করবে (default = `0`)
* **stop** → কোন index পর্যন্ত যাবে (exclusive অর্থাৎ stop index এর আগে পর্যন্ত নেবে)
* **step** → কয় ধাপে যাবে (default = `1`)

👉 `arr[start:stop:step]` সবসময় একটা **নতুন array** return করে।

---

## 🔹 Examples

### 1) Simple slicing

```python
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
print(a[1:4])     # array('i', [20, 30, 40])
```

**ব্যাখ্যা**: index 1 থেকে 4 এর আগ পর্যন্ত → `20, 30, 40`

---

### 2) Omit start

```python
print(a[:3])      # array('i', [10, 20, 30])
```

**ব্যাখ্যা**: শুরুর থেকে index 3 এর আগে পর্যন্ত।

---

### 3) Omit stop

```python
print(a[2:])      # array('i', [30, 40, 50])
```

**ব্যাখ্যা**: index 2 থেকে শেষ পর্যন্ত।

---

### 4) Omit both (copy)

```python
b = a[:]          # shallow copy
print(b)          # array('i', [10, 20, 30, 40, 50])
```

---

### 5) Negative index

```python
print(a[-3:])     # array('i', [30, 40, 50])
print(a[:-2])     # array('i', [10, 20, 30])
```

**ব্যাখ্যা**: -3 মানে শেষ থেকে তৃতীয়, -2 মানে শেষ থেকে দ্বিতীয় পর্যন্ত না নেওয়া।

---

### 6) Step usage

```python
print(a[::2])     # array('i', [10, 30, 50])
print(a[1::2])    # array('i', [20, 40])
```

**ব্যাখ্যা**: `::2` মানে প্রতি ২ ধাপে একবার করে নেবে।

---

### 7) Negative step (reverse)

```python
print(a[::-1])    # array('i', [50, 40, 30, 20, 10])
print(a[4:1:-1])  # array('i', [50, 40, 30])
```

**ব্যাখ্যা**: -1 মানে উল্টো দিকে পড়বে।

---

### 8) Replace slice

```python
a[1:3] = arr.array('i', [200, 300])
print(a)          # array('i', [10, 200, 300, 40, 50])
```

**ব্যাখ্যা**: index 1 থেকে 2 পর্যন্ত replace হলো নতুন value দিয়ে।

---

### 9) Delete slice

```python
del a[1:3]
print(a)          # array('i', [10, 40, 50])
```

---

### 10) Copy with step > 1

```python
x = arr.array('i', range(1,11))  # 1-10
print(x[1:9:3])   # array('i', [2, 5, 8])
```

**ব্যাখ্যা**: index 1 → 9 এর আগে পর্যন্ত, step 3 এ নেয়া → 2, 5, 8

---

## ⚡ Key Points (মনে রাখার জন্য)

1. Slicing সবসময় **নতুন array** তৈরি করে (original অপরিবর্তিত, যদি না replace করো)।
2. Negative index মানে → শেষ থেকে গোনা।
3. Step positive হলে → বামে থেকে ডানে, Negative হলে → ডানে থেকে বামে।
4. Start বাদ দিলে → 0 থেকে শুরু, Stop বাদ দিলে → শেষ পর্যন্ত, Step বাদ দিলে → 1।

---



## 11) Array Exercises (Practice Problems)

এখন তোমার জন্য 10টি প্র্যাকটিস প্রবলেম দিলাম:

1. একটি array বানাও এবং প্রথম ও শেষ element print করো।
2. একটি array-তে user input থেকে ৫টি সংখ্যা যোগ করে print করো।
3. array থেকে সব even সংখ্যাকে filter করে print করো।
4. একটি array reverse করে print করো (reverse() ব্যবহার না করে slicing দিয়ে)।
5. array-এর সব element-এর যোগফল বের করো।
6. দুইটি array join করে নতুন array বানাও।
7. একটি array sort করো descending order-এ।
8. array থেকে duplicate elements remove করো।
9. array থেকে একটি নির্দিষ্ট মান কয়বার আছে তা গণনা করো।
10. একটি array copy করো এবং দুইটাকে আলাদা প্রিন্ট করো।

---



> শুরুতে মনে রাখো:

```python
import array as arr
```

---

## 30 Practice Problems (with solutions)

### 1) প্রথম ও শেষ আইটেম প্রিন্ট

```python
import array as arr
a = arr.array('i', [3, 6, 9, 12])
print(a[0], a[-1])        # 3 12
```

ব্যাখ্যা: পজিটিভ/নেগেটিভ index দিয়ে element ধরা।

---

### 2) অ্যারে’তে ৫টি ইনপুট যোগ করা

```python
a = arr.array('i', [])
for _ in range(5):
    a.append(int(input()))
print(a)
```

ব্যাখ্যা: `append()` দিয়ে একে একে যোগ।

---

### 3) জোড় সংখ্যা ফিল্টার

```python
a = arr.array('i', [1,2,3,4,5,6])
even = arr.array('i', [x for x in a if x % 2 == 0])
print(even)                     # array('i', [2, 4, 6])
```

ব্যাখ্যা: comprehension থেকে নতুন `array('i', …)`।

---

### 4) reverse() ছাড়া উল্টানো (slicing)

```python
a = arr.array('i', [1,2,3,4])
rev = arr.array('i', a[::-1])
print(rev)                      # array('i', [4,3,2,1])
```

ব্যাখ্যা: `[::-1]` স্লাইস রিভার্স কপি দেয়।

---

### 5) সব উপাদানের যোগফল

```python
a = arr.array('i', [5,10,15])
print(sum(a))                   # 30
```

ব্যাখ্যা: `sum` ইটারেবল থেকে যোগফল নেয়।

---

### 6) সর্বোচ্চ/সর্বনিম্ন

```python
a = arr.array('i', [8,1,9,3])
print(max(a), min(a))           # 9 1
```

ব্যাখ্যা: `max/min` সরাসরি কাজ করে।

---

### 7) দুটি array join করা

```python
a1 = arr.array('i', [1,2])
a2 = arr.array('i', [3,4])
a3 = arr.array('i', a1.tolist() + a2.tolist())
print(a3)                       # array('i',[1,2,3,4])
```

ব্যাখ্যা: list-এ কনভার্ট করে কনক্যাট, পরে array বানালাম।

---

### 8) ডুপ্লিকেট রিমুভ (অর্ডার রাখা)

```python
a = arr.array('i', [1,2,2,3,1,4,3])
seen, out = set(), []
for x in a:
    if x not in seen:
        seen.add(x); out.append(x)
a = arr.array('i', out)
print(a)                        # array('i',[1,2,3,4])
```

ব্যাখ্যা: সেট দিয়ে দেখা-নামা ট্র্যাক।

---

### 9) নির্দিষ্ট মান কয়বার আছে

```python
a = arr.array('i', [2,2,3,4,2])
print(a.count(2))               # 3
```

ব্যাখ্যা: `count(x)` বিল্ট-ইন মেথড।

---

### 10) copy (shallow)

```python
a = arr.array('i', [7,8,9])
b = a[:]        # বা arr.array('i', a)
b.append(10)
print(a, b)     # a অপরিবর্তিত, b-তে নতুন
```

ব্যাখ্যা: স্লাইস কপি নতুন অবজেক্ট।

---

### 11) insert দিয়ে index-এ যোগ

```python
a = arr.array('i', [1,3,4])
a.insert(1, 2)
print(a)                        # array('i',[1,2,3,4])
```

ব্যাখ্যা: `insert(i, x)` নির্দিষ্ট স্থানে ঢোকে।

---

### 12) remove vs pop

```python
a = arr.array('i', [1,2,3,2])
a.remove(2)     # প্রথম 2 যাবে
last = a.pop()  # শেষ এলিমেন্ট যাবে
print(a, last)  # array('i',[1,3,2]) 2
```

ব্যাখ্যা: `remove(x)` মান-ভিত্তিক; `pop([i])` index-ভিত্তিক।

---

### 13) index খোঁজা (না পেলে ValueError)

```python
a = arr.array('i', [5,10,15,10])
print(a.index(10))              # 1
```

ব্যাখ্যা: প্রথম occurrence এর index।

---

### 14) reverse() ব্যবহার

```python
a = arr.array('i', [1,2,3])
a.reverse()
print(a)                        # array('i',[3,2,1])
```

ব্যাখ্যা: ইন-প্লেস রিভার্স।

---

### 15) sort করা (array-এ সরাসরি নেই)

```python
a = arr.array('i', [5,1,8,3])
a = arr.array('i', sorted(a))   # ascending
print(a)                        # array('i',[1,3,5,8])
```

ব্যাখ্যা: `sorted()` → list → array।

---

### 16) descending sort

```python
a = arr.array('i', [5,1,8,3])
a = arr.array('i', sorted(a, reverse=True))
print(a)                        # array('i',[8,5,3,1])
```

ব্যাখ্যা: `reverse=True`।

---

### 17) buffer\_info, typecode, itemsize

```python
a = arr.array('i', [1,2,3])
print(a.buffer_info())  # (address, length)
print(a.typecode)       # 'i'
print(a.itemsize)       # 4 (bytes per item)
```

ব্যাখ্যা: নিম্নস্তরের মেটাডাটা।

---

### 18) tolist / fromlist

```python
a = arr.array('i', [1,2,3])
lst = a.tolist()
b = arr.array('i', [])
b.fromlist([4,5])
print(lst, b)           # [1,2,3] array('i',[4,5])
```

ব্যাখ্যা: list ↔ array রূপান্তর।

---

### 19) tobytes / frombytes

```python
a = arr.array('i', [10,20,30])
bts = a.tobytes()
c = arr.array('i')
c.frombytes(bts)
print(c)                 # array('i',[10,20,30])
```

ব্যাখ্যা: সিরিয়ালাইজ/ডিসিরিয়ালাইজ।

---

### 20) স্লাইস রিপ্লেসমেন্ট (একাধিক বদল)

```python
a = arr.array('i', [1,2,3,4,5])
a[1:4] = arr.array('i', [20,30,40])
print(a)                # array('i',[1,20,30,40,5])
```

ব্যাখ্যা: স্লাইসে array-ই দিতে হবে টাইপ মিলিয়ে।

---

### 21) নির্দিষ্ট রেঞ্জ ডিলিট (slice delete)

```python
a = arr.array('i', [10,20,30,40,50])
del a[1:4]
print(a)                # array('i',[10,50])
```

ব্যাখ্যা: `del` স্লাইসে কাজ করে।

---

### 22) Step স্লাইস

```python
a = arr.array('i', [1,2,3,4,5,6,7,8])
print(a[::2])           # array('i',[1,3,5,7])
```

ব্যাখ্যা: `start:stop:step`।

---

### 23) শর্তসাপেক্ষ multiple replace

```python
a = arr.array('i', [1,2,3,4,5,6])
a = arr.array('i', [99 if x%2==0 else x for x in a])
print(a)                # even → 99
```

ব্যাখ্যা: comprehension দিয়ে ট্রান্সফর্ম।

---

### 24) দুটি array মার্জ করে sort (unique)

```python
a = arr.array('i', [3,1,2,2])
b = arr.array('i', [2,4,3])
merged = list(set(a.tolist() + b.tolist()))
merged.sort()
a = arr.array('i', merged)
print(a)                # array('i',[1,2,3,4])
```

ব্যাখ্যা: সেটে ডুপ্লিকেট কাটে, তারপর sort।

---

### 25) rotate right by k (স্লাইস ট্রিক)

```python
a = arr.array('i', [1,2,3,4,5])
k = 2
n = len(a)
a = arr.array('i', a[-k:] + a[:n-k])
print(a)                # array('i',[4,5,1,2,3])
```

ব্যাখ্যা: রিয়ার অংশ সামনে বসাও।

---

### 26) find all indexes of a value

```python
a = arr.array('i', [1,2,3,2,4,2])
indexes = [i for i,x in enumerate(a) if x==2]
print(indexes)          # [1, 3, 5]
```

ব্যাখ্যা: `enumerate` দিয়ে স্ক্যান।

---

### 27) pairwise sum (দুই array)

```python
a = arr.array('i', [1,2,3])
b = arr.array('i', [4,5,6])
c = arr.array('i', [x+y for x,y in zip(a,b)])
print(c)                # array('i',[5,7,9])
```

ব্যাখ্যা: `zip` দিয়ে সমান্তরাল যোগ।

---

### 28) remove all occurrences of x

```python
a = arr.array('i', [2,1,2,3,2,4])
x = 2
a = arr.array('i', [v for v in a if v!=x])
print(a)                # array('i',[1,3,4])
```

ব্যাখ্যা: কমপ্রিহেনশন ফিল্টার।

---

### 29) chunk into fixed size

```python
a = arr.array('i', range(1,11))
k = 3
chunks = [arr.array('i', a[i:i+k]) for i in range(0, len(a), k)]
for ch in chunks: print(ch)
```

ব্যাখ্যা: স্টেপ দিয়ে স্লাইস স্লাইস ভাগ করা।

---

### 30) running average (window 3)

```python
a = arr.array('f', [1,2,3,4,5])
win = 3
avg = [(a[i:i+win]).tolist() and sum(a[i:i+win])/win
       for i in range(0, len(a)-win+1)]
print(avg)              # [2.0, 3.0, 4.0]
```

ব্যাখ্যা: স্লাইস উইন্ডো নিয়ে গড়।

---

## ছোট টিপস

* সবসময় **typecode** ঠিক রাখো: `'i'` (int), `'f'` (float) ইত্যাদি; দুই array যোগ/স্লাইস-রিপ্লেসে typecode মিলতে হবে।
* `array` তে `sort()` নেই—`sorted()`→list→array প্যাটার্ন ব্যবহার করো।
* বাইনারি সিরিয়ালাইজ দরকার হলে `tobytes()/frombytes()` দারুণ কাজে লাগে।

---

