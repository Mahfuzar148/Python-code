
---

# 🐍 Python Static Method — বিস্তারিত

---

## 🔹 Static Method কী?

* Static method হলো এমন method যেটা **class বা object এর সাথে bound হয় না**।
* সাধারণ method (instance method) এর মতো **self** বা class method এর মতো **cls** parameter নেয় না।
* এগুলো **@staticmethod** decorator ব্যবহার করে declare করা হয়।
* Static method সাধারণত **utility/helper function** হিসেবে কাজ করে (যেমন: data process, calculation ইত্যাদি)।

---

## 🔹 Syntax

```python
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # কোনো instance বা class variable লাগবে না
        return arg1 + arg2
```

---

## 📝 Example 1: Basic Static Method

```python
class MathOps:
    @staticmethod
    def add(a, b):   # static method
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathOps.add(5, 7))        # 12
print(MathOps.multiply(3, 4))   # 12
```

👉 এখানে static method সরাসরি class থেকে কল করা হয়েছে।
👉 কোনো object বানানোর দরকার হয়নি।

---

## 📝 Example 2: Static Method object দিয়েও কল করা যায়

```python
class Utility:
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

u1 = Utility()
u1.greet("Rahim")         # object দিয়েও কল করা যায়
Utility.greet("Karim")    # class দিয়েও কল করা যায়
```

👉 static method একই থাকে, object যত বানানো হোক না কেন আলাদা কপি তৈরি হয় না।

---

## 📝 Example 3: Class এর ভেতর Utility Function

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

print(Temperature.celsius_to_fahrenheit(30))   # 86.0
print(Temperature.fahrenheit_to_celsius(86))   # 30.0
```

👉 এখানে static method কনভার্সন করছে, কিন্তু class বা object এর কোনো data ব্যবহার করছে না।

---

## 📝 Example 4: Static Method বনাম Instance/Class Method

```python
class Demo:
    value = 100   # class attribute
    
    def __init__(self, x):
        self.x = x   # instance attribute
    
    def instance_method(self):     # instance method
        return self.x
    
    @classmethod
    def class_method(cls):         # class method
        return cls.value
    
    @staticmethod
    def static_method(a, b):       # static method
        return a + b

d = Demo(50)
print(d.instance_method())     # 50  -> object data use করছে
print(Demo.class_method())     # 100 -> class data use করছে
print(Demo.static_method(2,3)) # 5   -> শুধু arguments use করছে
```

---

## 📝 Example 5: Validation Example

```python
class Validator:
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 100

print(Validator.is_valid_age(25))   # True
print(Validator.is_valid_age(150))  # False
```

👉 Static method ব্যবহার হয় **data validation বা utility check** করার জন্য।

---

## 🔹 Static Method এর বৈশিষ্ট্য

1. **self / cls নেয় না** → instance বা class data access করতে পারে না।
2. **Independent থাকে** → শুধু দেওয়া arguments ব্যবহার করে।
3. **Call করা যায়** → ClassName.method() অথবা object.method() দিয়ে।
4. **Efficient** → কারণ class/object level memory use করে না, সব object share করে।
5. **Utility/Helper functions** এর জন্য আদর্শ।

---

## 🔹 Static Method বনাম Class Method বনাম Instance Method

| ধরন             | Decorator       | প্রথম Parameter | Access করতে পারে                       | কল করার ধরন                        |
| --------------- | --------------- | --------------- | -------------------------------------- | ---------------------------------- |
| Instance Method | কিছু নেই        | `self`          | Instance attributes + Class attributes | `obj.method()`                     |
| Class Method    | `@classmethod`  | `cls`           | Class attributes                       | `Class.method()` বা `obj.method()` |
| Static Method   | `@staticmethod` | কিছু নেই        | কিছুই না (শুধু arguments)              | `Class.method()` বা `obj.method()` |

---

# ✅ সারসংক্ষেপ

* **Static Method** হলো এমন method যেটা **class বা object এর data ব্যবহার করে না**।
* এগুলো **@staticmethod** দিয়ে declare করা হয়।
* সাধারণত **utility/helper কাজ** (যেমন math, validation, conversion) এর জন্য ব্যবহার হয়।
* Instance method → `self`, Class method → `cls`, Static method → কিছুই নেয় না।

---

