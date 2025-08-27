
---

# 📌 Python Set (Overview)

➡️ **Set** হলো একটি **unordered collection** যেখানে **unique (ডুপ্লিকেট ছাড়া)** এলিমেন্ট থাকে।
➡️ `{}` বা `set()` দিয়ে তৈরি করা হয়।

```python
myset = {1, 2, 3, 4}
print(myset)   # {1, 2, 3, 4}
```

---

# 📌 Set এর Built-in Methods/Functions (List)

1. `add()`
2. `update()`
3. `remove()`
4. `discard()`
5. `pop()`
6. `clear()`
7. `copy()`
8. `union()` (`|`)
9. `intersection()` (`&`)
10. `difference()` (`-`)
11. `symmetric_difference()` (`^`)
12. `issubset()`
13. `issuperset()`
14. `isdisjoint()`

---

# 🔎 প্রতিটি Function এর Example + ব্যাখ্যা

---

## 1. `add()`

একটি নতুন element যোগ করে।

```python
s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}
```

---

## 2. `update()`

একসাথে একাধিক element যোগ করে (list, tuple, set ইত্যাদি থেকে)।

```python
s = {1, 2}
s.update([3, 4, 5])
print(s)   # {1, 2, 3, 4, 5}
```

---

## 3. `remove()`

নির্দিষ্ট element মুছে ফেলে। element না থাকলে `KeyError` দেয়।

```python
s = {1, 2, 3}
s.remove(2)
print(s)   # {1, 3}
# s.remove(5)  # ❌ Error: KeyError
```

---

## 4. `discard()`

`remove()` এর মতো, কিন্তু element না থাকলে error দেয় না।

```python
s = {1, 2, 3}
s.discard(2)
s.discard(5)  # error হবে না
print(s)   # {1, 3}
```

---

## 5. `pop()`

র‍্যান্ডমভাবে একটি element মুছে ফেলে ও return করে।

```python
s = {10, 20, 30}
val = s.pop()
print(val)   # যেকোনো একটি number (ধরা যাক 10)
print(s)     # বাকি element গুলো
```

---

## 6. `clear()`

সব element মুছে ফেলে, ফাঁকা set হয়ে যায়।

```python
s = {1, 2, 3}
s.clear()
print(s)   # set()
```

---

## 7. `copy()`

একটি shallow copy (নতুন set) তৈরি করে।

```python
s = {1, 2, 3}
c = s.copy()
print(c)   # {1, 2, 3}
```

---

## 8. `union()` বা `|`

দুটি set এর সব element (ডুপ্লিকেট ছাড়া) return করে।

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)       # {1, 2, 3, 4, 5}
```

---

## 9. `intersection()` বা `&`

দুটির common element return করে।

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
print(a & b)              # {2, 3}
```

---

## 10. `difference()` বা `-`

প্রথম set এ আছে কিন্তু দ্বিতীয়টিতে নেই।

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)            # {1, 2}
```

---

## 11. `symmetric_difference()` বা `^`

যে element দুটি set এ মিলছে না, শুধু ভিন্নগুলো return করে।

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)                      # {1, 2, 4, 5}
```

---

## 12. `issubset()`

একটা set অন্যটার মধ্যে পুরোপুরি আছে কি না চেক করে।

```python
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))   # True
print(b.issubset(a))   # False
```

---

## 13. `issuperset()`

একটা set অন্যটাকে পুরোপুরি contain করছে কি না।

```python
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))   # True
print(b.issuperset(a))   # False
```

---

## 14. `isdisjoint()`

দুটি set এর মধ্যে কোনো common element নেই কি না।

```python
a = {1, 2}
b = {3, 4}
c = {2, 5}
print(a.isdisjoint(b))  # True (কোনো মিল নেই)
print(a.isdisjoint(c))  # False (2 মিল আছে)
```

---

# ✅ Quick Summary Table

| Method                       | কাজ                                       |
| ---------------------------- | ----------------------------------------- |
| `add()`                      | একটি element যোগ করা                      |
| `update()`                   | একাধিক element যোগ                        |
| `remove()`                   | element মুছে ফেলে (না থাকলে error)        |
| `discard()`                  | element মুছে ফেলে (না থাকলে error দেয় না) |
| `pop()`                      | র‍্যান্ডম element মুছে ফেলে               |
| `clear()`                    | সব element মুছে ফেলে                      |
| `copy()`                     | নতুন copy তৈরি                            |
| `union()` \|                 | দুটি set merge                            |
| `intersection()` `&`         | common element                            |
| `difference()` `-`           | প্রথমটায় আছে কিন্তু দ্বিতীয়টায় নেই        |
| `symmetric_difference()` `^` | শুধু ভিন্ন element                        |
| `issubset()`                 | subset কি না                              |
| `issuperset()`               | superset কি না                            |
| `isdisjoint()`               | কোনো common নেই কি না                     |

---

