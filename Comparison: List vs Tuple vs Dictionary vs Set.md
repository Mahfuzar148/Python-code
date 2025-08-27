
---

# 📘 Comparison: List vs Tuple vs Dictionary vs Set

| Feature         | **List**                                | **Tuple**                    | **Dictionary**                      | **Set**                             |
| --------------- | --------------------------------------- | ---------------------------- | ----------------------------------- | ----------------------------------- |
| **Syntax**      | `[1, 2, 3]`                             | `(1, 2, 3)`                  | `{"a":1, "b":2}`                    | `{1, 2, 3}`                         |
| **Order**       | Ordered (insertion order preserved)     | Ordered (fixed)              | Ordered (Python 3.7+)               | Unordered                           |
| **Mutable?**    | ✅ Yes (changeable)                      | ❌ No (immutable)             | ✅ Yes (keys unique, values mutable) | ✅ Yes (but no duplicates)           |
| **Duplicates**  | Allowed                                 | Allowed                      | Keys unique, values can duplicate   | ❌ Not allowed                       |
| **Indexing**    | Supported (list\[0])                    | Supported (tuple\[0])        | By key (dict\["a"])                 | ❌ Not supported                     |
| **Use Case**    | Collection of ordered, changeable items | Fixed collection (safe data) | Key-value mapping                   | Unique items, fast membership check |
| **Performance** | Slower than tuple                       | Faster (immutable)           | Lookup O(1) avg.                    | Membership test O(1) avg.           |

---

# 📘 Conversion Methods

## 🔹 1. List ↔ Tuple

```python
# List to Tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)   # (1, 2, 3)

# Tuple to List
tup = (4, 5, 6)
lst = list(tup)
print(lst)   # [4, 5, 6]
```

---

## 🔹 2. List ↔ Set

```python
# List to Set
lst = [1, 2, 2, 3]
s = set(lst)
print(s)   # {1, 2, 3}  (duplicates removed)

# Set to List
s = {4, 5, 6}
lst = list(s)
print(lst)  # [4, 5, 6]
```

---

## 🔹 3. Tuple ↔ Set

```python
# Tuple to Set
tup = (1, 2, 3, 2)
s = set(tup)
print(s)   # {1, 2, 3}

# Set to Tuple
s = {4, 5, 6}
tup = tuple(s)
print(tup)  # (4, 5, 6) → order random হতে পারে
```

---

## 🔹 4. List ↔ Dictionary

```python
# List of pairs → Dictionary
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2}

# Direct List to Dict (index → value)
lst = [10, 20, 30]
d = dict(enumerate(lst))
print(d)  # {0: 10, 1: 20, 2: 30}

# Dictionary to List (keys or values or items)
d = {"x": 1, "y": 2}
print(list(d))         # ['x', 'y'] → only keys
print(list(d.values())) # [1, 2]
print(list(d.items()))  # [('x',1), ('y',2)]
```

---

## 🔹 5. Tuple ↔ Dictionary

```python
# Tuple of pairs → Dict
tup = (("a", 1), ("b", 2))
d = dict(tup)
print(d)  # {'a': 1, 'b': 2}

# Dict → Tuple
d = {"x": 10, "y": 20}
print(tuple(d.items()))  # (('x',10), ('y',20))
```

---

## 🔹 6. Set ↔ Dictionary

```python
# Set → Dictionary (value default None)
s = {"a", "b", "c"}
d = dict.fromkeys(s, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}

# Dictionary → Set
d = {"x": 1, "y": 2}
print(set(d))          # {'x','y'} → only keys
print(set(d.values())) # {1,2}
```

---

# ✅ সারসংক্ষেপ

* **List** → ordered, mutable, duplicates allowed.
* **Tuple** → ordered, immutable.
* **Dictionary** → key-value pair, keys unique.
* **Set** → unordered, unique elements only.

**Conversion Functions:**

* `list(), tuple(), set(), dict(), dict.fromkeys(), enumerate(), zip()`

---


