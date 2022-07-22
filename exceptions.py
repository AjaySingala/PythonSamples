# def div(x,y):
#     z = 0
#     try:
#         z = x / y
#     except ZeroDivisionError as zde:
#         print("You cannot divided by zero!")
#         print(zde)
#     except:
#         print("Something went wrong!!!")
#     else:
#         print("No exception! YAY!!!")
#         return z
#     finally:
#         print("This will always be called...")

    
# print(div(10,2))
# print(div(10,0))
# print(div(10,"John Smith"))


# File I/O.
def readFile(filename):
    try:
        with open(filename) as f:
            data = f.readlines()
            print(data)

            
    except FileNotFoundError as fnf_err:
        print(f"File {filename} not found. ERROR: {fnf_err}")
    except:
        print(f"Some error occured when trying to read file {filename}")


print("Reading file that exists...")
readFile("test.txt")
print("Reading file that does not exists...")
readFile("invalid_file.txt")
