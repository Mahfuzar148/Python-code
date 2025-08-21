
---

# 🔹 Python Type Casting (Theory)

👉 **Type Casting** মানে হলো একটি ডেটা টাইপকে আরেকটি ডেটা টাইপে রূপান্তর করা।
Python-এ দুইভাবে টাইপ কাস্টিং হয়:

1. **Implicit Type Casting (Type Conversion)**

   * Python নিজে থেকে টাইপ কনভার্ট করে।
   * যেমনঃ `int + float → float`

2. **Explicit Type Casting (Type Casting by user)**

   * আমরা নিজেরা চাইলে এক টাইপ থেকে আরেক টাইপে কনভার্ট করি।
   * Common ফাংশনসমূহ:

     * `int()` → ইন্টিজার বানায়
     * `float()` → ফ্লোট বানায়
     * `str()` → স্ট্রিং বানায়
     * `list()`, `tuple()`, `set()` → ডেটা টাইপ কনভার্ট করে
     * `dict()` → key-value পেয়ার থেকে dict বানায়

---

# 🔹 ১০টি Example with Explanation

---

### 1) Implicit Type Casting

```python
a = 5      # int
b = 2.5    # float
c = a + b
print(c, type(c))  # 7.5 <class 'float'>
```

**ব্যাখ্যা:** Python int + float কে স্বয়ংক্রিয়ভাবে float বানায়।

---

### 2) int() ব্যবহার

```python
x = int(3.9)
print(x, type(x))  # 3 <class 'int'>
```

**ব্যাখ্যা:** দশমিক বাদ দিয়ে integer বানায় (রাউন্ড করে না, শুধু truncate করে)।

---

### 3) float() ব্যবহার

```python
x = float(5)
print(x, type(x))  # 5.0 <class 'float'>
```

**ব্যাখ্যা:** int কে float বানায়।

---

### 4) str() ব্যবহার

```python
x = str(123)
print(x, type(x))  # "123" <class 'str'>
```

**ব্যাখ্যা:** সংখ্যা → string কনভার্ট করা যায়।

---

### 5) list() ব্যবহার

```python
t = (1,2,3)
l = list(t)
print(l, type(l))  # [1,2,3] <class 'list'>
```

**ব্যাখ্যা:** tuple → list কনভার্ট।

---

### 6) tuple() ব্যবহার

```python
s = {1,2,3}
t = tuple(s)
print(t, type(t))
```

**ব্যাখ্যা:** set → tuple কনভার্ট।

---

### 7) set() ব্যবহার

```python
l = [1,2,2,3]
s = set(l)
print(s, type(s))  # {1,2,3} <class 'set'>
```

**ব্যাখ্যা:** list → set করলে duplicate বাদ যায়।

---

### 8) dict() ব্যবহার

```python
pairs = [(1,"a"), (2,"b")]
d = dict(pairs)
print(d, type(d))  # {1:"a", 2:"b"}
```

**ব্যাখ্যা:** key-value pair list থেকে dict বানানো যায়।

---

### 9) String → List

```python
s = "Python"
l = list(s)
print(l)  # ['P','y','t','h','o','n']
```

**ব্যাখ্যা:** string কে character list বানানো যায়।

---

### 10) Boolean Casting

```python
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("Hi"))   # True
```

**ব্যাখ্যা:** 0, "", None = False; বাকি সবকিছু = True

---

# ✅ সারসংক্ষেপ

* **Implicit Casting** → Python নিজে টাইপ বদলায়।
* **Explicit Casting** → আমরা ফাংশন ব্যবহার করে টাইপ কনভার্ট করি।
* গুরুত্বপূর্ণ ফাংশন: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bool()`

---


# 🔹 Extra 10 Examples of Type Casting in Python

---

### 11) Float String → Float

```python
s = "3.1416"
f = float(s)
print(f, type(f))  # 3.1416 <class 'float'>
```

**ব্যাখ্যা:** string → float করা যায় যদি string এর ভেতরে সংখ্যা থাকে।

---

### 12) String → Integer

```python
s = "100"
i = int(s)
print(i, type(i))  # 100 <class 'int'>
```

**ব্যাখ্যা:** string → int করা যায় যদি string এর ভেতরে শুধু সংখ্যা থাকে।

---

### 13) Invalid Casting Error

```python
s = "abc"
# print(int(s))   # ValueError: invalid literal for int()
```

**ব্যাখ্যা:** সংখ্যা ছাড়া অন্য string কে int/float এ কনভার্ট করলে error হয়।

---

### 14) List → String (join ব্যবহার)

```python
chars = ['P','y','t','h','o','n']
s = "".join(chars)
print(s, type(s))  # "Python" <class 'str'>
```

**ব্যাখ্যা:** list of string → single string এ কনভার্ট করা যায়।

---

### 15) String → List of Words (split)

```python
sentence = "I love Python"
words = sentence.split()
print(words)  # ['I','love','Python']
```

**ব্যাখ্যা:** `split()` ব্যবহার করলে string → list of words হয়ে যায়।

---

### 16) Int → Binary, Octal, Hexadecimal (string আকারে)

```python
n = 25
print(bin(n))  # '0b11001'
print(oct(n))  # '0o31'
print(hex(n))  # '0x19'
```

**ব্যাখ্যা:** int → অন্য number system এর string representation বানানো যায়।

---

### 17) Binary String → Int

```python
b = "1010"
i = int(b, 2)
print(i)  # 10
```

**ব্যাখ্যা:** string কে base-2 (binary) থেকে int এ কনভার্ট করা যায়।

---

### 18) List of Tuples → Dict

```python
pairs = [("a",1),("b",2)]
d = dict(pairs)
print(d)  # {'a':1,'b':2}
```

**ব্যাখ্যা:** (key,value) পেয়ার লিস্টকে dict বানানো যায়।

---

### 19) Bool → Int/Str

```python
print(int(True))   # 1
print(int(False))  # 0
print(str(True))   # "True"
```

**ব্যাখ্যা:** bool কে int বা str এ কনভার্ট করা যায়।

---

### 20) Complex → String

```python
z = 5 + 6j
s = str(z)
print(s, type(s))  # '(5+6j)' <class 'str'>
```

**ব্যাখ্যা:** complex number → string কনভার্ট করা যায়।

---

