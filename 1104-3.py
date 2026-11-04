import json

json_str = '''
[
    {"name": "사과", "price": "100"},
    {"name": "바나나", "price": "200"},
    {"name": "배", "price": "300"},
    {"name": "감", "price": "400"},
    {"name": "자두", "price": "50"}
]
'''

output = json.loads(json_str)
print(output)
print()


#파이썬 자료형 -> JSON 문자열

text = json.dumps(output)

print(text)

print()

print(type(output))