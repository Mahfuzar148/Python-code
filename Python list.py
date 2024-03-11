subjecst =["C","C++","Python","Java","TOC","Bangla"]
print(subjecst)

for sub in subjecst :
    print(sub)
print(subjecst[0])

print(subjecst[1 : ]) # all element will be printed from index 1
print(subjecst[-1]) # Negative index indicate end of the list or reverse order

# check whether an element exist in the list or not using 'in' operator  and 'not in' operator.

print("Python" in subjecst)

print("English " in subjecst)

print("English" not in subjecst)


#add elemnet into list

subjecst + ["Algorithm","Data Structure"]
print("List after Adding : ",subjecst)

#length calculation of list
print(len(subjecst))

# add element into list using append() function
subjecst.append("Compiler design")
print("Element of list after adding by using append() function : ",subjecst)
#insert element in a particular position
subjecst.insert(2,"Data science")

print("List after inserting : ",subjecst)
# remove element from list
subjecst.remove("Data science")
print(" list after removing : ",subjecst)
#sorting a list

subjecst.sort()

print("List after sorting : ", subjecst)

#reversing of a list

subjecst.reverse()

print("List after reversing : ",subjecst)

#pop() function remove element from the end of the list one by one

subjecst.pop()
print(" List after calling pop() function : ", subjecst)
#copy a list into another

subjects1 = subjecst.copy()

print("subjects1 : ",subjects1)

#get index number of a particular element of a list
print("Index of 'TOC' ",subjects1.index("TOC"))

# count frequency of an element
print(" frequncy of 'TOC' : ",subjects1.count("TOC"))
# clear() function clear all element from the list


subjecst.clear()
print("list after calling clear function() : ",subjecst)


