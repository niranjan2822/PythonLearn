x = 1
y = "abc"
print(x)
print(y)

x = 4
x = "abc"
print(x)

x = 'john'
x = "john"
print(x)

_my_name = "niranjan"
print(_my_name)

# my-name = "Niranjan" -- > Not allowed --   ^SyntaxError: can't assign to operator
# print(my-name)

# Assign value to multiple variables
x, y, z = "apple", "orange", "banana"
print(x)
print(y)
print(z)
print(x, y, z)

# Assign the same value to multiple variables in one line
x = y = z = "apple"
print(x)
print(y)
print(z)
print(x, y, z)

# To combine both text and a variable using + character

x = "awesome"
print("Python is " + x)

# It can also use the + character to add a variable to another variable

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)
print(x + y)
print(x)

# If we try to combine a string and a number python will give an error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# x = 5
# y = "Niranjan"
# print(x + y)

# Global variables can be used by everyone , both inside of functions and outside

x = "awesome"


def func():
    print("Python is " + x)


func()

# Creating a variable inside a function with the same name as the global variable

x = "awesome"


def func():
    x = "fantastic 1"
    print("Python is " + x)


func()
print("Python is " + x)


# Create a global variable inside a function we can use the global keyword

def func():
    global x
    x = "fantastic 2"


func()
print("Python is " + x)

# To change the value of a global variable inside a function , refer to the variable by using the global keyword

x = "awesome"


def func():
    global x
    x = "fantastic 5"


func()
print("Python is " + x)


