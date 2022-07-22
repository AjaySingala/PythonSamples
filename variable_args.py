## non-kewyword arguments.
# def foo(*args):
#     print(args)
#     for arg in args:
#         print(arg)

# foo("John")
# foo("John", "Mary")
# foo("John", "Mary", "Joe")
# foo("John", "Mary", 200)


# def foobar(arg1, *args):
#     print(arg1)
#     for arg in args:
#         print(arg)

# foobar("This is a test", "John", "Mary")

# kewyword arguments.
def new_foo(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"Key: {k}. Value: {v}")
        print("The key %s has the value %s" % (k,v))

new_foo(first="John", last="Smith")
new_foo(first="John", last="Smith", age=25)
