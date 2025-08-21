
---

# 🔹 Python Operators (থিওরি)

Python এ অপারেটর হলো বিশেষ চিহ্ন যা **ভ্যালু বা ভ্যারিয়েবল** এর উপর নির্দিষ্ট কাজ করে।

### অপারেটরের ধরন

1. **Arithmetic Operators** → `+ - * / % // **`
2. **Comparison (Relational) Operators** → `== != > < >= <=`
3. **Logical Operators** → `and or not`
4. **Bitwise Operators** → `& | ^ ~ << >>`
5. **Assignment Operators** → `= += -= *= /= %= //= **=`
6. **Membership Operators** → `in`, `not in`
7. **Identity Operators** → `is`, `is not`

---

# 🔹 ২০টি Example with Explanation

---

### 1) Addition (`+`)

```python
a, b = 10, 5
print(a + b)  # 15
```

**ব্যাখ্যা:** দুইটা সংখ্যা যোগ করে।

---

### 2) Subtraction (`-`)

```python
print(a - b)  # 5
```

**ব্যাখ্যা:** দুইটা সংখ্যার বিয়োগফল বের করে।

---

### 3) Multiplication (`*`)

```python
print(a * b)  # 50
```

**ব্যাখ্যা:** গুণফল বের করে।

---

### 4) Division (`/`)

```python
print(a / b)  # 2.0
```

**ব্যাখ্যা:** ভাগ করলে সর্বদা float রিটার্ন করে।

---

### 5) Floor Division (`//`)

```python
print(10 // 3)  # 3
```

**ব্যাখ্যা:** ভাগফল ইন্টিজার আকারে দেয় (দশমিক বাদ দেয়)।

---

### 6) Modulus (`%`)

```python
print(10 % 3)  # 1
```

**ব্যাখ্যা:** ভাগশেষ দেয়।

---

### 7) Exponentiation (`**`)

```python
print(2 ** 3)  # 8
```

**ব্যাখ্যা:** ঘাত নির্ণয় করে (2³)।

---

### 8) Equal (`==`)

```python
print(5 == 5)  # True
```

**ব্যাখ্যা:** দুই ভ্যালু সমান হলে True।

---

### 9) Not Equal (`!=`)

```python
print(5 != 3)  # True
```

**ব্যাখ্যা:** সমান না হলে True।

---

### 10) Greater / Less

```python
print(7 > 3)   # True
print(3 < 7)   # True
```

**ব্যাখ্যা:** তুলনা অপারেটর ব্যবহার করে।

---

### 11) Greater/Equal, Less/Equal

```python
print(5 >= 5)  # True
print(4 <= 6)  # True
```

**ব্যাখ্যা:** সমান বা বড়/ছোট চেক করে।

---

### 12) Logical AND

```python
print(True and False)  # False
```

**ব্যাখ্যা:** দুই পাশেই True হলে শুধু True।

---

### 13) Logical OR

```python
print(True or False)  # True
```

**ব্যাখ্যা:** যেকোনো একটা True হলেই True।

---

### 14) Logical NOT

```python
print(not True)  # False
```

**ব্যাখ্যা:** মান উল্টে দেয়।

---

### 15) Bitwise AND

```python
print(5 & 3)  # 1
```

**ব্যাখ্যা:** বাইনারি AND করে (0101 & 0011 = 0001)।

---

### 16) Bitwise OR

```python
print(5 | 3)  # 7
```

**ব্যাখ্যা:** বাইনারি OR (0101 | 0011 = 0111)।

---

### 17) Bitwise XOR

```python
print(5 ^ 3)  # 6
```

**ব্যাখ্যা:** বাইনারি XOR (ভিন্ন হলে 1)।

---

### 18) Bitwise Shift

```python
print(5 << 1)  # 10  (shift left)
print(5 >> 1)  # 2   (shift right)
```

**ব্যাখ্যা:** bit গুলোকে বামে/ডানে সরায়।

---

### 19) Membership Operator

```python
fruits = ["apple", "banana"]
print("apple" in fruits)     # True
print("mango" not in fruits) # True
```

**ব্যাখ্যা:** কোনো ভ্যালু লিস্ট/সেটে আছে কিনা চেক করে।

---

### 20) Identity Operator

```python
x = [1,2,3]
y = [1,2,3]
z = x
print(x is y)     # False (ভিন্ন অবজেক্ট)
print(x is z)     # True  (একই অবজেক্ট)
```

**ব্যাখ্যা:** `is` অবজেক্ট আইডেন্টিটি (memory address) চেক করে।

---



---

### 1) Bitwise AND (`&`)

```python
a, b = 5, 3   # 5 = 0101, 3 = 0011
print(a & b)  # 1 (0001)
```

**ব্যাখ্যা:** দুই বিটই `1` হলে `1`, নাহলে `0`।

---

### 2) Bitwise OR (`|`)

```python
a, b = 5, 3   # 0101 | 0011
print(a | b)  # 7 (0111)
```

**ব্যাখ্যা:** যেকোনো এক বিট `1` হলে `1`।

---

### 3) Bitwise XOR (`^`)

