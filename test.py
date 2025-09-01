#Print
print("Python Started...")
#----------------
#Data Types

#String 
string_a = "Hello World"

#Int
int_a = 12

#Float
float_a=3.17

#Complex
complex_a=complex(2,3)
complex_b=2+3j

#List
list_a = ["Apple","Orange","Mango"]

#Tuple
tuple_a = ("Python","Html","Css","JS")

#Set
set_a = {"Apple","Lenovo","Samsung","Iqoo"}

#FrozenSet
fset_a = frozenset({"A","I","O","U","E"})

#Dictionary
dict_a = {
    "name":"Python",
    "Version":3.17,
    "Author":"Guido Van Rossum"
}

#Bool
bool_a = True

#--------------------------

#Operators

x,y = 5,10

#Arithmetic Operators

print(x + y)    # Addition
print(x - y)    # Subtraction
print(x * y)    # Multiplication
print(x / y)    # Division
print(x // y)   # Floor Division
print(x % y)    # Modulus
print(x ** y)   # Exponengtial

#Comparison Operators

print(x == y)   # EqualTo
print(x != y)   # NotEqualTo
print(x > y)    # GreaterThan
print(x < y)    # LessThan
print(x >= 5)   # GreaterThan or Equalto
print(y <= 10)  # LessThan or Equalto

#Logical Operator

a, b = True, False

print(a and b)  # And
print(a or b)   # Or
print(not a)    # Not

#Assignment Operators

x += 3   # x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 2   # x = x * 2 → 12
x /= 4   # x = x / 4 → 3.0
x %= 2   # x = x % 2 → 1.0
x **= 3  # x = x ** 3 → 1.0
x //= 2  # x = x // 2 → 0.0

#Bitwise Operators

a, b = 5, 3   # (in binary: 5 → 101, 3 → 011)

print(a & b)   # 1  (AND → 101 & 011 = 001)
print(a | b)   # 7  (OR  → 101 | 011 = 111)
print(a ^ b)   # 6  (XOR → 101 ^ 011 = 110)
print(~a)      # -6 (NOT → invert bits)
print(a << 1)  # 10 (Left shift → 101 → 1010)
print(a >> 1)  # 2  (Right shift → 101 → 10)

#Identity Operators

x = [1, 2]
y = [1, 2]
z = x

print(x is y)      # False (different objects with same values)
print(x is z)      # True  (same object)
print(x is not y)  # True


#Membership Operators

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("mango" not in fruits)  # True


#------------------------

#Conditions

#if
age = 18

if age >= 18:
    print("Eligible to vote")


#if Else

num = 5

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#if Elif Else

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#Nested if
x = 10
y = 20

if x > 5:
    if y > 15:
        print("Both conditions are True")

#ShortHand
a = 10
b = 20

print("a is greater") if a > b else print("b is greater")



#Match Case
key = "James"
match key:
    case "James":
        print("James")
    case "Jhon":
        print("Jhon")
    case _:
        print("Invalid")

#------------------------

#Loops

#For Loop
for i in range(5): 
    print(i)

    
#While Loop
count = 1

while count <= 5:
    print(count)
    count += 1
    
    
#-----------------------------

#LIST
fruits = ["apple", "banana", "cherry"]

#Access List Items
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:])    # ['banana', 'cherry']


#Change List Items
fruits[1] = "orange"
print(fruits)   # ['apple', 'orange', 'cherry']

#Add List Items
fruits.append("mango")              #ADD TO LAST
fruits.insert(1, "grape")           #ADD TO INDEX VALUE
fruits.extend(["kiwi", "melon"])    #COMPINE
print(fruits)

#Remove List Items
fruits.remove("orange") #Item
fruits.pop(2)           #INDEX
del fruits[0]           #INDEX
fruits.clear()          #CLEAR ALL

#Loop List
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)


#List Comprehension
# Basic
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# With condition
even = [x for x in range(10) if x % 2 == 0]
print(even)   # [0, 2, 4, 6, 8]


#Important List Methods
nums = [5, 2, 9, 1]

nums.append(10)       # [5, 2, 9, 1, 10]
nums.extend([3, 7])   # [5, 2, 9, 1, 10, 3, 7]
nums.insert(1, 99)    # [5, 99, 2, 9, 1, 10, 3, 7]
nums.remove(9)        # removes first 9
nums.pop()            # removes last item
nums.sort()           # [1, 2, 3, 5, 7, 10, 99]
nums.reverse()        # reverse order
nums.count(2)         # count occurrences → 1
nums.index(99)        # find index → 6
nums.copy()           # shallow copy
nums.clear()          # empty list


#--------------------------
#TUPLE METHODS
fruits_1 = ("apple", "banana", "cherry")

#Access Tuple Items
print(fruits_1[0])      # apple
print(fruits_1[-1])     # cherry
print(fruits_1[1:])     # ('banana', 'cherry')


