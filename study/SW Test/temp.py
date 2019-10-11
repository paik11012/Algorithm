from pprint import pprint
box = []
for j in range(8):
    box.append([i for i in range(8)])
pprint(box)
city = 8
if city % 2 == 0:
    c = (city-1) // 2
else: c = city // 2
for ii in range(1, city // 2):
    odds = ii * 2 + 1  # 3 5 7
    print(c)
    mid = odds // 2 + 1
    print(mid)
    # for x in range(odds):  # 가로 행 3
    #     for y in range()
    #     print(x)


# print(box[2][2])
