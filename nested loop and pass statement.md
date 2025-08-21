
1. **for–else loop**
2. **nested loop**
3. **pass statement**

---

# 🔹 1) for–else loop

👉 Python-এ `for` লুপের সাথে **`else`** ব্যবহার করা যায়।

* **`else` ব্লক কেবল তখনই চলবে যখন লুপ সম্পূর্ণ শেষ হবে (break ছাড়া)।**
* যদি `break` হয় → `else` আর চলবে না।

### Example 1: for–else সাধারণ

```python
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 != 0:
        print("Odd found")
        break
else:
    print("No odd found")
```

**ব্যাখ্যা:** এখানে সব সংখ্যা জোড়, তাই `else` ব্লক চলবে।

---

### Example 2: for–else দিয়ে Prime check

```python
n = 11
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
```

**ব্যাখ্যা:** যদি `n` কোনো সংখ্যা দিয়ে ভাগ হয় → `break` হবে, তাই `else` চলবে না। প্রাইম হলে `else` চলবে।

---

# 🔹 2) Nested Loop

👉 লুপের ভেতরে আরেকটা লুপ চালানোকে **nested loop** বলে।

* সাধারণত টেবিল/ম্যাট্রিক্স/প্যাটার্ন প্রিন্ট করতে ব্যবহৃত হয়।

### Example 3: Multiplication table (nested for)

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i*j)
```

---

### Example 4: Pattern printing

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

**Output:**

```
*
**
***
****
*****
```

---

### Example 5: Nested loop with list of list

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```

---

# 🔹 3) pass Statement

👉 **`pass`** হলো একটা **placeholder statement**।

* মানে: “এখানে কিছু না লিখলেও কোড valid থাকবে।”
* ফাংশন, লুপ, কন্ডিশনে পরে কোড যোগ করার জন্য ব্যবহার হয়।

### Example 6: Empty function

```python
def todo():
    pass
```

---

### Example 7: pass inside loop

```python
for i in range(5):
    if i == 2:
        pass   # কিছু করবে না
    else:
        print(i)
```

**ব্যাখ্যা:** i==2 হলে লুপ কিছু না করে এগিয়ে যাবে।

---

### Example 8: pass inside if-else

```python
x = 10
if x > 5:
    pass   # পরে কোড লেখা হবে
else:
    print("Small number")
```

---

# ✅ সারসংক্ষেপ

* **for–else**: লুপ স্বাভাবিকভাবে শেষ হলে `else` চালায়, কিন্তু `break` হলে চালায় না।
* **nested loop**: লুপের ভিতরে আরেকটি লুপ (টেবিল, ম্যাট্রিক্স, প্যাটার্ন ইত্যাদিতে কাজে লাগে)।
* **pass**: placeholder statement—কিছু না করলেও কোড valid রাখে।

---


