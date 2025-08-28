
---

# 🐍 Python Access Modifiers — বিস্তারিত

👉 **Access Modifiers** হলো এমন কিছু রুল (বা convention) যেগুলো দিয়ে আমরা ঠিক করি কোন class attribute/method কোথা থেকে access করা যাবে।
👉 Python-এ মূলত ৩ ধরনের access modifier আছে:

1. **Public**
2. **Protected**
3. **Private**

(অন্যান্য ভাষা যেমন Java, C++ এ এগুলো **strictly enforced**, কিন্তু Python-এ এগুলো **convention based** অর্থাৎ developer দের জন্য "signal", পুরোপুরি ব্লক করে না।)

---

## 1️⃣ Public Members (ডিফল্ট)

* Python-এ সব attribute/method by default **public**।
* এগুলোকে class এর ভিতরে ও বাইরে সব জায়গা থেকে access করা যায়।

```python
class Student:
    def __init__(self, name, age):
        self.name = name      # public attribute
        self.age = age
    
    def show(self):           # public method
        print(f"{self.name}, {self.age}")

s = Student("Rahim", 20)
print(s.name)     # বাইরে থেকেও পাওয়া যাচ্ছে
s.show()
```

✅ Public → সবার জন্য উন্মুক্ত।

---

## 2️⃣ Protected Members (`_single_underscore`)

* নামের আগে `_` দিলে বোঝানো হয় যে এটা **protected**।
* Convention: এগুলোকে class বা subclass থেকে ব্যবহার করা যাবে, কিন্তু বাইরে থেকে সরাসরি ব্যবহার না করাই ভালো।

```python
class Employee:
    def __init__(self, name, salary):
        self._salary = salary   # protected attribute
        self.name = name

    def _show_salary(self):     # protected method
        print(f"{self.name} earns {self._salary}")

class Manager(Employee):
    def show(self):
        print("Manager salary:", self._salary)  # subclass এ ব্যবহার করা যাবে

e = Employee("Karim", 25000)
print(e._salary)   # ⚠ যদিও access করা যাচ্ছে, convention অনুযায়ী বাইরে থেকে ব্যবহার না করা উচিত
```

✅ Protected → "আংশিক সুরক্ষিত" (subclass এ OK, বাইরে থেকে avoid করতে হবে)।

---

## 3️⃣ Private Members (`__double_underscore`)

* নামের আগে `__` (double underscore) দিলে সেটা **private** হয়ে যায়।
* Class এর বাইরে থেকে সরাসরি access করা যায় না।
* Python এ এটা **name mangling** করে রাখে → attribute এর নাম পরিবর্তন হয়ে যায় `_ClassName__var` আকারে।

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def __show_balance(self):      # private method
        print("Balance:", self.__balance)

    def access_balance(self):      # public method দিয়ে access করা যাবে
        self.__show_balance()

acc = BankAccount(5000)
# print(acc.__balance)       ❌ AttributeError
print(acc._BankAccount__balance)  # ✅ name mangling দিয়ে পাওয়া যাবে
acc.access_balance()              # ✅ public method দিয়ে access
```

✅ Private → বাইরে থেকে সরাসরি পাওয়া যাবে না, শুধু class এর ভেতরে।

---

## 🔹 Access Modifiers একসাথে

```python
class Demo:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"
    
    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

d = Demo()
print(d.public_var)       # Public (সবার জন্য উন্মুক্ত)
print(d._protected_var)   # Protected (warning: বাইরে থেকে avoid করা উচিত)
# print(d.__private_var)  # ❌ Error
print(d._Demo__private_var) # ✅ name mangling
```

---

## 🔹 Access Modifiers Summary

| Type          | Declaration Style | Access Level                                                                        | উদাহরণ                |
| ------------- | ----------------- | ----------------------------------------------------------------------------------- | --------------------- |
| **Public**    | `var`             | Class এর ভেতরে ও বাইরে সব জায়গায় ব্যবহারযোগ্য                                       | `obj.var`             |
| **Protected** | `_var`            | Class এবং Subclass এ ব্যবহারযোগ্য (কিন্তু conventionally বাইরে থেকে avoid করতে হবে) | `obj._var`            |
| **Private**   | `__var`           | শুধুমাত্র Class এর ভেতরে ব্যবহারযোগ্য, বাইরে থেকে সরাসরি access করা যাবে না         | `obj._ClassName__var` |

---

# ✅ সারসংক্ষেপ

* **Public** → ডিফল্ট, সবখানে ব্যবহার করা যায়।
* **Protected (`_`)** → subclass এ ব্যবহার OK, বাইরে থেকে avoid করা convention।
* **Private (`__`)** → class এর বাইরে থেকে সরাসরি ব্যবহার করা যায় না, শুধু ভেতরে।
* Python এ access modifiers **convention based**, strict নয়।

---

