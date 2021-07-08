import json

jsonStr = '[{"a":1, "b":2}, {"c":3, "d":4}]'
aList = json.loads(jsonStr)
print(aList[0]['b'])

jsonStr = '[[{"a":1, "b":2}], [{"c":3, "d":4}]]'
aList = json.loads(jsonStr)
print(aList[0][0])

with open('read_json.json') as f_in:
    data = json.load(f_in)
    print(data)
    print("Ask:", data['Ask'])