#1 Using slicing.
txt = "Hello World"
print(txt)
txtReverse = txt [::-1]
print(txtReverse)

#2 Create a function.
def my_function(x):
  return x[::-1]

txt = "I wonder how this text looks like backwards"
print(txt)
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
