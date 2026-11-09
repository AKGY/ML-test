#CSV : Comma-Separated Value

#CSV "1000","비누","300"
#SSV Speace-Separated Value : "1001" "장갑" "150"
#TSV Tab-Separated Value : "1002"  "마스크"    "230"

#CSV > SSV,TSV
#한줄에 데이터 하나
csv_str = '''
ID, 품명, 가격
"1000","비누","300" #1번 데이터
"1001","장갑","150" #2번 데이터
"1002","마스크","230" #3번 데이터
'''
#CSV는 선형적이라 표현력이 많이 제약됨

xml_str = '''
<product>
    <product ID = "1000">
        <name>비누</name>
        <price>300</price>
    <product ID = "1001">
        <name>장갑</name>
        <price>150</price>
    <product ID = "1002">
        <name>마스크</name>
        <price>230</price>
</product>
'''
#xml은 사람마다 형식이 다를수있다 = 표현력이 매우 다양하다

json_str = '''
[
    ID : 1000,
    품명 : "비누"
    가격 : 300
]
[
    ID : 1001,
    품명 : "장갑"
    가격 : 150
]
[
    ID : 1002,
    품명 : "마스크"
    가격 : 230
]

'''
#json은 표현이 규격화되어있다

#CSV>JSON>XML 용량
#XML>JSON>CSV 표현력
csv.split(sep=",")


splitted = csv.split("\n")
