
---

# 📘 Python Dictionary Full Guide (সব টপিক কাভার করা)

---

## 1. **Python - Dictionaries (Basics)**

👉 Dictionary হলো key\:value data structure।

```python
student = {
    "name": "Rahim",
    "age": 21,
    "cgpa": 3.75
}
print(student["name"])   # Rahim
```

---

## 2. **Access Dictionary Items**

```python
info = {"name":"Karim", "age":20}
print(info["name"])        # Karim
print(info.get("age"))     # 20
print(info.get("cgpa", 0)) # Key না থাকলে default 0
```

---

## 3. **Change Dictionary Items**

```python
student = {"name":"Rahim", "age":21}
student["age"] = 22
print(student)  # {'name':'Rahim','age':22}
```

---

## 4. **Add Dictionary Items**

```python
student = {"name":"Sami"}
student["cgpa"] = 3.9
print(student)  # {'name':'Sami', 'cgpa':3.9}
```

---

## 5. **Remove Dictionary Items**

```python
data = {"a":1, "b":2, "c":3}
data.pop("b")
print(data)   # {'a':1, 'c':3}

data.popitem()   # শেষের key:value মুছে দেয়
del data["a"]    # নির্দিষ্ট key মুছে ফেলা
print(data)
```

---

## 6. **Dictionary View Objects (keys, values, items)**

```python
student = {"name":"Karim", "age":21}
print(student.keys())    # dict_keys(['name','age'])
print(student.values())  # dict_values(['Karim',21])
print(student.items())   # dict_items([('name','Karim'),('age',21)])
```

---

## 7. **Loop Dictionaries**

```python
data = {"a":1, "b":2, "c":3}

for k in data:                 # শুধু key
    print(k)

for v in data.values():        # শুধু value
    print(v)

for k,v in data.items():       # key-value একসাথে
    print(k, v)
```

---

## 8. **Copy Dictionaries**

```python
a = {"x":10, "y":20}
b = a.copy()
print(b)  # {'x':10,'y':20}
```

---

## 9. **Nested Dictionaries**

```python
students = {
  "101": {"name":"Rahim", "age":21},
  "102": {"name":"Karim", "age":22}
}

print(students["101"]["name"])   # Rahim
```

---

## 10. **Dictionary Methods**

👉 সব মেথড একসাথে:

* `clear()` → dict খালি
* `copy()` → shallow copy
* `fromkeys()` → keys থেকে dict বানানো
* `get()` → safe access
* `items()` → key,value tuple
* `keys()` → সব key
* `values()` → সব value
* `pop()` → নির্দিষ্ট key মুছে ফেলা
* `popitem()` → শেষের key\:value মুছে ফেলা
* `setdefault()` → key না থাকলে default সেট করা
* `update()` → অন্য dict দিয়ে merge/update

---

## 11. **Dictionary Exercises (প্র্যাকটিস আইডিয়া)**

✅ কিছু সাধারণ অনুশীলন:

1. একটি dict এ সব value এর যোগফল বের করো।
2. দুটি dict merge করো।
3. dict থেকে সর্বোচ্চ value কোন key তে আছে বের করো।
4. nested dict এ student এর average cgpa বের করো।

---

# ✅ সারসংক্ষেপ (সব টপিক কাভার্ড)

* Dictionary Basics
* Access, Change, Add, Remove items
* View Objects (keys, values, items)
* Looping over dictionaries
* Copy dictionaries
* Nested dictionaries
* Dictionary methods (11টি function)
* Exercises for practice

---


## 🔹 Dictionary Methods (সবগুলোর নাম আগে লিস্টে)

| Method         | কাজ                                 |
| -------------- | ----------------------------------- |
| `clear()`      | dictionary খালি করে                 |
| `copy()`       | shallow copy করে                    |
| `fromkeys()`   | নতুন dict বানায় keys দিয়ে         |
| `get()`        | key এর মান safely বের করে           |
| `items()`      | (key, value) pair tuple আকারে দেয়  |
| `keys()`       | সব key রিটার্ন করে                  |
| `values()`     | সব value রিটার্ন করে                |
| `pop()`        | key দিয়ে মান মুছে দেয়             |
| `popitem()`    | শেষের (key, value) মুছে দেয়        |
| `setdefault()` | key না থাকলে default ভ্যালু সেট করে |
| `update()`     | অন্য dict দিয়ে আপডেট করে           |

