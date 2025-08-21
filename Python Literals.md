
---

# 🔹 Python Literals (থিওরি)

👉 **Literal** মানে হলো কোনো ভ্যালু যেটা সরাসরি কোডে লেখা থাকে।
যেমনঃ `10`, `"Hello"`, `3.14`, `[1,2,3]` ইত্যাদি।

Python-এ প্রধান প্রধান লিটারাল টাইপগুলো হলো:

1. **Numeric Literals** → `int`, `float`, `complex`
2. **String Literals** → `"Hello"`, `'Python'`, `"""multiline"""`
3. **Boolean Literals** → `True`, `False`
4. **Special Literal** → `None`
5. **Collection Literals** → `list []`, `tuple ()`, `dict {}`, `set {}`

---

# 🔹 ১০টি Example with Explanation

---

### 1) Integer Literal

```python
x = 100
print(x, type(x))  # 100 <class 'int'>
```

**ব্যাখ্যা:** `100` হলো integer literal।

---

### 2) Float Literal

```python
pi = 3.1416
print(pi, type(pi))
```

**ব্যাখ্যা:** দশমিক মান হলো float literal।

---

### 3) Complex Literal

```python
z = 2 + 3j
print(z, type(z))  # (2+3j) <class 'complex'>
```

**ব্যাখ্যা:** `a+bj` আকারে লেখা complex literal।

---

### 4) String Literal (Single line)

```python
name = "Python"
print(name)
```

**ব্যাখ্যা:** `"Python"` হলো string literal।

---

### 5) String Literal (Multi-line)

```python
text = """This is
a multi-line
string literal"""
print(text)
```

**ব্যাখ্যা:** তিনটি কোটেশন (`"""`) দিয়ে মাল্টি-লাইন string literal লেখা যায়।

---

### 6) Boolean Literals

```python
x = True
y = False
print(x, y)
```

**ব্যাখ্যা:** `True` এবং `False` হলো boolean literal।

---

### 7) Special Literal (None)

```python
val = None
print(val, type(val))
```

**ব্যাখ্যা:** `None` হলো special literal, মানে "কিছু নেই"।

---

### 8) List Literal

```python
fruits = ["apple", "banana", "mango"]
print(fruits)
```

**ব্যাখ্যা:** `["apple","banana","mango"]` হলো list literal।

---

### 9) Tuple Literal

```python
t = (10, 20, 30)
print(t)
```

**ব্যাখ্যা:** `(10,20,30)` হলো tuple literal।

---

### 10) Dictionary Literal

```python
student = {"name":"Rahim", "age":20}
print(student)
```

**ব্যাখ্যা:** `{"key":"value"}` আকারে dictionary literal তৈরি হয়।

---

# ✅ সারসংক্ষেপ

* **Numeric Literals** → int, float, complex
* **String Literals** → single, double, multiline
* **Boolean Literals** → True, False
* **Special Literal** → None
* **Collection Literals** → list, tuple, dict, set

---


