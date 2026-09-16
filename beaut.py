from bs4 import BeautifulSoup

html = """
<html><body>
        <div id="meigen">
        <h1>위키북스 도서</h1>
        <ul class="items">
            <li>유니티 게임 이펙트 입문</li>
            <li>스위프트로 시작하는 아이폰 앱 개발서</li>
            <li>모던 웹사이트 디자인의 정석</li>
        </ul>
        <ul class="items items2">
                    <li>메트로 2033</li>
                    <li>디지털 포트리스</li>
                    <li>총 균 쇠</li>
                    <li id=death>죽음의 수용소에서</li>
                </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

#태그 선택자 "h1" "html"
#id선택자 "#<id이름>"
#클래스 선택자 "<클래스 이름><클래스 이름><클래스 이름>"
#후손 선택자 "#meigen li"
#자식 선택자 "ul.items > li"

##########
header = soup.select_one("h1") #요소  #태그 선택자
id_item = soup.select_one("#death") #id선택자
class_items = soup.select(".items.items2 > li") #클래스 선택자
D_item = soup.select_one("#meigen h1") #후손 선택자
lst_items = soup.select("ul.items > li") #요소의 배열  #자식 선택자
##########

#요소 : select_one()을 이용하여 추출한 배열
#.string<<문자열 .attrs<<<속성(글 색깔 등)

print("header = ", header.string)
print("id_item = ", id_item.string)
print("Di = ", D_item.string)



for lst in lst_items :
    print("lst = ", lst.string)

for cl in class_items :
    print("cl = ", cl.string)

