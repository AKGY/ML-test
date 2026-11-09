with open("agaricus-lepiota.data", "r") as f:
    csv = f.read()

splitted = csv.split("\n")
'''
for item in splitted:
    list_mushroom = item.split(",")
    print(list_mushroom)
'''
for item in splitted:
    if not item.strip():
        continue
    list_mushroom = item.split(",")

    print("\n요소를 선택하는 경우")
    print(list_mushroom[0])
    print(list_mushroom[1])
    print(list_mushroom[2])
    print(list_mushroom[3])

    print("\n요소의 범위를 선택하는 경우")
    print(list_mushroom[1:4])
    print(list_mushroom[5:10])
    print(list_mushroom[:10])
    print(list_mushroom[5:])



