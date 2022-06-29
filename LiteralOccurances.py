# Method 1:
# Python3 implementation to print the characters and frequencies in order of its occurrence.
def prCharWithFreq(inputStr):
    # Store all characters and their frequencies in dictionary
    d = {}
    for i in inputStr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
     
    # Print characters and their frequencies in same order of their appearance
    for i in inputStr:
 
        # Print only if this character is not printed before. 
        if d[i] != 0:
            print("{}{}".format(i,d[i]), end =" ")
            d[i] = 0
      
     
# Driver Code
if __name__ == "__main__" :
    inputStr = "It was the best of times. It was the worst of times."
    print("String:", inputStr)
    print("Literal Occurances...")
    prCharWithFreq(inputStr)

# Method 2:
# Using built-in Python function Counter().
from collections import Counter

def prCharWithFreq2(string):
    # Store all characters and their frequencies using Counter function
    d = Counter(string)
    
    # Print characters and their frequencies in same order of their appearance
    for i in d:
        print(i+str(d[i]), end=" ")

string = "It was the best of times. It was the worst of times."
print("\n\nString: ",string, " using Counter()...")
prCharWithFreq2(string)
