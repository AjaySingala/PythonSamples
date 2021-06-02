# eng2gr = dict()
# print(eng2gr)
# eng2gr['one'] = 'eins'
# print(eng2gr)

# eng2gr = {'one': 'eins', 'two': 'zwei', 'three': 'drei'}
# print(eng2gr)

# # Access dictionary elements.
# eng2gr = {'one': 'eins', 'two': 'zwei', 'three': 'drei'}
# print(eng2gr['two'])
# # print(eng2gr['four']) // Error.

# # Using the get() method.
# print(eng2gr.get('two'))
# print(eng2gr.get('three'))

# print(len(eng2gr))

# # Change or add elements in a dictionary.
# eng2gr = {'one': 'eins', 'two': 'zwei', 'three': 'drei'}
# eng2gr['four'] = 'four' #Add Element
# print(eng2gr)
# eng2gr['four'] = 'vier'  #Update Element
# print(eng2gr)

# # Dictionary Membership Test.
# print('one' in eng2gr)
# print('eins' in eng2gr)

# # See whether something appears as a value in a dictionary, you can use the method values.
# vals = list(eng2gr.values())
# print(vals)
# print('eins' in vals)

# # Delete or remove elements from a dictionary.
# eng2gr = {'one': 'eins', 'two': 'zwei', 'three': 'drei', 'four':'vier'}
# # remove a particular item
# print(eng2gr.pop('four'))
# print(eng2gr)

# # remove an arbitrary item
# print(eng2gr.popitem())
# print(eng2gr)

# # delete a particular item
# del eng2gr['one']
# print(eng2gr)

# # remove all items
# eng2gr.clear()
# print(eng2gr)

# Some other methods for dictionaries.
fruits = {}.fromkeys(['Orange','Apple','Banana'], 0)
print(fruits)

for item in fruits.items():
    print(item)

print(list(sorted(fruits.keys())))

