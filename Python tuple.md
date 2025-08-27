
---

# 📘 Python Tuple — বিস্তারিত

## 🔹 Tuple কী?

* Tuple হলো **immutable sequence** (মানে একবার বানালে এর ভ্যালু পরিবর্তন করা যায় না)।
* List এর মতোই ordered collection, কিন্তু **modify, append, remove** করা যায় না।
* Declaration: `()` দিয়ে।

```python
t = (1, 2, 3, 4)
print(t)        # (1, 2, 3, 4)
print(type(t))  # <class 'tuple'>
```

---

## 🔹 Tuple এর গুরুত্বপূর্ণ Function/Method লিস্ট

1. `len()` → length বের করে
2. `max()` → সবচেয়ে বড় ভ্যালু
3. `min()` → সবচেয়ে ছোট ভ্যালু
4. `sum()` → যোগফল (যদি numeric হয়)
5. `tuple()` → অন্য iterable কে tuple এ রূপান্তর
6. `count(x)` → কতবার এসেছে
7. `index(x)` → কোন পজিশনে আছে
8. Membership → `in`, `not in`
9. Concatenation → `+` দিয়ে যোগ
10. Repetition → `*` দিয়ে বারবার রিপিট
11. Slicing → `[start:end:step]`
12. Iteration → loop দিয়ে ঘোরা
13. Unpacking → আলাদা ভেরিয়েবলে ভাগ করা
14. Nesting → tuple এর মধ্যে tuple রাখা

---

# 📌 এখন প্রতিটা Function এর Example + ব্যাখ্যা

---

## 1. `len()`

```python
t = (10, 20, 30, 40)
print(len(t))   # 4
```

➡️ tuple এ কয়টা element আছে বের করে।

---

## 2. `max()`

```python
t = (2, 9, 5, 1)
print(max(t))   # 9
```

➡️ সবচেয়ে বড় মান রিটার্ন করে।

---

## 3. `min()`

```python
t = (2, 9, 5, 1)
print(min(t))   # 1
```

➡️ সবচেয়ে ছোট মান রিটার্ন করে।

---

## 4. `sum()`

```python
t = (5, 10, 15)
print(sum(t))   # 30
```

➡️ tuple এর সব element এর যোগফল দেয় (শুধু সংখ্যা হলে)।

---

## 5. `tuple()` কনভার্সন

```python
lst = [1, 2, 3]
t = tuple(lst)
print(t)    # (1, 2, 3)

s = "abc"
print(tuple(s))  # ('a', 'b', 'c')
```

➡️ অন্য iterable (list, string) কে tuple বানায়।

---

## 6. `count(x)`

```python
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))   # 3
```

➡️ নির্দিষ্ট element কয়বার এসেছে তা জানায়।

---

## 7. `index(x)`

```python
t = ("a", "b", "c", "b")
print(t.index("b"))  # 1
```

➡️ element প্রথম কোন পজিশনে আছে তা দেয়।

---

## 8. Membership — `in`, `not in`

```python
t = (10, 20, 30)
print(20 in t)      # True
print(50 not in t)  # True
```

---

## 9. Concatenation — `+`

```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4)
```

➡️ দুইটা tuple কে একসাথে যোগ করা যায়।

---

## 10. Repetition — `*`

```python
t = (1, 2)
print(t * 3)   # (1, 2, 1, 2, 1, 2)
```

---

## 11. Slicing — `[start:end:step]`

```python
t = (0, 1, 2, 3, 4, 5)
print(t[1:4])     # (1, 2, 3)
print(t[:3])      # (0, 1, 2)
print(t[::2])     # (0, 2, 4)
print(t[::-1])    # (5, 4, 3, 2, 1, 0)
```

➡️ tuple থেকে নির্দিষ্ট অংশ কেটে আনা যায়।

---

## 12. Iteration

```python
t = ("Dhaka", "Khulna", "Chittagong")
for city in t:
    print(city)
```

---

## 13. Unpacking

```python
t = (100, 200, 300)
a, b, c = t
print(a, b, c)   # 100 200 300
```

➡️ tuple এর মান আলাদা আলাদা ভেরিয়েবলে রাখা যায়।

---

## 14. Nested Tuple

```python
t = (1, (2, 3), (4, 5, 6))
print(t[1])        # (2, 3)
print(t[2][1])     # 5
```

➡️ tuple এর ভিতরে আবার tuple রাখা যায়।

---

# ✅ সারসংক্ষেপ টেবিল

| Function/Operation | কাজ                           |
| ------------------ | ----------------------------- |
| `len()`            | element সংখ্যা বের করে        |
| `max(), min()`     | সবচেয়ে বড়/ছোট মান             |
| `sum()`            | যোগফল                         |
| `tuple()`          | অন্য iterable কে tuple বানানো |
| `count(x)`         | কয়বার এসেছে                   |
| `index(x)`         | প্রথম অবস্থান                 |
| `in, not in`       | membership test               |
| `+`                | concatenation                 |
| `*`                | repetition                    |
| `slicing`          | অংশ কেটে আনা                  |
| `for loop`         | iterate                       |
| unpacking          | আলাদা ভেরিয়েবল এ ভাগ          |
| nested tuple       | tuple এর ভিতরে tuple          |

---

