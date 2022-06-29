# Method 0: Using a class.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = 1
        previous = nums[0]
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != previous:
                length += 1
                previous = nums[i]
                nums[index] = nums[i]
                index += 1
        return length


input_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]

# printing the list using * operator separated by space
print(*input_list)

# # printing the list using * and sep operator
# print("printing lists separated by commas")

# print(*input_list, sep = ", ")

# # print in new line
# print("printing lists in new line")

# print(*input_list, sep = "\n")

print("Current items in the list: ", len(input_list))
ob1 = Solution()
print("No. of items in list after removing duplicates: ", ob1.removeDuplicates(input_list))
print(*input_list)

# Method 1: removing duplicated from the list using naive methods.
# Another way of removing duplicates from a list:
print("\nAnother way of removing duplicates from an unsorted list...")
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print("Before:", t)

s = []
for i in t:
    if i not in s:
        s.append(i)
print("After:", s)

print("\nRemoving duplicates from an sorted list...")
t = [1, 1, 2, 2, 3, 5, 5, 6, 6, 6, 7, 8, 8, 8]
print("Before:", t)

s = []
for i in t:
    if i not in s:
        s.append(i)
print("After:", s)

# Method 2: removing duplicates from the list using list comprehension.
print("\nremoving duplicates from the list using list comprehension ...")
# initializing list
sam_list = [11, 13, 15, 16, 13, 15, 16, 11]
print ("The list is: " + str(sam_list))

# to remove duplicated from list
result = []
[result.append(x) for x in sam_list if x not in result]

# printing list after removal
print("The list after removing duplicates: " + str(result))

# Method 3: removing duplicated from the list using set()
print("\nremoving duplicated from the list using set() ...")
# initializing list
sam_list = [11, 15, 13, 16, 13, 15, 16, 11]
print ("The list is: " + str(sam_list))

# to remove duplicated from list
sam_list = list(set(sam_list))

# printing list after removal ordering distorted
print("The list after removing duplicates: " + str(sam_list))
