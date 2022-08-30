import re
# txt = "The rain in Spain is not as good as the rain in India"
# x = re.search("^The.*Spain$", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.search("^[A-T][a-h][f-r]*", txt)
# print(x)

# x = re.search("^[a-zA-Z0-9]+$", "abcd7891")
# print(x)
# x = re.search("^[a-zA-Z0-9]+$", "91abcd7891")
# print(x)
# x = re.search("^[a-zA-Z0-9]+$", "abcd 7891")
# print(x)
# x = re.search("^[a-zA-Z0-9]+$", "abcdefgh")
# print(x)

# x = re.search("^[a-zA-Z0-9]*$", "abcdefgh")
# print(x)

# x = re.search("^\w+$", "abcd")
# print(x)

# str = 'ajaysingala125'
# isalnum = str.isalnum()
# print('Is String Alphanumeric :', isalnum)

# txt = "The rain in Spain"
# x = re.split("\s", txt,1)
# print(x)

# x = re.sub("\s", "9", txt)
# print(x)

# x = re.sub("\s", "9", txt, 2)
# print(x)

# def find_capitals(s):
#     result = re.findall('[A-Z]\w+', s)
#     #result = re.findall('[A-Z][A-z]+', s)
#     for i in result:
#         print(i)

# find_capitals("Jacob and Ajay work for Revature W0rd")


# def findallEmail():
#     with open('emails.txt', 'r') as file:
#         readfile = file.read()
#         result = re.findall('[\w.]+@[\w.]+.[\w]+', readfile)
#         # result = re.findall("(\w[.\w]*@[a-zA-Z0-9-.]+\.\w+)",readfile)
#         for i in result:
#             print(i)

# findallEmail()
