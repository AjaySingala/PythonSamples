# To take input from the user.

# n = int(input("Enter n: "))
n = 10
while n <15 :
    print(n)
    n = n + 1
print('STOP!!!')

# # An infinite loop.
# n = 10
# while True :
#     print(n)
#     n = n + 1
# print('STOP!!!')

# # break.
# while True:
#     line = input('Enter "STOP" to stop the loop\n')
#     if line == 'STOP':
#         break
#     print(line)
# print('STOP!')

# # continue #1.
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# # Continue #2
# for i in "Make Me Analyst":
#     if i == "M":
#         continue
#     print(i)
# print("STOP")

# # for loop.
# emp = ['Seba', 'Kattula', 'Mohan']
# for e in emp:
#     print('Hello:', e)
# print('Done!')

# arr=[1,2,3,4,5]
# for i in arr:
#     print(i)

# # range().
# # Program to iterate through a list using indexing
# arr = [11,12,13,14,15]
# # iterate over the list using index
# for i in range(len(arr)):
#     print(arr[i])

# # Program to iterate through a list using indexing
# arr = ["A","B","C","D"]
# # iterate over the list using index
# for i in range(len(arr)):
#     print(arr[i])

# count = 0
# for i in [1,2,3,4,5]: 
#     count = count + 1
# print('Count: ', count)

# # Maximum and minimum loops
# largest = None
# print('Before 1:', largest)
# for i in [3, 4, 12, 90, 44, 150]: 
#     if largest is None or i > largest :
#         largest = i 
#     print('Loop 1:', i, largest)
# print('Largest 1:', largest)
# smallest = None
# print('Before 2:', smallest)
# for i in [3, 4, 12, 90, 44, 150]: 
#     if smallest is None or i < smallest :
#         smallest = i 
#     print('Loop 2:', i, smallest)
# print('Smallest 2:', smallest)
