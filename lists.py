# numbers = [10, 20, 30, 40, 50]
# print(numbers)

# empty = []
# print(empty)

# food = ['Hot dog','Sandwich', 'Hamburger']
# print(food)

# # list with mixed datatypes.
# mixed_list = [1, "Python", 1.5]
# print(mixed_list)

# # The following list contains a string, a float, an integer, and another list:
# nested_list = ['Python', 2.0, 5, [10, 20]]
# print(nested_list)

# # Lists are mutable.
# food = ['Hot dog','Grill Sandwich', 'Cheese burger']
# print(food[0])
# print(food[1])

# numbers = [10, 20]
# numbers[0] = 100
# numbers[1] = 200
# print(numbers)

# # The in operator.
# food = ['Hot dog','Sandwich', 'Hamburger']
# print('Hot dog' in food)
# print('French fries' in food)

# # Access elements from a list.
# food=['Hot dog','Sandwich', 'Hamburger']
# print(food[0])
# print(food[1])
# # print(food[3])  # Error.

# # Negative indexing.
# food=['Hot dog','Sandwich', 'Hamburger']
# print(food[-1])
# print(food[-2])
# print(food[-3])

# # Traversing a list.
# food=['Hot dog','Sandwich', 'Hamburger']
# for i in food:
#     print(i)
# # Traverse using range and len.
# for i in range(len(food)):
#     print(food[i])

# # + operator concatenates lists.
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# # The * operator repeats a list a given number of times.
# a=[0]*4
# print(a)
# b=[1,2,3]*3
# print(b)

# # slice lists.
# #l = ['make','me', 'analyst']
# l = ['this', 'is', 'a', 'sample', 'list', 'of', 'many' 'words']
# # get elements 2nd to 3rd. Starts with 0. 1:3 means upto 3rd, but not including 3rd.
# print(l[1:3])
# # get elements beginning to 2nd
# print(l[:-1])
# # get elements 2nd to end
# print(l[1:])
# # elements beginning to end
# print(l[:])

# # A slice operator on the left side of an assignment can update multiple elements.
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# # replace b,c with x,y.
# t[1:3] = ['x', 'y']
# print(t)
# # replace x,y with m,n,o.
# t[1:3] = ["m", "n", "o"]
# print(t)

# # List methods.
# # append.
# x = ['a', 'b', 'c']
# x.append('d')
# print(x)

# # extend.
# x1 = ['a', 'b', 'c']
# x2 = ['d', 'e']
# x1.extend(x2)
# print(x1)

# # sort.
# t = ['d', 'c', 'e', 'b', 'a']
# print(t)
# t.sort()
# print(t)

# # Delete or remove elements from a list.
# # pop operator.
# t = ['a', 'b', 'c']
# print(t)
# x = t.pop(1)
# print(t)
# print(x)
# print(type(x))

# t = ['a', 'b', 'c', 'd', 'e']
# print(t)
# print(t.pop())
# print(t)

# # del operator.
# t = ['a', 'b', 'c']
# print(t)
# del t[1]
# print(t)

# # remove() function.
# t = ['a', 'b', 'c']
# print(t)
# t.remove('b')
# print(t)

# # del with slice index to remove more than 1 element.
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t)
# del t[1:5]
# print(t)

# # Lists and functions.
# nums = [3, 4, 5, 6, 7, 8]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# # Calculate total and average.
# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Total:', total)
# print('Average:', average)

# # Calculate total and average using built-in functions.
# numlist = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Total:', total)
# print('Average:', average)

# # Lists and strings.
# # Convert from a string to a list of characters.
# l="Make Me Aanlyst"
# t = list(l)
# print(t)

# # Break a string into words.
# s = 'Make Me Aanlyst'
# t = s.split()
# print(t)

# s = 'make-me-analyst'
# delimiter = '-'
# t= s.split(delimiter)
# print(t)

# # join is the inverse of split. It takes a list of strings and concatenates the elements.
# t = ['Make', 'Me', 'Analyst']
# delimiter = ' '
# j = delimiter.join(t)
# print(j)

# # List arguments.
# def delete_head(t):
#     del t[0]

# letters = ['a', 'b', 'c']
# delete_head(letters)
# print(letters)

# # The append method modifies a list, but the + operator creates a new list.
# t1 = [1, 2]
# t2 = t1.append(3)
# print(t1)
# print(t2)
# t3 = t1 + [3]
# print(t1)
# print(t2)
# print(t3)
# print(t2 is t3)

