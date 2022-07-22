def foo(qty, item, price = 1.59):
    ## print("Item: ", item, "Quantity: ", qty, "Price: ", price)
    # Interpolation or formatting.
    print(f"Item: {item}, Quantity: {qty} Price: {price}")

foo(10, "Pencil", 1.99)
foo(20, "Pens", 2.99)

foo("Pens", 10, 2.99)

# named parameters.
foo(qty=15, item="Erasers", price=2.59)
foo(item="Erasers", price=2.59, qty=15)
foo(price=2.59, item="Erasers", qty=15)

foo(25, "sharpeners")
foo(item="sharpeners", qty=25)
# foo(3.99, item="sharpeners", qty=25)  # Gives an error.
foo(item="sharpeners", qty=25, price=3.99)


def foobar(item, price = 1.59, qty = 10):
    print(f"Item: {item}, Quantity: {qty} Price: {price}")

foobar("Markers")