```python
a, b = 5, 3   # 0101 ^ 0011
print(a ^ b)  # 6 (0110)
```

**ব্যাখ্যা:** দুই বিট ভিন্ন হলে `1`, সমান হলে `0`।

---

### 4) Bitwise NOT (`~`)

```python
a = 5         # 0101
print(~a)     # -6
```

**ব্যাখ্যা:** সব বিট উল্টে দেয় (two’s complement আকারে Negative হয়)।

---

### 5) Left Shift (`<<`)

```python
a = 5         # 0101
print(a << 1) # 10 (1010)
```

**ব্যাখ্যা:** বিটগুলো বামে সরায়, মান ২ গুণ হয়।

---

### 6) Right Shift (`>>`)

```python
a = 10        # 1010
print(a >> 1) # 5 (0101)
```

**ব্যাখ্যা:** বিটগুলো ডানে সরায়, মান অর্ধেক হয়।

---

# 🔹 Identity Operators (অবজেক্ট আইডেন্টিটি চেক করে)

👉 ভ্যালু সমান কিনা নয়, **মেমরি আইডেন্টিটি (object reference)** চেক করে।

---

### 7) `is`

```python
x = [1,2,3]
y = x
print(x is y)  # True
```

**ব্যাখ্যা:** `y` আসলে `x` এর একই অবজেক্টকে রেফার করছে।

---

### 8) `is not`

```python
x = [1,2,3]
y = [1,2,3]
print(x is not y)  # True
```

**ব্যাখ্যা:** `x` আর `y` দেখতে একই রকম হলেও আলাদা অবজেক্ট (ভিন্ন মেমরি)।

---

### 9) `is` বনাম `==`

```python
a = [10,20]
b = [10,20]
print(a == b)  # True  (মান সমান)
print(a is b)  # False (অবজেক্ট আলাদা)
```

**ব্যাখ্যা:** `==` মান তুলনা করে, `is` মেমরি লোকেশন তুলনা করে।

---

### 10) `None` চেক করার সঠিক উপায়

```python
x = None
print(x is None)      # True ✅
print(x == None)      # True কিন্তু কম ব্যবহার হয়
```

**ব্যাখ্যা:** `None` চেক করতে সবসময় `is` ব্যবহার করা উচিত।

---


# ✅ সারসংক্ষেপ

* **Arithmetic** → + - \* / // % \*\*
* **Comparison** → == != > < >= <=
* **Logical** → and or not
* **Bitwise** → &, |, ^, \~, <<, >>
* **Assignment** → =, +=, -= ইত্যাদি
* **Membership** → in, not in
* **Identity** → is, is not



---

## 1) দুই সংখ্যা যোগফল

**Problem:** দুটি সংখ্যা ইনপুট নিয়ে যোগফল বের করো।

```python
a, b = 12, 8
s = a + b
print(s)  # 20
```

**Why:** বেসিক আরিথমেটিক ও ভ্যারিয়েবল।

---

## 2) জোড়/বিজোড় চেক

**Problem:** একটি সংখ্যা জোড় নাকি বিজোড় তা প্রিন্ট করো।

```python
n = 17
print("Even" if n % 2 == 0 else "Odd")  # Odd
```

**Why:** `%` ও টার্নারি এক্সপ্রেশন।

---

## 3) তিন সংখ্যার মধ্যে বৃহত্তম

**Problem:** তিনটি সংখ্যার মধ্যে সর্বোচ্চটা বের করো।

```python
a, b, c = 10, 25, 7
print(max(a, b, c))  # 25
```

**Why:** বিল্ট-ইন `max()` ব্যবহার।

---

## 4) ফ্যাক্টোরিয়াল (Iterative)

**Problem:** n! (ফ্যাক্টোরিয়াল) বের করো।

```python
n = 5
fact = 1
for i in range(2, n+1):
    fact *= i
print(fact)  # 120
```

**Why:** লুপ ও গুণ।

---

## 5) ফিবোনাচ্চি সিরিজ (প্রথম n টার্ম)

**Problem:** প্রথম n টা Fibonacci সংখ্যা প্রিন্ট করো।

```python
n = 7
a, b = 0, 1
res = []
for _ in range(n):
    res.append(a)
    a, b = b, a + b
print(res)  # [0, 1, 1, 2, 3, 5, 8]
```

**Why:** মাল্টিপল অ্যাসাইনমেন্ট, লুপ।

---

## 6) প্রাইম নাম্বার চেক

**Problem:** সংখ্যা প্রাইম কি না।

```python
n = 29
is_prime = n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
print(is_prime)  # True
```

**Why:** রেঞ্জ, রুট অপ্টিমাইজেশন, `all()`।

---

## 7) স্ট্রিং প্যালিনড্রোম

**Problem:** স্ট্রিং উল্টে দিলেও একই থাকলে True।

```python
s = "madam"
print(s == s[::-1])  # True
```

**Why:** স্লাইসিং।

---

## 8) ভাওয়েল কাউন্ট

**Problem:** স্ট্রিং-এ কয়টা vowel আছে।

```python
s = "Programming in Python"
vowels = set("aeiouAEIOU")
count = sum(ch in vowels for ch in s)
print(count)  # 6
```

