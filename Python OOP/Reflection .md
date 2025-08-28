
---

# 🐍 Reflection in Python — বিস্তারিত

---

## 🔹 Reflection কী?

👉 **Reflection** হলো এমন একটি process যেখানে প্রোগ্রাম **runtime এ নিজেকে পরীক্ষা (inspect)** করতে পারে এবং প্রয়োজনে **নিজেকে পরিবর্তন**ও করতে পারে।

📌 সহজভাবে:

* Reflection → "নিজেকে দেখা"
* মানে হলো object / class এর property, methods, type, attributes runtime এ বের করা এবং manipulate করা।

---

## 🔹 Reflection দিয়ে কী কী করা যায়?

1. কোনো object/class এর **type** বের করা
2. Object এ **কোন attributes/methods আছে** তা বের করা
3. **Dynamic ভাবে attributes/methods access** করা
4. **Runtime এ নতুন attributes add করা**

---

## 🔹 Python এ Reflection Tools

Python এ reflection করার জন্য কিছু built-in function আছে:

* `type(obj)` → object এর type দেয়
* `id(obj)` → object এর unique identity (address-like) দেয়
* `dir(obj)` → object এর সব attributes/methods এর list দেয়
* `getattr(obj, name)` → attribute value বের করে
* `setattr(obj, name, value)` → attribute সেট করে
* `hasattr(obj, name)` → attribute আছে কিনা check করে
* `callable(obj)` → object callable কিনা দেখে
* `__dict__` → object এর attributes dictionary আকারে দেয়

---

## 📝 Example 1: type() এবং id()

```python
x = [1,2,3]
print(type(x))   # <class 'list'>
print(id(x))     # unique identity (memory address-like)
```

---

## 📝 Example 2: dir()

```python
class Student:
    def __init__(self, name):
        self.name = name
    def show(self):
        return f"Name: {self.name}"

s = Student("Rahim")
print(dir(s))   # সব method + attribute এর list
```

---

## 📝 Example 3: getattr(), setattr(), hasattr()

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("Karim", 50000)

print(getattr(e, "name"))   # Karim
print(hasattr(e, "age"))    # False

setattr(e, "age", 25)       # নতুন attribute যোগ হলো
print(e.age)                # 25
```

👉 এখানে `age` attribute আগে ছিল না, কিন্তু runtime এ যোগ করা হলো।

---

## 📝 Example 4: **dict** দিয়ে Reflection

```python
print(e.__dict__)
```

👉 Output:

```
{'name': 'Karim', 'salary': 50000, 'age': 25}
```

---

## 📝 Example 5: callable()

```python
print(callable(e))          # False (object callable নয়)
print(callable(e.__init__)) # True (method callable)
```

---

## 📝 Example 6: Reflection in Function

```python
def greet():
    return "Hello"

print(callable(greet))   # True
print(greet.__name__)    # greet
```

---

## 🔹 Advanced: Reflection + Dynamic Method Call

```python
class Math:
    def add(self, a, b):
        return a+b
    def mul(self, a, b):
        return a*b

m = Math()

method_name = "mul"
print(getattr(m, method_name)(5, 6))   # 30
```

👉 এখানে method নাম string আকারে runtime এ পাঠানো হয়েছে, `getattr` দিয়ে সেই method call করা হলো।

---

## 🔹 Reflection এর ব্যবহার ক্ষেত্র

1. **Debugging & Introspection** → object এর ভেতর কী আছে দেখা
2. **Frameworks (Django, Flask)** → class/method dynamically load করা
3. **Serialization/Deserialization** → object কে JSON এ রূপান্তর
4. **Dynamic method dispatch** → string দিয়ে method কল করা
5. **Plugin systems** → runtime এ external code লোড করা

---

## 🔹 Reflection বনাম Introspection

| বিষয়       | Reflection                              | Introspection                     |
| ---------- | --------------------------------------- | --------------------------------- |
| Definition | Object কে runtime এ দেখা ও পরিবর্তন করা | শুধু object কে দেখা (পরিবর্তন নয়) |
| Scope      | Inspect + Modify                        | Inspect only                      |
| Example    | getattr, setattr                        | type, dir                         |

---

# ✅ সারসংক্ষেপ

* **Reflection** = প্রোগ্রাম runtime এ নিজের structure কে দেখা ও modify করা।
* Python এ reflection functions → `type()`, `id()`, `dir()`, `getattr()`, `setattr()`, `hasattr()`, `callable()`, `__dict__`।
* ব্যবহার: Debugging, Frameworks, Plugin system, Dynamic method call।
* Introspection = শুধু দেখা, Reflection = দেখা + পরিবর্তন করা।

---

