
---

# 🔹 Python User Input (Theory)

👉 Python-এ ইউজারের কাছ থেকে ইনপুট নেওয়ার জন্য ব্যবহার করা হয়:

```python
input("Enter something: ")
```

* `input()` সবসময় **string** রিটার্ন করে।
* যদি সংখ্যা দরকার হয় → `int(input())` বা `float(input())` ব্যবহার করতে হয়।
* অনেক সময় **split()** দিয়ে একসাথে একাধিক ইনপুট নেওয়া হয়।

---

# 🔹 ২০টি Example with Explanation

---

### 1) বেসিক ইনপুট

```python
name = input("Enter your name: ")
print("Hello", name)
```

**ব্যাখ্যা:** ইউজার যা লিখবে তা string আকারে `name` এ যাবে।

---

### 2) Integer Input

```python
age = int(input("Enter your age: "))
print("You are", age, "years old")
```

**ব্যাখ্যা:** `int()` ব্যবহার করে integer এ কনভার্ট করা হয়।

---

### 3) Float Input

```python
pi = float(input("Enter value of pi: "))
print("Pi =", pi)
```

**ব্যাখ্যা:** দশমিক মান `float()` দিয়ে নেওয়া হয়।

---

### 4) দুইটা সংখ্যা যোগফল

```python
a = int(input("Enter first: "))
b = int(input("Enter second: "))
print("Sum =", a+b)
```

**ব্যাখ্যা:** দুই ইনপুট যোগ করা হয়েছে।

---

### 5) এক লাইনে একাধিক ইনপুট

```python
x, y = input("Enter two words: ").split()
print(x, y)
```

**ব্যাখ্যা:** `split()` দিয়ে স্পেস অনুযায়ী আলাদা হয়।

---

### 6) একাধিক সংখ্যা (map ব্যবহার)

```python
nums = list(map(int, input("Enter numbers: ").split()))
print(nums)
```

**ব্যাখ্যা:** সব ইনপুটকে integer list এ রূপান্তর করা হয়েছে।

---

### 7) স্ট্রিং উল্টানো

```python
s = input("Enter text: ")
print("Reverse:", s[::-1])
```

**ব্যাখ্যা:** ইনপুট স্ট্রিং স্লাইস দিয়ে উল্টানো।

---

### 8) প্যালিনড্রোম চেক

```python
s = input("Enter word: ")
print("Palindrome?" , s == s[::-1])
```

**ব্যাখ্যা:** উল্টালে একই হলে palindrome।

---

### 9) গড় বের করা

```python
a, b, c = map(int, input("Enter 3 numbers: ").split())
print("Average =", (a+b+c)/3)
```

**ব্যাখ্যা:** একাধিক ইনপুট নিয়ে গড় বের করা।

---

### 10) ক্যালকুলেটর

```python
a = int(input("Enter first: "))
b = int(input("Enter second: "))
op = input("Enter operator (+,-,*,/): ")
if op == "+": print(a+b)
elif op == "-": print(a-b)
elif op == "*": print(a*b)
elif op == "/": print(a/b)
```

**ব্যাখ্যা:** অপারেটর ইনপুট অনুযায়ী কাজ করে।

---

### 11) Boolean Input

```python
val = input("Enter True/False: ") == "True"
print(val, type(val))
```

**ব্যাখ্যা:** string `"True"` লিখলে `True` বানানো হয়।

---

### 12) Character Input

```python
ch = input("Enter a character: ")[0]
print(ch)
```

**ব্যাখ্যা:** ইউজারের ইনপুট থেকে প্রথম ক্যারেক্টার নেওয়া।

---

### 13) ASCII Value

```python
ch = input("Enter a character: ")[0]
print("ASCII:", ord(ch))
```

**ব্যাখ্যা:** ইনপুট ক্যারেক্টারের ASCII ভ্যালু বের করা।

---

### 14) Password Input (mask ছাড়া)

```python
pwd = input("Enter password: ")
print("Password length:", len(pwd))
```

**ব্যাখ্যা:** পাসওয়ার্ড ইনপুট নিয়ে লেন্থ চেক করা।

---

### 15) Decimal → Binary

```python
n = int(input("Enter number: "))
print("Binary:", bin(n))
```

**ব্যাখ্যা:** ইনপুট নাম্বারকে বাইনারি আকারে কনভার্ট।

---

### 16) String → List of Words

```python
sentence = input("Enter a sentence: ")
print(sentence.split())
```

**ব্যাখ্যা:** ইনপুট বাক্যকে লিস্টে ভাগ করা।

---

### 17) Multiplication Table

```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)
```

**ব্যাখ্যা:** ইনপুট নাম্বারের নামতা প্রিন্ট করা।

---

### 18) Sum of Digits

```python
n = input("Enter number: ")
print(sum(int(d) for d in n))
```

**ব্যাখ্যা:** ইনপুট string কে digit list বানিয়ে যোগফল বের করা।

---

### 19) Even Numbers Filter

```python
nums = list(map(int, input("Enter numbers: ").split()))
even = [x for x in nums if x % 2 == 0]
print("Even:", even)
```

**ব্যাখ্যা:** ইনপুট লিস্ট থেকে জোড় সংখ্যা বের করা।

---

### 20) Grade System

```python
mark = int(input("Enter your mark: "))
if mark >= 80: print("A+")
elif mark >= 60: print("B")
else: print("Fail")
```

**ব্যাখ্যা:** ইউজারের মার্কস অনুযায়ী গ্রেড নির্ধারণ।

---

# ✅ সারসংক্ষেপ

* `input()` সবসময় **string** রিটার্ন করে।
* সংখ্যা নিতে হলে → `int()` / `float()` ব্যবহার করতে হবে।
* একাধিক ইনপুট → `split()`, `map()` দিয়ে হ্যান্ডেল করা যায়।
* ইউজার ইনপুট ব্যবহার করে ছোটখাট প্রোগ্রাম বানানো যায় যেমন ক্যালকুলেটর, টেবিল, গ্রেড সিস্টেম ইত্যাদি।

---