---

## 🔹 প্রতিটি Method এর Example + ব্যাখ্যা

---

### 1. `clear()`

```python
data = {"a":1, "b":2}
data.clear()
print(data)   # {}
```

➡️ dict একদম খালি হয়ে যায়।

---

### 2. `copy()`

```python
data = {"x":10, "y":20}
new_data = data.copy()
print(new_data)   # {'x': 10, 'y': 20}
```

➡️ আলাদা copy তৈরি হয় (shallow copy)।

---

### 3. `fromkeys()`

```python
keys = ["id", "name", "age"]
new_dict = dict.fromkeys(keys, None)
print(new_dict)  
# {'id': None, 'name': None, 'age': None}
```

➡️ keys থেকে নতুন dict বানায়, ডিফল্ট value সেট করা যায়।

---

### 4. `get()`

```python
student = {"name": "Sami", "age": 22}
print(student.get("name"))    # Sami
print(student.get("cgpa", 0)) # 0 (কারণ cgpa নেই)
```

➡️ `get()` ব্যবহার করলে error হয় না, default value দেওয়া যায়।

---

### 5. `items()`

```python
info = {"a":1, "b":2}
print(info.items())  # dict_items([('a',1), ('b',2)])

for k,v in info.items():
    print(k, v)
```

➡️ key-value জোড়া tuple আকারে দেয়।

---

### 6. `keys()`

```python
student = {"name":"Rahim", "age":21}
print(student.keys())   # dict_keys(['name','age'])
```

➡️ সব key দেখা যায়।

---

### 7. `values()`

```python
student = {"name":"Rahim", "age":21}
print(student.values())   # dict_values(['Rahim', 21])
```

➡️ সব value দেখা যায়।

---

### 8. `pop()`

```python
data = {"x":100, "y":200}
removed = data.pop("x")
print(removed)  # 100
print(data)     # {'y':200}
```

➡️ নির্দিষ্ট key মুছে দেয় এবং value রিটার্ন করে।

---

### 9. `popitem()`

```python
data = {"a":1, "b":2, "c":3}
item = data.popitem()
print(item)   # ('c',3) (শেষের আইটেম)
```

➡️ শেষের key-value pair মুছে দেয়।

---

### 10. `setdefault()`

```python
student = {"name":"Karim"}
print(student.setdefault("age", 20))  # 20
print(student)  # {'name': 'Karim', 'age':20}
```

➡️ key না থাকলে সেট করে, থাকলে পুরনো value রাখে।

---

### 11. `update()`

```python
a = {"x":1, "y":2}
b = {"y":5, "z":10}
a.update(b)
print(a)  # {'x':1, 'y':5, 'z':10}
```

➡️ dict merge/modify করে।

---

## 🔹 Extra Dictionary Tricks

### Dictionary Comprehension

```python
squares = {x: x*x for x in range(1,6)}
print(squares)  
# {1:1, 2:4, 3:9, 4:16, 5:25}
```

---

### Nested Dictionary

```python
students = {
    "101": {"name":"Rahim", "age":21},
    "102": {"name":"Karim", "age":22}
}
print(students["101"]["name"])   # Rahim
```

---

### Dictionary Loop

```python
data = {"a":1, "b":2, "c":3}
for key in data:
    print(key, ":", data[key])
```

---

# ✅ সারসংক্ষেপ

👉 Dictionary methods:
`clear, copy, fromkeys, get, items, keys, values, pop, popitem, setdefault, update`

👉 ব্যবহার:

* **Store data in key\:value**
* **Safe access** (`get`)
* **Dynamic add/remove** (`update, pop, setdefault`)
* **Iteration** (`keys, values, items`)

---

