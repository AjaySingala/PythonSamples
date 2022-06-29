# Method 1:
arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
    if arr[i] < mini:
        mini = arr[i]

    if arr[i] > maxi:
        maxi = arr[i]

print("Array:", arr)
print ("Smallest:", mini)
print ("Largest:", maxi)

# Method 2: Sort the array using inbuilt sort()function
# Minimum element is at index 0 and maximum is at index -1
# So, print(arr[0])
# And, print(arr[-1])
arr = [10, 89, 9, 56, 4, 80, 8]
print("\nBefore:", arr)
arr.sort()

print("After:", arr)
print ("Smallest:", arr[0])
print ("Largest:", arr[-1])

# Method 3 :
# Using inbuilt function min(arr) , it return minimum element of the array.
# Similarly max(arr) return the maximum element of the array.
arr = [10, 89, 9, 56, 4, 80, 8]
print("\n",arr)
print("Smallest:",min(arr))
print("Largest:",max(arr))
