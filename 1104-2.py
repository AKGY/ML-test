#JSON(JavaScrpt Object Notaion)
#6가지 자료형
#숫자 : 10, 20, 30 ...
#문자열 : "따옴표로 감싼다" "1848"
#부울 : True, False <<<JS에선 소문자임 true, false
#NULL : null
#배열 : [10, 20, 30, "안녕하세요", true] 자료형 섞기가능
#객체 : 파이썬 dictionary, {} curly bracket 사용
#JSON : [{"키A":"값"} {"키A":1234,  "키B":  "값",    "키C":true,    "키D":[12,57],   "키E": ["name",52] }]
#json으로 처리하면 import.json json으로 빼려면export ex) import json json_str = [{},{},{},{}]
#JSON 문자열 -> 파이썬 자료형 // json.load, json.loads 메소드
import json

json_str = '''
[
    {"name": "사과", "price": "2000"},
    {"name": "바나나", "price": "5000"},
    {"name": "귤", "price": "12000"},
    {"name": "감", "price": "6000"},
    {"name": "배", "price": "8000"}
]
'''

output = json.loads(json_str)
print(output)


