import ast,sys
input_str = sys.stdin.read()
sides = ast.literal_eval(input_str)#list of side lengths
n = len(sides) 

my_stack = []
i = 0

print("sides:", sides)
while(i < n):
    print("i:", i, "n:", n, "sides[i]:", sides[i],"sides[n-1]:", sides[n-1])
    if sides[i] >= sides[n-1]:
        my_stack.append(sides[i])
        i = i+1
    else:
        my_stack.append(sides[n-1])
        n = n - 1
    
    print("my_stack:", my_stack)

flag = 0
i = 1
while i < len(my_stack): 
    print("i:", i, "my_stack[i]:", my_stack[i],"my_stack[i-1]:", my_stack[i-1], "(my_stack[i] > my_stack[i - 1]):",(my_stack[i] > my_stack[i - 1]))
    if(my_stack[i] > my_stack[i - 1]): 
        flag = 1
    print(flag)
    i += 1
    

if (not flag) : 
    print ("Possible") 
else : 
    print ("Impossible") 
