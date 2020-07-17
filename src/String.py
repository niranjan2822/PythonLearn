# Python Strings
# "" , ''

print("Hello")
print('hello')

# Assign String to a variable

a = "Hello world "
print(a)

# Multiline strings:
a = """we can assign a multiline string to a variable"""
print(a)

a = '''we can assign a multiline string to a variable'''
print(a)

# Strings are arrays
# Ex - Get the character at position 1

x = "Hello world"
print(x[0])
print(x[1])
print(x[5])
print(x[6])
print(x[8])
# print(x[11])  # --> IndexError: string index out of range

# Slicing :
# Get the characters from position 2 to position 5 (not included)

a = "Helloworld"
print(a[2:5])  # --> llo
print(a[2:6])  # --> llow
print(a[2:7])  # --> llowo

a = "Bangalore"
print(a[2:7])

# Negative Indexing

# Get the character from position 5 to position 1 , starting the count from the end of the string .

a = "Helloworld"
print(a[-5:-1])  # --> worl
print(a[-4:-2])  # --> or
print(a[-6:-3])  # --> owo

a = "Hello world"
print(a[-5:-1])  # --> worl
print(a[-4:-2])  # --> or
print(a[-6:-3])  # -->   wo  (with space wo)

# String Length :
# To get the length of a string use the len() function

a = "Hello World"
print(len(a))

# 11

a = "HelloWorld"
print(len(a))

# 10

# String Methods

# 1. strip() --> Removes whitespace from the beginning or the end

a = " Hello World "
print(a)

a = " Hello World "
print(a.strip())

# 2. lower() --> String in lower case

a = "HELLO World"
print(a.lower())

# 3. replace()  --> replace a string with another string

a = "Hello World"
print(a.replace('H', 'Z'))  # --> H is old string , new one is z  --> Zello World

# 4. split() --> its the separator

a = "Helloworld"
b = a.split(",")
print(b)

# output--> ['Helloworld']


a = "Hello , world"
b = a.split(",")
print(b)
# Output --> ['Hello ', ' world']


# Check string  --> in and not in
# Check if the phrase "ain" is present in the following text :

txt = " The rain in spain"
x = "ain" in txt
print(x)

# output --> True

txt = " The rain in spain"
x = "ain" not in txt
print(x)

# output --> False

# String Concatenation : we can use the = operator

a = "Hello"
b = "world"
x = a + b
print(x)

# for space

a = "Hello"
b = "world"
c = a + " " + b
print(c)

# String Format --> we can not combine string and number like this

# age = 36
# txt = "My name is Niranjan , I am " + age
# print(txt)  # --> TypeError: can only concatenate str (not "int") to str

# we can combine string and numbers by using the format() method

age = 45
txt = "My name is Niranjan , and I am {}"
print(txt.format(age))

# --> My name is Niranjan , and I am 45

age = 45
txt = "My name is Niranjan , and I am  "
print(txt.format(age))

# --> output- My name is Niranjan , and I am

# Unlimited number of arguments we will pass

quantity = 3
itemno = 122
price = 50.12
myorder = "I want {} piece of item {} for {} dollars ."
print(myorder.format(quantity, itemno, price))

# Output --> I want 3 piece of item 122 for 50.12 dollars .

quantity = 3
itemno = 122
price = 50.12
myorder = "I want to pay {} dollar for {} piece of items {} "
print(myorder.format(quantity, itemno, price))

# Output --> I want to pay 3 dollar for 122 piece of items 50.12

quantity = 3
itemno = 122
price = 50.12
myorder = "I want to pay {1} dollar for {2} piece of items {0} "
print(myorder.format(quantity, itemno, price))

# --> output--  I want to pay 122 dollar for 50.12 piece of items 3

# Escape Character -- backslash \
# Ex - We will get an error if you use double quotes inside a string that is surrounded by double quotes .

# txt = "I am Niranjan from "Bihar buxar" name"
# output - SyntaxError: invalid syntax

txt = "I am Niranjan from \"Bihar buxar\" name."
print(txt)

# Output --> I am Niranjan from "Bihar buxar" name.

# other escape character
# \' --> Single quotes

txt = 'It\'s alright.'
print(txt)

# output --> It's alright.

# \n --> new line
txt = "Hello\nworld"
print(txt)

# output -->
# Hello
# world

# \t --> Tab
txt = "Hello \t world"
print(txt)

# output --> Hello 	 world

# \b --> backslash

txt = "Hello \bworld"
print(txt)

# Output --> Helloworld


name = 'kamal'
age = 34
sal = 1000.00

sentence = 'my name is {0}. i am {1}. i have {2}'
print(sentence.format(name, age, sal))
# output - my name is kamal. i am 34. i have 1000.0
print(sentence.format("Naren", 39, 2000.00))
#                      0     1     2
# output - my name is Naren. i am 39. i have 2000.0

sentence = 'my name is {name}. i am {age}. i have {sal}'
print(sentence.format(name="Kamal", age=35, sal=1000.0))

# output - my name is Kamal. i am 35. i have 1000.0

print(sentence.format(name="raj", age=25, sal=7000.0))

# output - my name is raj. i am 25. i have 7000.0

