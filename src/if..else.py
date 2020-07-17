# python --> if..else
# Ex --> if statement

a = 33
b = 200
if b > a:
    print("b is greater than a")

# output --> b is greater than a

# elif --> The elif keyword is python way of saying if the previous condition were not True , then try thi condition .
# Ex :
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# output - a and b are equal

# Else --> The else keyword catches anything which is not caught by the preceding conditions .

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Output --> a is greater than b

# We can also have an else without the elif :

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# Short hand --> if..else :
# If you have only one statement to execute for if and one for else , we can put it all on the same line .

a = 2
b = 330
print("A") if a > b else print("B")  # --> B

# short hand --> if
# if you have only one statement to execute we can put it on the same line as if the statement .
a = 220
b = 33
if a > b: print("a is greater than b")  # --> a is greater than b --> this technique is called ternary operators .

# short hand --> we can also have multiple else statement on same line
a = 330
b = 330
print("A") if a > b else print('=') if a == b else print("B")
# Output --> =

# 'and' keyword --> The and keyword is a logical operator and is used to combine conditional statement

a = 200
b = 33
c = 500
if a > b and c > a :
    print("Both condition are True")

# Output : Both condition are True

# 'or' keyword --> The or keyword is a logical operator , and is used to combine conditional statement .
a = 200
b = 33
c = 500
if a > b or a > c :
    print("At least one of the condition is True")
# output -> At least one of the condition is True

# nested if : we can have if statement inside if statements , this is called nested if statements .

x = 41
if x > 10:
    print("Above ten")
    if x > 20 :
        print("and also above 20 ")
    else:
        print("but not above 20")

# Output -->
# Above ten
# and also above 20

# The pass statement :
# If statement can not be empty , but if you for some reason have an if statement with no content , put in the pass
# statement to avoid getting an error

a = 33
b = 200
if b > a:
    pass   # --> Output -- blank


