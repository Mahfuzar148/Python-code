
---

# 🔹 Python Data Types (তত্ত্ব)

Python-এ মূলত কয়েক ধরনের ডাটা টাইপ আছে:

1. **Numeric Types** → `int`, `float`, `complex`
2. **Sequence Types** → `list`, `tuple`, `range`
3. **Text Type** → `str`
4. **Set Types** → `set`, `frozenset`
5. **Mapping Type** → `dict`
6. **Boolean Type** → `bool`
7. **Binary Types** → `bytes`, `bytearray`, `memoryview`
8. **None Type** → `NoneType`

👉 Python **dynamic typed** অর্থাৎ ভ্যারিয়েবল তৈরি করার সময় টাইপ ডিক্লেয়ার করতে হয় না।

---

# 🔹 ২০টি Example with Explanation

---

### 1) Integer (`int`)

```python
x = 10
print(type(x))  # <class 'int'>
```

**ব্যাখ্যা:** `int` হলো পূর্ণ সংখ্যা ডাটা টাইপ।

---

### 2) Float (`float`)

```python
pi = 3.1416
print(type(pi))
```

**ব্যাখ্যা:** দশমিক সংখ্যার জন্য `float` ব্যবহার হয়।

---

### 3) Complex Number (`complex`)

```python
z = 3 + 4j
print(z.real, z.imag)  # 3.0 4.0
```

**ব্যাখ্যা:** complex number = `real + imag*j`

---

### 4) String (`str`)

```python
name = "Python"
print(name.upper())
```

**ব্যাখ্যা:** `str` হলো টেক্সট ডাটা। এতে অনেক built-in method আছে।

---

### 5) String Multiline

```python
text = """This is
a multiline
string"""
print(text)
```

**ব্যাখ্যা:** তিনটি কোটেশন (`"""`) দিয়ে মাল্টি-লাইন স্ট্রিং লেখা যায়।

---

### 6) List

```python
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)
```

**ব্যাখ্যা:** লিস্ট হলো ordered & mutable collection।

---

### 7) List Slicing

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])  # [20,30,40]
```

**ব্যাখ্যা:** লিস্টের অংশ বের করতে slice ব্যবহার করা হয়।

---

### 8) Tuple

```python
t = (1, 2, 3)
print(type(t))
```

**ব্যাখ্যা:** tuple ordered কিন্তু immutable।

---

### 9) Tuple Unpacking

```python
a, b, c = (10, 20, 30)
print(a, b, c)
```

**ব্যাখ্যা:** tuple থেকে একাধিক ভ্যারিয়েবল একসাথে পাওয়া যায়।

---

### 10) Range

```python
r = range(1,6)
print(list(r))  # [1,2,3,4,5]
```

**ব্যাখ্যা:** `range()` দিয়ে সিকোয়েন্স জেনারেট হয়, সাধারণত লুপে ব্যবহৃত হয়।

---

### 11) Set

```python
s = {1, 2, 2, 3}
print(s)  # {1,2,3}
```

**ব্যাখ্যা:** set unordered এবং duplicate মান রাখে না।

---

### 12) Set Operations

```python
a = {1,2,3}
b = {3,4,5}
print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
```

**ব্যাখ্যা:** set দিয়ে union, intersection ইত্যাদি কাজ করা যায়।

---

### 13) FrozenSet

```python
fs = frozenset([1,2,3])
# fs.add(4)  # error (immutable)
print(fs)
```

**ব্যাখ্যা:** `frozenset` হলো immutable set।

---

### 14) Dictionary

```python
student = {"name":"Rahim","age":20}
print(student["name"])
```

**ব্যাখ্যা:** dict হলো key-value mapping।

---

### 15) Dictionary Update

```python
student["age"] = 21
print(student)
```

**ব্যাখ্যা:** dict mutable; key-এর value পরিবর্তন করা যায়।

---

### 16) Boolean

```python
x = True
y = False
print(x and not y)  # True
```

**ব্যাখ্যা:** `bool` কন্ডিশনাল অপারেশনে ব্যবহার হয়।

---

### 17) NoneType

```python
val = None
print(type(val))  # <class 'NoneType'>
```

**ব্যাখ্যা:** `None` মানে কোনো ভ্যালু নেই।

---

### 18) Bytes

```python
b = b"Hello"
print(type(b))
```

**ব্যাখ্যা:** `bytes` হলো immutable byte sequence।

---

### 19) Bytearray

```python
ba = bytearray([65,66,67])
ba[0] = 90
print(ba)  # bytearray(b'ZBC')
```

**ব্যাখ্যা:** `bytearray` হলো mutable byte sequence।

---

### 20) MemoryView

```python
mv = memoryview(b"Python")
print(mv[0])  # 80 (ASCII of 'P')
```

**ব্যাখ্যা:** `memoryview` byte-level access দেয়।

---

# ✅ সারসংক্ষেপ

* **Numeric Types** → int, float, complex
* **Sequence Types** → list, tuple, range
* **Set Types** → set, frozenset
* **Mapping Type** → dict
* **Text Type** → str
* **Boolean** → bool
* **Binary Types** → bytes, bytearray, memoryview
* **NoneType** → None

---


