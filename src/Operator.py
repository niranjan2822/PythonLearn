# Arithmetic operator :

# + -> Addition
# -  -> Subtraction
# * --> Multiplication
# / --> Division
# % --> Modules
# ** --> Exponentiation
# // --> floor division

# Modules --> %
x = 5
y = 2
print(x % y)
# output - 1

# Exponentiation
x = 2
y = 5
print(x ** y)

# Output - 32 --> 2*2*2*2*2

# floor division

x = 15
y = 2
print(x // y)

# Output - 7

# Python Assignment operator

# '='
x = 5
print(x)  # --> 5

# ' += '  Ex = x += 3  OR x = x+3
x += 3
print(x)  # --> 8

x = 5
x += 3
print(x)  # --> 8

# ' - = ' Ex - x -= 3 or x = x - 3

x = 5
x -= 3
print(x)  # --> 2

# ' *= '  Ex --> x *= 3 , or x = x * 3

x = 5
x *= 3
print(x)   # --> 15

# Python Comparison operator
# ' == ' equal  --> x == y
x = 5
y = 3
print(x == y)   # --> False

# ' != ' not equal  --> x != y
x = 5
y = 3
print(x != 3)  # --> True

# Python Logical operator
# and --> Return True if both statement are True

x = 5
print(x > 3 and x < 10)   # --> True

# or --> Return True if one of the statement is True

x = 5
print(x > 3 or x < 4)   # --> True

# not -->  Reverse the result , return false if the result is True

x = 5
print(not (x > 3 and x < 10))    # --> False

# Python Identity operator

# is --> Return True if both variables are the same object .

x = [" apple " , " banana "]
y = [" apple " , " banana "]
z = x
print(x is z)
print(x is y)
print(x == y)

# Output -
# True
# False
# True

# is not  --> Returns True if both variables are not the same object .

x = [" apple " , " banana "]
y = [" apple " , " banana "]
z = x
print(x is not z)
print(x is not y)
print(x != y)

# Output :
# False
# True
# False

# Python membership operators :
# in --> Returns True if a sequence with the specified value is present in the object

x = ["apple" , "banana"]
print("banana" in x)    # --> True

# not in --> Return True if a sequence with the specified value is not present in the object .

x = ["apple","banana"]
print("mango" not in x)  # --> True












