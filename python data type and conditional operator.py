print("Mahfuzar Rahman")
num = 24
print(int(num)*int(num))
# this is my first code
'''
this is my first commit

'''
# integer type data
num2 = 345
print(type(num2))
# floating point data
num3 = 234.56
print(type(num3))
#complex type data
num4 = 23j
print(type(num4))
name1 = "Sujan "
print(type(name1))

#boolean data tyep
bool = True
print(type(bool))
# to find a character or string  in  another string ,
# we have use ("character or string " in another string name)
name2 = "the position of University of rajshahi is second in Bangladesh "
# now we will search string "position" in name2,
# if the 'position' stay in name2 then it will return true otherwise false
find = "position" in name2
print(find)

# small calculations
n1 = input("Enter the number : ")
n2 = input("Enter the second number : ")
n1 =int(n1)
n2 = int(n2)    #integer conversion
operator = input("Enter (+,-,*,/,% ) : ")
if operator == "+" :
    print("The sum is ",n1+n2)
elif operator == "-" :
    print("The subtraction is : ",n1-n2);
elif operator == "*" :
    print("The multiplication is : ",n1*n2)
elif operator == '/'  :
    print("The quotient is ",n1//n2)
elif operator =="%":
    print("The remainder is ",n1%n2)
else :
    print("!Invalid")







