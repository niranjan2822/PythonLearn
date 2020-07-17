# Python Loops :
# Python has two primitive loop commands :
# 1 . while 2 . for
# 1. while --> with the while loop we can execute a set of statements as long as condition in True

# Ex : print i as long as i is less than 6

i = 1
while i < 6:
    print(i)
    i += 1

# output -
# 1
# 2
# 3
# 4
# 5

# The break statement : with the break statement we can stop the loop even if the while condition is True :
# ex - exit the loop when i is 3 :

i = 1
while i < 6 :
    print(i)
    if i == 3:
        break
    i += 1

# Output -->
# 1
# 2
# 3

# The continue statement : with the continue statement we can stop the current iteration , and continue with the next :
# Ex - continue to the next iteration if i is 3 :

i = 0         # If here i ll give 3 then 4 , 5 , 6 is print
while i < 6:  # if here i ll give 5 then 1 , 2, 4 , 5 print
    i += 1
    if i == 3 :
        continue
    print(i)

# Output -->
# 1
# 2
# 4
# 5
# 6

# The else statement : with the else statement we can run a block of code once when the condition no longer is true :

i = 1
while i < 6:
    print(i)
    i += 1
else :
    print("i is no longer less than 6")

# output :
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6

# Python 'for' loop : a for loop is used for iterating over a sequence (that is either a list , a tuple , a dictionary ,
# a set or a string) with the for loop we can execute a set of statements once for each item is a list , tuple etc .

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

# Output :
# apple
# banana
# cherry

# Ex- loop through the letters in the word "banana"

for x in "banana":
    print(x)

# Output :
# b
# a
# n
# a
# n
# a

# The break statement : with the break statement we can stop the loop before it has looped through all items .
# Ex - exit the loop when x is banana

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# Output :
# apple
# banana

# Ex - exit the loop when x is banana , but this time the break comes before the print .

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
     break
    print(x)

# Output - apple

# The continue statement : with the continue statement we can stop the current iteration of the loop and continue with
# the next
# Ex - do not print banana

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
     continue
    print(x)
# Output -
# apple
# cherry

# The range() function : The range() function returns a sequence of numbers , starting from 0 by default and increment
# by 1 (by default) and ends at a specified number .

# Ex - using the range() function

for x in range(3):
    print(x)
# Output -
# 0
# 1
# 2

# Ex - Using the start parameter :

for x in range(2,6):
    print(x)
# Output -
# 2
# 3
# 4
# 5

# Ex- Increment the sequence with 3 (default is 1)
for x in range(5,20,5):
    print(x)

# (2,10,2) --> 2,4,6,8
# (2,10,3) --> 2,5,8
# (2,20,3) --> 2,5,8,11,14,17
# (2,30,5) --> 2,7,12,17,22,27
# (5,20,5) --> 5,10,15

# else in for loop :
# print all numbers from 0 to 5 and a print a message when the loop has ended .
for x in range(6):
    print(x)
else:
    print("finally finished")
# Output -->
# 0
# 1
# 2
# 3
# 4
# 5
# finally finished

# nested loop :
# print each object for every fruit :
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

# Output :
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry


# The pass statement :

for x in [0,1,2]:
    pass












