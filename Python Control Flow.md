
---

# 🔹 Python Control Flow (Theory)

👉 Control Flow মানে হলো **প্রোগ্রামের কোন অংশ কখন চলবে সেটা নিয়ন্ত্রণ করা**।
Python-এ Control Flow প্রধানত ৩ ভাগে বিভক্ত:

1. **Conditional Statements** → `if`, `if-else`, `if-elif-else`, nested if
2. **Loops** → `for`, `while`, nested loops
3. **Loop Control Statements** → `break`, `continue`, `pass`

---

# 🔹 Part 1: Conditional Statements

---

### 1) Simple if

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

### 2) if-else

```python
n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### 3) if-elif-else

```python
mark = 65
if mark >= 80:
    print("A+")
elif mark >= 60:
    print("B")
else:
    print("Fail")
```

---

### 4) Nested if

```python
x = 20
if x > 10:
    if x < 30:
        print("x is between 10 and 30")
```

---

### 5) One-line if (Ternary Operator)

```python
a, b = 10, 20
print("a is bigger" if a > b else "b is bigger")
```

---

# 🔹 Part 2: Loops

---

### 6) while loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

### 7) for loop with range

```python
for i in range(1, 6):
    print(i)
```

---

### 8) Iterating List

```python
fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)
```

---

### 9) Iterating String

```python
for ch in "Python":
    print(ch)
```

---

### 10) Iterating Dictionary

```python
student = {"name":"Rahim", "age":20}
for key, value in student.items():
    print(key, "=", value)
```

---

### 11) Nested Loop

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

---

# 🔹 Part 3: Loop Control Statements

---

### 12) break statement

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

---

### 13) continue statement

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

---

### 14) pass statement

```python
for i in range(5):
    if i == 2:
        pass  # Placeholder
    print(i)
```

---

### 15) else with loop

```python
for i in range(3):
    print(i)
else:
    print("Loop finished")
```

---

### 16) Prime check with for-else

```python
n = 7
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
```

---

# 🔹 Part 4: More Advanced Flow

---

### 17) match-case (Python 3.10+)

```python
x = 2
match x:
    case 1: print("One")
    case 2: print("Two")
    case _: print("Other")
```

---

### 18) List Comprehension with if

```python
nums = [1,2,3,4,5]
evens = [x for x in nums if x % 2 == 0]
print(evens)
```

---

### 19) Nested List Comprehension

```python
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
```

---

### 20) while True (infinite loop with break)

```python
while True:
    cmd = input("Enter q to quit: ")
    if cmd == "q":
        break
```

---

### 21) Using enumerate

```python
fruits = ["apple", "banana", "mango"]
for i, f in enumerate(fruits):
    print(i, f)
```

---

### 22) Using zip

```python
names = ["A", "B", "C"]
marks = [80, 70, 90]
for n, m in zip(names, marks):
    print(n, m)
```

---

### 23) any() with loop

```python
nums = [1, 3, 5, 7]
print(any(x % 2 == 0 for x in nums))  # False
```

---

### 24) all() with loop

```python
nums = [2, 4, 6]
print(all(x % 2 == 0 for x in nums))  # True
```

---

### 25) Complex Example: FizzBuzz

```python
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

# ✅ সারসংক্ষেপ

* **if/elif/else** → শর্ত নিয়ন্ত্রণ
* **while / for** → লুপ
* **break, continue, pass** → লুপ নিয়ন্ত্রণ
* **else with loop, match-case, comprehension** → advanced control flow

---

