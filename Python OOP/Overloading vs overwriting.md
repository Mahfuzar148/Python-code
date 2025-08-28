
---

# 🐍 Method Overloading বনাম Method Overriding (Python এ)

---

## 🔹 1. Method Overloading

**Definition:**
একই ক্লাসে একি নামের একাধিক method define করা হয়, কিন্তু parameter (argument) সংখ্যা বা টাইপ ভিন্ন হয়।

👉 অন্য ভাষা (Java, C++) তে সরাসরি সম্ভব।
👉 Python-এ **direct support নেই** → কিন্তু আমরা **default arguments**, `*args`, `**kwargs` দিয়ে simulate করতে পারি।

### 📝 Example (Pythonic Overloading)

```python
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

c = Calculator()
print(c.add(5, 10))       # 15
print(c.add(2, 3, 4))     # 9
print(c.add())            # 0
```

👉 এখানে একটাই method `add()` আছে, কিন্তু arguments ভেদে কাজ আলাদা করছে।

---

## 🔹 2. Method Overriding

**Definition:**
Inheritance এর সময় child class তার parent class এর কোনো method কে **আবার define করে দেয়**, যাকে **override** বলা হয়।

👉 Python এ **পুরোপুরি supported**।
👉 Method নাম ও parameter list একই থাকে, কিন্তু behavior নতুন হয়।

### 📝 Example (Overriding)

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

class Cat(Animal):
    def sound(self):   # overriding
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()   # Animal makes sound
d.sound()   # Dog barks
c.sound()   # Cat meows
```

👉 এখানে `sound()` method child classes নিজেদের মতো override করেছে।

---

## 🔹 3. তুলনা (Comparison Table)

| বিষয়       | **Overloading**                     | **Overriding**                         |
| ---------- | ----------------------------------- | -------------------------------------- |
| ঘটে কোথায়  | একই ক্লাসে                          | Parent → Child ক্লাসে                  |
| উদ্দেশ্য   | এক method → বিভিন্ন কাজ (args ভেদে) | Inherited method → নতুন behavior দেওয়া |
| Method নাম | একই                                 | একই                                    |
| Parameter  | আলাদা হতে পারে                      | সাধারণত parent এর মতোই                 |
| Python এ   | ❌ Directly নেই (simulate করতে হয়)   | ✅ পুরোপুরি supported                   |
| Example    | `add(a,b)`, `add(a,b,c)`            | `sound()` in Animal vs Dog vs Cat      |

---

## 🔹 4. Visual Diagram

```
Overloading (Same class)               Overriding (Parent → Child)

   Class Calculator                      Class Animal
   ------------------                    ----------------
   + add(a, b)                           + sound()  ---> "Animal makes sound"
   + add(a, b, c)     <-- একই নাম         ----------------
   ------------------                        ↑
                                             |
                                             |
                                        Class Dog
                                        ----------------
                                        + sound()  ---> "Dog barks"
```

---

## ✅ সারসংক্ষেপ

* **Overloading** → একই ক্লাসে একি নামের method, arguments ভেদে আলাদা কাজ। (Python এ simulate করা যায়)
* **Overriding** → Child class, Parent এর method কে redefine করে নিজের মতো করে কাজ করায়। (Python এ পুরোপুরি supported)

---

