# Boolean represent one of two values :
# True or False

print(10 > 9)  # --> True
print(10 == 9)  # --> False
print(10 < 9)  # --> False

# Ex :

a = 200
b = 300
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Output --> b is greater than a

# bool() --> The bool() function allows you to evaluate any value and give you  True or False in return .

# Example :

print(bool("Hello"))  # --> True
print(bool(15))  # --> True

# Evaluate two variables :

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Output - True
# Output - True

# Some values are False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Function can return a boolean

def func():
    return True


print(func())
# True
