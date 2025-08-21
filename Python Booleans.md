
---

# 🔹 Python Boolean (Theory)

👉 Boolean হলো ডাটা টাইপ, যা কেবল দুইটা ভ্যালু ধারণ করে:

* **True**
* **False**

---

### ১. Boolean আসলে কী?

* Python-এ `bool` হলো **int-এর সাবক্লাস**।
* অর্থাৎ,

  ```python
  int(True)  # 1
  int(False) # 0
  ```
* Boolean সাধারণত **শর্ত (Condition)** এ ব্যবহৃত হয়।

---

### ২. Boolean Expressions

* কোনো Comparison বা Logical operation করলে Boolean রিটার্ন হয়।
* উদাহরণ:

  ```python
  5 > 3   # True
  10 == 2 # False
  ```

---

### ৩. Truthy & Falsy Values

* Python-এ কিছু জিনিসকে **False** ধরা হয়:

  * `0`, `0.0`, `0j`
  * `""` (empty string)
  * `[]` (empty list), `()`, `{}`, `set()`
  * `None`
* বাকিগুলো সব **True** হিসেবে গণ্য হয়।

---

# 🔹 ১০টি Example with Explanation

---

### 1) Boolean Variable

```python
x = True
y = False
print(x, y)
```

**ব্যাখ্যা:** `True` এবং `False` হলো Boolean literal।

---

### 2) Comparison থেকে Boolean

```python
print(10 > 5)  # True
print(2 == 3)  # False
```

**ব্যাখ্যা:** তুলনা করলে Boolean ভ্যালু আসে।

---

### 3) Logical Operators

```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

**ব্যাখ্যা:** `and`, `or`, `not` Boolean expression এ ব্যবহার হয়।

---

### 4) Boolean as Integer

```python
print(True + 5)   # 6
print(False * 10) # 0
```

**ব্যাখ্যা:** `True = 1`, `False = 0`

---

### 5) Empty String = False

```python
print(bool(""))   # False
print(bool("Hi")) # True
```

---

### 6) Empty List = False

```python
print(bool([]))     # False
print(bool([1,2]))  # True
```

---

### 7) None = False

```python
x = None
print(bool(x))  # False
```

---

### 8) Condition এ Boolean

```python
age = 20
if age >= 18:
    print("Adult")   # Prints Adult
```

**ব্যাখ্যা:** শর্ত চেক করার জন্য Boolean ব্যবহার হয়।

---

### 9) Boolean Function Example

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
```

---

### 10) Boolean Casting

```python
print(bool(0))   # False
print(bool(123)) # True
```

**ব্যাখ্যা:** সংখ্যা → Boolean কনভার্ট করলে, কেবল `0` হলে False, বাকি সব True।

---

# ✅ সারসংক্ষেপ

* Boolean টাইপের মান = **True/False**
* `bool` আসলে `int` এর সাবক্লাস
* Boolean আসে → comparison, logical অপারেটর, condition থেকে
* **Falsy Values:** 0, 0.0, 0j, "", \[], {}, None
* Boolean condition এ সবচেয়ে বেশি ব্যবহার হয়

---


