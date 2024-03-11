dictionary = {"name" : "Mahfuzar Rahman","age":24,"DOB": 2000}
d2 = {(2,3) : "This is a tuple",3.5 : "Floating number"}

print(d2)
print(dictionary)

print(dictionary["name"])
print(d2[(2,3)])

#length calculation
l1 = len(dictionary)
print(l1)

#copy

dictionary1 = dictionary

print(dictionary1)

#add element into dictionary
dictionary["University"] =  "University of Rajshahi"
print(dictionary)

# delete element of dictionary
dictionary.pop("University")
print(dictionary)

#clear all element of dictionary using clear function

dictionary1.clear()

print(dictionary1)  # all element of dictionary1 has removed after using clear function
#show an element of dictionary using get() function
print(d2.get(3.5))
# show all element of a dictionary by calling  items() function
print(d2.items())

#show all key of dictionary by calling key() function
print(d2.keys())
# delete dictionary using del function
del dictionary1
print(dictionary1)



