
---

# 🐍 Python Enum (Enumerations) — বিস্তারিত

---

## 🔹 Enum কী?

👉 **Enum (Enumeration)** হলো একটা symbolic name collection, যেগুলো constant value কে **একটা নাম** দিয়ে represent করে।
👉 Enums ব্যবহার করলে কোড readable হয়, hard-coded number/string ব্যবহার করতে হয় না।

📌 উদাহরণ (বাস্তব জীবন):

* সপ্তাহের দিন (সোম, মঙ্গল, বুধ, ...)
* রং (লাল, সবুজ, নীল)
* Status Code (SUCCESS=1, FAILURE=0)

---

## 🔹 Python এ Enum Import

Python এ Enum ব্যবহার করতে হলে **enum module** ইম্পোর্ট করতে হয়।

```python
from enum import Enum
```

---

## 📝 Example 1: Basic Enum

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)        # Color.RED
print(Color.RED.name)   # RED
print(Color.RED.value)  # 1
```

👉 এখানে `Color` নামে একটা Enum বানানো হয়েছে যেখানে `RED=1`, `GREEN=2`, `BLUE=3`।

---

## 📝 Example 2: Iterating over Enum

```python
for color in Color:
    print(color.name, "=", color.value)
```

👉 Output:

```
RED = 1
GREEN = 2
BLUE = 3
```

---

## 📝 Example 3: Comparing Enum Members

```python
if Color.RED == Color.GREEN:
    print("Same")
else:
    print("Different")
```

👉 Output:

```
Different
```

---

## 📝 Example 4: Weekdays Example

```python
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(Weekday.FRIDAY.name, Weekday.FRIDAY.value)  # FRIDAY 5
```

---

## 📝 Example 5: Using Enum in Functions

```python
def is_weekend(day):
    return day in (Weekday.SATURDAY, Weekday.SUNDAY)

print(is_weekend(Weekday.SATURDAY))  # True
print(is_weekend(Weekday.MONDAY))    # False
```

---

## 📝 Example 6: Auto Values (auto())

👉 Python 3.6+ এ `auto()` দিয়ে values auto-assign করা যায়।

```python
from enum import auto

class Status(Enum):
    SUCCESS = auto()
    FAILURE = auto()
    PENDING = auto()

for s in Status:
    print(s.name, s.value)
```

👉 Output (auto assign):

```
SUCCESS 1
FAILURE 2
PENDING 3
```

---

## 📝 Example 7: Enum with Methods

```python
class Shape(Enum):
    CIRCLE = 1
    SQUARE = 2
    TRIANGLE = 3
    
    def describe(self):
        if self == Shape.CIRCLE:
            return "Round shape"
        elif self == Shape.SQUARE:
            return "Four equal sides"
        else:
            return "Three sides"

print(Shape.TRIANGLE.describe())   # Three sides
```

---

## 📝 Example 8: Access Enum by Value or Name

```python
print(Weekday(1))           # Weekday.MONDAY
print(Weekday['FRIDAY'])    # Weekday.FRIDAY
```

---

## 🔹 Enum এর সুবিধা

1. **Readability বাড়ায়** → `Color.RED` পড়তে সহজ, `1` এর চেয়ে।
2. **Constants define করা সহজ হয়**।
3. **Comparison clean হয়** (no magic numbers)।
4. **Group related constants** একসাথে রাখা যায়।

---

## 🔹 Enum বনাম সাধারণ Constant

| বিষয়        | Enum                                | Constant Variable     |
| ----------- | ----------------------------------- | --------------------- |
| Grouping    | Related constants group করা যায়     | আলাদা আলাদা থাকে      |
| Readability | বেশি readable (`Color.RED`)         | কম readable (`RED=1`) |
| Safety      | Duplicate/invalid value এ error দেয় | সহজে ভুল হতে পারে     |

---

## ✅ সারসংক্ষেপ

* **Enum** হলো symbolic names for constants।
* Python এ `enum.Enum` ব্যবহার করে বানানো হয়।
* Features: `.name`, `.value`, iteration, comparison।
* `auto()` দিয়ে auto numbering সম্ভব।
* ব্যবহার: Days, Status Codes, Colors, Configurations ইত্যাদি।

---

