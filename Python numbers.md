
---

# 🔹 Python Numbers (Theory)

Python-এ **number data type** কয়েক রকম হয়:

1. **Integers (`int`)**

   * ধনাত্মক বা ঋণাত্মক পূর্ণসংখ্যা।
   * সীমাহীন (memory যত থাকে)।
   * Example: `-5, 0, 100000`

2. **Floating Point Numbers (`float`)**

   * দশমিক সংখ্যা (real numbers)।
   * Example: `3.14, -0.5, 2.0`

3. **Complex Numbers (`complex`)**

   * আকার: `a + bj` (যেখানে `a` = real part, `b` = imaginary part)।
   * Example: `2+3j`

4. **Boolean (`bool`)**

   * আসলে এটা `int` এর সাবক্লাস।
   * `True` → 1, `False` → 0

---

# 🔹 কিছু গুরুত্বপূর্ণ ধারণা

* Python-এ সংখ্যা **ডাইনামিক টাইপড** → আগে থেকে ডাটা টাইপ ডিক্লেয়ার করতে হয় না।
* **Type Conversion:** `int()`, `float()`, `complex()` ব্যবহার করে টাইপ কনভার্ট করা যায়।
* **Math Module:** `math.sqrt()`, `math.pi`, `math.sin()` ইত্যাদি।
* **Random Module:** `random.randint()`, `random.random()` ইত্যাদি।
* **Operators:** `+ - * / % // **` সংখ্যা নিয়ে কাজ করতে ব্যবহার হয়।

---

# 🔹 Examples (with Explanation)

---

### 1) Integer Example

```python
x = 10
print(x, type(x))   # 10 <class 'int'>
```

---

### 2) Float Example

```python
y = 3.1416
print(y, type(y))  # 3.1416 <class 'float'>
```

---

### 3) Complex Example

```python
z = 2 + 3j
print(z.real, z.imag)  # 2.0 3.0
```

---

### 4) Boolean is a Number

```python
print(True + 5)   # 6
print(False * 10) # 0
```

**ব্যাখ্যা:** `True = 1`, `False = 0`

---

### 5) Division vs Floor Division

```python
print(7 / 2)   # 3.5 (float)
print(7 // 2)  # 3 (integer)
```

---

### 6) Modulus (ভাগশেষ)

```python
print(10 % 3)  # 1
```

---

### 7) Power / Exponentiation

```python
print(2 ** 5)  # 32
```

---

### 8) Absolute Value

```python
print(abs(-7))  # 7
```

---

### 9) Rounding Numbers

```python
print(round(3.1416, 2))  # 3.14
```

---

### 10) Min / Max

```python
nums = [10, 20, 5, 30]
print(min(nums), max(nums))  # 5 30
```

---

### 11) Sum of List

```python
print(sum([1,2,3,4,5]))  # 15
```

---

### 12) Math Module

```python
import math
print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592...
```

---

### 13) Trigonometric Functions

```python
print(math.sin(math.pi/2))  # 1.0
```

---

### 14) Logarithm

```python
print(math.log(100, 10))  # 2.0
```

---

### 15) Random Number

```python
import random
print(random.randint(1, 10))  # 1 থেকে 10 এর মধ্যে র‍্যান্ডম নাম্বার
```

---

### 16) Float Infinity

```python
x = float("inf")
print(x > 1000000)  # True
```

---

### 17) NaN (Not a Number)

```python
y = float("nan")
print(y == y)  # False
```

---

### 18) Complex Calculation

```python
z1 = 2 + 3j
z2 = 1 + 4j
print(z1 * z2)  # (-10+11j)
```

---

### 19) Binary / Octal / Hex Representation

```python
n = 25
print(bin(n))  # 0b11001
print(oct(n))  # 0o31
print(hex(n))  # 0x19
```

---

### 20) Convert Back to Int

```python
print(int("1010", 2))  # 10  (binary string → int)
```

---

# ✅ সারসংক্ষেপ

* **int** → পূর্ণসংখ্যা
* **float** → দশমিক সংখ্যা
* **complex** → a+bj আকারে imaginary সংখ্যা
* **bool** → True/False, আসলে int-এর সাবক্লাস
* Math & Random module সংখ্যা নিয়ে কাজ করতে ব্যবহৃত হয়
* সংখ্যা বিভিন্ন **base (2,8,16)** এ কনভার্ট করা যায়

---


