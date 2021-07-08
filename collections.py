from collections import Counter

# Counter
sandwich_sales = ["veg", "grill", "egg", "veg", "veg", "chicken", "cheese"]
mycounter = Counter(sandwich_sales)
print(mycounter)
print(mycounter["veg"])

print(Counter(["B","A","A","B","C","X","Y","A"]))

print(Counter({"A": 3, "B":5, "C":8}))

print(Counter(A=3, B=4, C=10))

# namedtuple.
from collections import namedtuple

Sandwich = namedtuple("SandwichItems", "name, price")
first_sandwich = Sandwich("Veg Sandwich", "$3.00")
print(first_sandwich)
print(first_sandwich.name)
print(first_sandwich.price)

second_sandwich = Sandwich._make(["Cheese", "$2.50"])
print(second_sandwich)
print(second_sandwich.name)
print(second_sandwich.price)

# defaultdict
from collections import defaultdict

sandwiches = defaultdict(str)
sandwiches[0] = "Veg"
sandwiches[1] = "Cheese"
sandwiches[2] = "Mayo"
print(sandwiches[0])
print(sandwiches[1])
print(sandwiches[2])
print(sandwiches[3])

# ChainMap
from collections import ChainMap
standard_menu = {"Veg": "$3.00", "Cheese": "$2.75", "Mayo": "$2.60"}
secret_menu = {"pizza": "$6.00", "Burger": "$5.50", "Pasta": "$7.00", "Veg": "$2.00"}

menu = ChainMap(standard_menu, secret_menu)
print(menu)
print(menu["Veg"])
print(menu["pizza"])
print(list(menu.keys()))
print(list(menu.values()))