#Update Tuples(NOT DIRECTLY)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "orange"
x = tuple(y)
print(x)   # ('apple', 'orange', 'cherry')

#Loop Tuples

for fruit in fruits_1:
    print(fruit)

# With index
for i, fruit in enumerate(fruits_1):
    print(i, fruit)


#TUPLE IMPORTANT
numbers = (1, 2, 3, 2, 4, 2)

print(numbers.count(2))   # 3 → how many times 2 appears
print(numbers.index(3))   # 2 → index of first occurrence of 3


#--------------------------
#SETS

fruits_2 = {"apple", "banana", "cherry"}


#Access Set Items
print("apple" in fruits_2)   # True
print("mango" in fruits_2)   # False

#Add Set Items
fruits_2.add("mango")                 #ADD SIGLE
fruits_2.update(["kiwi", "melon"])    #ADD MULTIPLE
print(fruits_2)

#Remove Set Items
fruits_2.remove("banana")     # error if not present
fruits_2.discard("orange")    # safe remove
fruits_2.pop()                # removes random item
fruits_2.clear()              # empty set
del fruits                  # delete set completely

#Loop Sets
for fruit in fruits_2:
    print(fruit)


#-----------------------------
#DICTIONARY
student = {
    "name": "James",
    "age": 21,
    "course": "Python"
}


#Access Dictionary Items
print(student["name"])     # James
print(student.get("age"))  # 21
print(student.get("marks", "Not Found"))  # Safe access with default

#Change Dictionary Items
student["age"] = 22
student.update({"course": "Data Science"})
print(student)  # {'name': 'Riya', 'age': 22, 'course': 'Data Science'}


#Add Dictionary Items
student["marks"] = 95
student.update({"college": "ABC University"})
print(student)


#Remove Dictionary Items
student.pop("marks")      # remove specific key
student.popitem()         # removes last inserted key–value pair
del student["age"]        # delete by key
student.clear()           # remove all items
del student               # delete dictionary completely

#Loop Through Dictionary
student = {
    "name": "James",
    "age": 21,
    "course": "Python"
}
# Loop keys
for key in student:
    print(key)

# Loop values
for value in student.values():
    print(value)

# Loop key–value pairs
for key, value in student.items():
    print(key, ":", value)
    
#Dictionary Comprehension
# Example 1: square numbers
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example 2: filter even numbers
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#Important Dictionary Methods
print(student.keys())      # dict_keys(['name', 'age', 'course'])
print(student.values())    # dict_values(['James', 21, 'Python'])
print(student.items())     # dict_items([('name', 'James'), ('age', 21), ('course', 'Python')])

# Get value safely
print(student.get("name"))   # James

# Set default if key not exists
student.setdefault("marks", 0)
print(student)   # {'name': 'James', 'age': 21, 'course': 'Python', 'marks': 0}

# Copy dictionary
copy_student = student.copy()
print(copy_student)

# Create dict from keys
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

#---------------------------------

#STRINGS

text = "Python"

#Accessing String

#Indexing
print(text[0])   # P
print(text[-1])  # n

#Slicing
print(text[0:4])    # Pyth
print(text[:4])     # Pyth (from start)
print(text[2:])     # thon (till end)
print(text[::2])    # Pto (every 2nd char)
print(text[::-1])   # nohtyP (reversed)



#Modify String

text = "hello world"
print(text.upper())   # HELLO WORLD
print(text.lower())   # hello world
print(text.title())   # Hello World
print(text.replace("world", "Python"))  # hello Python


#Concatenate Strings

a = "Hello"
b = "Python"
result = a + " " + b
print(result)  # Hello Python

name = "James"
age = 21
print(f"My name is {name}, I am {age} years old.")



#Important String Methods
text = "  Hello, Python World!  "

print(len(text))          # length of string
print(text.strip())       # remove spaces
print(text.lstrip())      # remove left spaces
print(text.rstrip())      # remove right spaces

print(text.upper())       # HELLO, PYTHON WORLD!
print(text.lower())       # hello, python world!
print(text.capitalize())  # Hello, python world!
print(text.title())       # Hello, Python World!
print(text.swapcase())    # hELLO, pYTHON wORLD!

print(text.find("Python"))   # index of "Python" (7)
print(text.count("o"))       # number of 'o'
print(text.startswith("He")) # False (because of spaces)
print(text.strip().startswith("He"))  # True

print(text.endswith("!"))    # False
print(text.replace("Python", "Java"))  # replace substring

# Splitting and joining
words = text.split()   # ['Hello,', 'Python', 'World!']
print(words)
print("-".join(words)) # Hello,-Python-World!

# Checking
print("Python".isalpha())   # True (only letters)
print("123".isdigit())      # True
print("hello123".isalnum()) # True
print("hello".islower())    # True
print("HELLO".isupper())    # True
