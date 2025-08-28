
---

# 🐍 Wrapper Class in Python — বিস্তারিত

---

## 🔹 Wrapper Class কী?

👉 **Wrapper Class** মানে হলো এমন একটি class যেটা আরেকটা class/object কে **"wrap" (ঘিরে রাখা)** করে এবং তার উপরে **extra functionality যোগ করে**।

* এটাকে অনেক সময় **Delegation** বা **Proxy pattern** ও বলা হয়।
* Wrapper class মূল object এর method গুলো call করে দেয় কিন্তু চাইলে তার আগে/পরে কিছু কাজ যোগ করতে পারে।

📌 উদাহরণ (বাস্তব জীবন):

* একটা Gift Box কে ধরো। ভেতরে gift আছে (মূল object)। Gift box হলো wrapper → যা packaging, decoration করে বাড়তি সুবিধা দেয়।

---

## 🔹 Wrapper Class এর উদ্দেশ্য

1. **Extra functionality যোগ করা**
2. **Encapsulation** (ভেতরের object লুকানো)
3. **Logging / Debugging**
4. **Access control**
5. **Decorator pattern implement করা**

---

## 📝 Example 1: Basic Wrapper Class

```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("Name:", self.name)

# Wrapper Class
class StudentWrapper:
    def __init__(self, student):
        self._student = student   # original object wrap করা হলো
    
    def show(self):
        print("Before showing student")  # extra কাজ
        self._student.show()             # আসল method call
        print("After showing student")   # extra কাজ

s = Student("Rahim")
sw = StudentWrapper(s)
sw.show()
```

👉 Output:

```
Before showing student
Name: Rahim
After showing student
```

---

## 📝 Example 2: Wrapper for Logging

```python
class Calculator:
    def add(self, a, b):
        return a + b

class CalculatorWrapper:
    def __init__(self, calc):
        self.calc = calc
    
    def add(self, a, b):
        print(f"Adding {a} and {b}")  # logging
        result = self.calc.add(a, b)
        print(f"Result = {result}")
        return result

c = Calculator()
cw = CalculatorWrapper(c)
cw.add(10, 20)
```

👉 Output:

```
Adding 10 and 20
Result = 30
```

---

## 📝 Example 3: Wrapper for Access Control

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

# Wrapper with Access Control
class SecureAccount:
    def __init__(self, account, password):
        self._account = account
        self._password = password
    
    def get_balance(self, password):
        if password == self._password:
            return self._account.get_balance()
        else:
            print("Access Denied!")

acc = BankAccount(5000)
secure_acc = SecureAccount(acc, "1234")

print(secure_acc.get_balance("1234"))   # ✅ 5000
print(secure_acc.get_balance("wrong"))  # ❌ Access Denied!
```

---

## 📝 Example 4: Using `__getattr__` for Auto-Delegation

👉 Python এ wrapper class বানাতে `__getattr__` method ব্যবহার করা যায় যাতে আসল object এর সব method auto-forward হয়।

```python
class Original:
    def greet(self):
        print("Hello from Original")

class Wrapper:
    def __init__(self, obj):
        self._obj = obj
    
    def __getattr__(self, name):
        # যদি wrapper এ method না থাকে → original এরটা use হবে
        return getattr(self._obj, name)

o = Original()
w = Wrapper(o)
w.greet()   # "Hello from Original"
```

---

## 🔹 Wrapper Class এর ব্যবহার ক্ষেত্র

* **Decorator pattern** (extra feature যোগ করা)
* **Adapter pattern** (incompatible class কে compatible বানানো)
* **Logging / Monitoring**
* **Security (access control)**
* **Resource management (database, file)**

---

## 🔹 Wrapper Class বনাম Normal Class

| বিষয়       | Normal Class                      | Wrapper Class                           |
| ---------- | --------------------------------- | --------------------------------------- |
| কাজ        | নিজের functionality implement করে | অন্য object কে wrap করে তার উপর কাজ করে |
| Dependency | Self-contained                    | অন্য class/object এর উপর নির্ভরশীল      |
| Example    | `Student`, `BankAccount`          | `StudentWrapper`, `SecureAccount`       |

---

# ✅ সারসংক্ষেপ

* **Wrapper Class** হলো এমন class যা অন্য object কে ঘিরে ধরে।
* মূল কাজ → আসল object এর কাজ চালানো + extra কাজ যোগ করা।
* Python এ wrapper বানানো যায় সাধারণ delegation, `__getattr__` বা decorator দিয়ে।
* ব্যবহার হয়: logging, security, monitoring, design patterns ইত্যাদিতে।

---