**Why:** সেট, কমপ্রিহেনশন, `sum(bool)`।

---

## 9) লিস্টের যোগফল ও গড়

**Problem:** একটি লিস্টের sum ও average বের করো।

```python
nums = [10, 20, 30, 40]
total = sum(nums)
avg = total / len(nums)
print(total, avg)  # 100 25.0
```

**Why:** `sum`, `len`, division।

---

## 10) সর্বোচ্চ/সর্বনিম্ন (ম্যানুয়াল)

**Problem:** `max/min` ছাড়া লিস্টের max/min বের করো।

```python
nums = [5, 2, 9, 1, 7]
mx, mn = nums[0], nums[0]
for x in nums[1:]:
    if x > mx: mx = x
    if x < mn: mn = x
print(mx, mn)  # 9 1
```

**Why:** শর্ত ও ট্রাভার্সাল।

---

## 11) ডুপ্লিকেট রিমুভ (অর্ডার রাখা)

**Problem:** লিস্ট থেকে ডুপ্লিকেট বাদ দাও, প্রথম দেখা অর্ডার রাখো।

```python
items = [1,2,2,3,1,4,3]
seen, unique = set(), []
for x in items:
    if x not in seen:
        seen.add(x)
        unique.append(x)
print(unique)  # [1,2,3,4]
```

**Why:** সেট + অর্ডার লিস্ট।

---

## 12) লিস্ট কমপ্রিহেনশন: স্কয়ার ফিল্টার

**Problem:** 1..20 থেকে জোড় সংখ্যার স্কয়ার।

```python
res = [x*x for x in range(1, 21) if x % 2 == 0]
print(res)
```

**Why:** কমপ্রিহেনশন + কন্ডিশন।

---

## 13) ডিকশনারি: শব্দগণনা

**Problem:** বাক্যের প্রতিটি শব্দের ফ্রিকোয়েন্সি।

```python
s = "to be or not to be"
freq = {}
for w in s.split():
    freq[w] = freq.get(w, 0) + 1
print(freq)  # {'to':2,'be':2,'or':1,'not':1}
```

**Why:** `dict.get`, `split`।

---

## 14) মার্জ ওভারল্যাপিং ইন্টারভাল

**Problem:** ওভারল্যাপিং ইন্টারভালগুলো মার্জ করো।

```python
intervals = [[1,3],[2,6],[8,10],[9,12]]
intervals.sort()
merged = []
for s, e in intervals:
    if not merged or s > merged[-1][1]:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)
print(merged)  # [[1,6],[8,12]]
```

**Why:** সোর্টিং, লিস্ট টপ চেক।

---

## 15) এনাগ্রাম চেক

**Problem:** দুটি স্ট্রিং এনাগ্রাম কি না (স্পেস/কেস ইগনোর)।

```python
a, b = "Listen", "Silent"
norm = lambda s: "".join(sorted(s.replace(" ", "").lower()))
print(norm(a) == norm(b))  # True
```

**Why:** নরমালাইজ + sort।

---

## 16) ইউনিক ক্যারেক্টার (স্ট্রিং)

**Problem:** স্ট্রিং-এ সব ক্যারেক্টার ইউনিক কি না।

```python
s = "abcdefA1"
print(len(s) == len(set(s)))  # True
```

**Why:** সেট সাইজ চেক।

---

## 17) টেম্পারেচার কনভার্সন

**Problem:** সেলসিয়াস → ফারেনহাইট।

```python
c = 37
f = (c * 9/5) + 32
print(f)  # 98.6
```

**Why:** ফর্মুলা ও ফ্লোট ম্যাথ।

---

## 18) সিম্পল ক্যালকুলেটর (ডিক্ট-ডিসপ্যাচ)

**Problem:** অপারেটর অনুসারে কাজ করো।

```python
a, b, op = 12, 4, "/"
ops = {"+": a+b, "-": a-b, "*": a*b, "/": a/b if b else None}
print(ops.get(op, "Invalid"))  # 3.0
```

**Why:** ডিকশনারি দ্বারা ডিসপ্যাচ প্যাটার্ন।

---

## 19) রান-লেংথ এনকোডিং (বেসিক)

**Problem:** স্ট্রিং কমপ্রেস (aaaabb → a4b2)।

```python
s = "aaabccccdd"
res, count = [], 1
for i in range(1, len(s)+1):
    if i < len(s) and s[i] == s[i-1]:
        count += 1
    else:
        res.append(s[i-1] + (str(count) if count > 1 else ""))
        count = 1
print("".join(res))  # a3bc4d2
```

**Why:** রান কাউন্টিং, বাউন্ডারি কেস।

---

## 20) টু-সাম (ইনডেক্স রিটার্ন)

**Problem:** লিস্টে এমন দুই ইন্ডেক্স খুঁজো যাদের যোগফল target।

```python
nums, target = [2,7,11,15], 9
seen = {}
ans = None
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        ans = (seen[need], i)
        break
    seen[x] = i
print(ans)  # (0, 1)
```

**Why:** হ্যাশম্যাপ দিয়ে O(n) সমাধান।

---


