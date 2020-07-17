'''
Class is the template
object is the instance created from the template
Class : Attributes and behaviours
----Attributes/fields/data/properties
----Behaviours/methods

string : 'hello'  #--> hello is the attribute
string : 'hello'.upper()  # upper is the behaviour

Custom class : Person - name , gender , id , height , weight , age ,  species = 'homosapiens'
              behavious - speak dance , eat , sleep , grow

object or instance :
p1 = person()
p1.name = 'niranjan'
p1.gender = 'm'
p1.id = 22222221

p2 = person()
p2.name = 'arjun'

parent class called object

'''


# How to create a syntax

class Snake:
    pass


python = Snake()  # Snake() object is created and assigning the variable python . we always create a object by calling a constructor
print(python)


class Snake:
    # class properties
    name = 'Python'  # Class attributes


print('class attribute - ', Snake.name)  # -->  without creating a object for this , we r calling class name directly
python1 = Snake()  # python 1 is object
python2 = Snake()

python1.name = "py"
print(python1.name)  #
print(python2.name)

# object = class(specified attributes and behaviours)
# object = class(attributes)

# constructor  = a constructor is used to create an object from the class

'''
self - Self is nothing but whatever object u r creating that should  access  all the attributes and method of the particlular class
Snake so when i called self , self is nothing object itself so the objects will have access to all the attributes and method of the class
snake thats y we always first first argument is self. 
Self is belong to an object

init function - init is a special function it is also called constructor

'''


class Snake:
    # instance properties -->
    def __init__(self, name):  # we defining the constructor from init function
        self.name = name


python = Snake('Python')  # python is just variable
print(python.name)
cobra = Snake('Cobra')  # cobra is just variable
print(cobra.name)


class Snake:
    def __init__(self, name):
        self.name = name

    def bite(self):
        print(self.name, 'bite is poisionous')


python = Snake('Python')
print(python.name)
python.bite()
cobra = Snake('Cobra')
print(cobra.name)
cobra.bite()


class Snake:
    # class attributes /property
    species = "reptiles"  # Class Attribute

    def __init__(self, name):  # instance attribute  92 and 93 line
        self.name = name

    def bite(self, isPoisonous):  # instance method line number 95 to 99
        if isPoisonous:
            print(self.name, 'bite is poisionous')
        else:
            print(self.name, 'bite is not poisionous')


# instance/object properties (name) does not require an object/instance to be created
# by calling the constructor and passing the arguments  , it can be directly called using objectName(python)

python = Snake('Python')  # name Python giving attribute
print(python.name)
python.bite(False)
cobra = Snake('Cobra')
print(cobra.name)
cobra.bite(True)

print(cobra.species)  # A class attribute

# for class attribute need not create a object we can call directly by class name
# class attribute species does not require an object/instance to be created , it can be directly called using class name (Snake)

print(Snake.species)

list_1 = list("python")
print(list_1)
list_1.reverse()
print(list_1)
list_1.remove("o")
print(list_1)


#  modify a object ----->

class Snake:
    # class attributes /property
    species = "reptiles"  # Class Attribute

    def __init__(self, name, len):  # instance attribute  140 tp 143 line
        self.name = name
        self.length = len

    def bite(self, isPoisonous):  # instance method line number 95 to 99
        if isPoisonous:
            print(self.name, 'bite is poisionous')
        else:
            print(self.name, 'bite is not poisionous')


python = Snake('Python', 2.5)  # name Python giving attribute
print(python.name)
python.bite(False)
cobra = Snake('Cobra', 1)
print(cobra.name)
cobra.bite(True)
print(cobra.length)
cobra.length = 2  # modify a object properties
print(cobra.length)
print(cobra.length)

print(0.1 + 0.2 - 0.3)


#class method


class Snake:
    # class attributes /property
    species = "reptiles"  # Class Attribute

    def __init__(self, name, isPoisonous):
        # instance attributes/properties
        self.name = name
        self.isPoisonous = isPoisonous

    def bite(self):  # instance method
        if self.isPoisonous :
            print(self.name, 'bite is poisionous')
        else:
            print(self.name, 'bite is not poisionous')

    @classmethod
    def layEggs (cls):
            print(cls.species, "can layEggs")


#Instance/object properties(name) require an object/instance to be created.
#by calling the constructor and passing arguments , it can be directly called using objectName(python)


python = Snake('Python', 2.5)  # name Python giving attribute
print(python.name)
python.bite()
cobra = Snake('Cobra', True)
print(cobra.name)
cobra.bite()
print(Snake.species)
print('class call-' , Snake.species)
Snake.layEggs()

print('niranjan'.upper())
print('niranjan'.replace('r' , 'a'))
print('niranjan'.count() )

