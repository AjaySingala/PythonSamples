# ListComprehension.py

# Legacy code.
from matplotlib.pyplot import new_figure_manager


names = ["ajay", "Batman", "Neo"]
new_names = []

for n in names:
    if n.islower():
        n = n.capitalize()
    else:
        n = "Relax " + n.capitalize()
    
    new_names.append(n)

names = new_names
print(names)

# Using List Comprehension.
names = ["ajay", "Batman", "Neo"]
[n.capitalize() if n.islower() else "Relax " + n.capitalize() for n in names]

# Hidden Message.
my_string = "hi442nm233ag2"

new_string = "".join(
    ["d" if i == "4"
        else "e" if i == "2"
        else "s" if i == "3"
        else i
        for i in my_string]
)

print(new_string)

# Convert a for loop into list comprehension.
# Regular for loop:
fruits = ["apples", "bananas", "straberries"]
for fruit in fruits:
    print(fruit)

# With list comprehension.
[print(fruit) for fruit in fruits]

# Convert strings into uppercase.
# Using for loop.
fruits = ["apples", "bananas", "straberries"]
new_fruits = []

for fruit in fruits:
    # Won't work.
    fruit = fruit.upper()
    new_fruits.append(fruit)

fruits = new_fruits
print(fruits)

# Using list comprehension.
fruits = ["apples", "bananas", "straberries"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# List comprehension conversion with booleans.
# Old way:
bits = [False, True, False, False, True, False, False, True]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

print(bits)
print(new_bits)

# Using list comprehension.
bits = [False, True, False, False, True, False, False, True]
super_bits = [1 if b == True else 0 for b in bits]
print(bits)
print(super_bits)

# String manipluation.
my_string = "HelloMyNameIsAjay"
my_string = [i for i in my_string]
print(my_string)

# apply join().
my_string = "HelloMyNameIsAjay"
my_string = "".join([i for i in my_string])
print(my_string)

# Modify the string using list comprehension.
my_string = "HelloMyNameIsAjay"
# If the char is lowercase, we do not touch it. 
# Else, we add a blank space before the character.
my_string = "".join(
    [i if i.islower() else " " + i for i in my_string]
)
print(my_string)

# Get rid of the starting blank space using slicing.
my_string = "HelloMyNameIsAjay"
# If the char is lowercase, we do not touch it. 
# Else, we add a blank space before the character.
my_string = "".join(
    [i if i.islower() else " " + i for i in my_string]
)[1:]
print(my_string)

# Using else-if (else action condition).
my_string = "HelloMyNameIsAjay"
# If the char is lowercase, we do not touch it. 
# Else, we add a blank space before the character.
my_string = "".join(
    [i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in my_string]
)[1:]
print(my_string)
