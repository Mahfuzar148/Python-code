
---

# 🔹 Python while loop (Theory)

👉 **while loop** হলো এমন এক ধরণের লুপ যা **একটা শর্ত (condition) সত্য থাকলে বারবার চলতে থাকে**।

**Syntax:**

```python
while condition:
    # loop body
    # must update condition, otherwise infinite loop
```

### গুরুত্বপূর্ণ পয়েন্ট:

* যদি condition শুরু থেকেই False হয় → লুপ একবারও চলবে না।
* condition কে আপডেট করতে হবে → না হলে **infinite loop** হবে।
* `break`, `continue`, `else` while লুপের সাথে ব্যবহার করা যায়।

---

# 🔹 Examples of while loop

---

### 1) বেসিক while loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**ব্যাখ্যা:** ১ থেকে ৫ পর্যন্ত প্রিন্ট করবে।

---

### 2) Infinite while loop (stop with break)

```python
while True:
    cmd = input("Enter q to quit: ")
    if cmd == "q":
        break
```

**ব্যাখ্যা:** অনন্তকাল চলবে, যতক্ষণ না ইউজার `q` লিখে।

---

### 3) Countdown

```python
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast Off!")
```

**ব্যাখ্যা:** কাউন্টডাউন এর মত।

---

### 4) Sum of first n numbers

```python
n = 5
s, i = 0, 1
while i <= n:
    s += i
    i += 1
print("Sum =", s)  # 15
```

---

### 5) Factorial

```python
n = 5
fact, i = 1, 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)  # 120
```

---

### 6) Multiplication table

```python
n, i = 7, 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1
```

---

### 7) Reverse digits of number

```python
n = 1234
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print("Reversed:", rev)  # 4321
```

---

### 8) Palindrome check (number)

```python
n, orig = 121, 121
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print(orig == rev)  # True
```

---

### 9) Print characters of string with while

```python
s = "Python"
i = 0
while i < len(s):
    print(s[i])
    i += 1
```

---

### 10) Loop with else

```python
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")
```

**ব্যাখ্যা:** while লুপ condition False হয়ে শেষ হলে `else` ব্লক চালায়।

---

### 11) break in while

```python
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
```

**ব্যাখ্যা:** i=5 হলে লুপ ভেঙে যায়।

---

### 12) continue in while

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

**ব্যাখ্যা:** ৩ বাদ যাবে।

---

### 13) Guessing Game

```python
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess number: "))
print("Correct!")
```

---

### 14) Nested while loop

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
```

---

### 15) Fibonacci with while

```python
a, b, i = 0, 1, 0
while i < 7:
    print(a)
    a, b = b, a+b
    i += 1
```

---

### 16) Digits count

```python
n, count = 12345, 0
while n > 0:
    count += 1
    n //= 10
print("Digits:", count)  # 5
```

---

### 17) Even numbers filter

```python
nums = [1,2,3,4,5,6]
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        print(nums[i])
    i += 1
```

---

### 18) Reverse a list

```python
nums = [10,20,30]
i = len(nums)-1
while i >= 0:
    print(nums[i])
    i -= 1
```

---

### 19) Collatz sequence

```python
n = 6
while n != 1:
    print(n, end=" ")
    n = n//2 if n%2==0 else 3*n+1
print(1)
```

---

### 20) Pattern printing

```python
i = 1
while i <= 5:
    print("*" * i)
    i += 1
```

---

# ✅ সারসংক্ষেপ

* **while loop** চলে যতক্ষণ শর্ত True থাকে।
* Infinite loop বানানো যায় `while True` দিয়ে।
* `break`, `continue`, `else` ব্যবহার করা যায়।
* সাধারণ কাজ → কাউন্টডাউন, নাম্বার প্রসেসিং, গেম লজিক, ইউজার ইনপুট ভ্যালিডেশন।

---

