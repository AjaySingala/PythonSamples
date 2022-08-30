import json

# jsonStr = '[{"a":1, "b":2}, {"c":3, "d":4}]'
# aList = json.loads(jsonStr)
# print(aList[0]['b'])

# jsonStr = '[[{"a":1, "b":2}], [{"c":3, "d":4}]]'
# aList = json.loads(jsonStr)
# print(aList[0][0])
# print(aList[0][0]["b"])

# print("Read JOSN from file...")
# with open('read_json.json') as f_in:
#     data = json.load(f_in)
#     print(data)
#     print("Print just the 'ask'...")
#     print("Ask:", data['Ask'])

# 
person = {
    "firstname": "John",
    "lastname": "Smith",
    "age": 28,
    "city": "Dallas",
    "phone": [ {"home": "555-9987", "work": "555-0941"}]
}
print(person)

#jsonPerson = json.dumps(person)
jsonPerson = json.dumps(person, indent=3)
print(jsonPerson)
print(type(jsonPerson))

sortedPerson = json.dumps(person, sort_keys=True)
print(sortedPerson)
print(type(sortedPerson))

sortedIndentedPerson = json.dumps(person, sort_keys=True, indent=4)
print(sortedIndentedPerson)
print(type(sortedIndentedPerson))
