from pprint import pprint

snail = [[0] * 5 for _ in range(5)]  # 숫자를 넣으려고 하는 리스트
# 배열이 뭐냐? 변수 여러개
# 4/ 4 4 3 3 2 2 1 1
X = 0  # 내가 숫자를 넣으려고 하는 좌표(인덱스) => 행
Y = 0  # 열
# snail[X][Y] = num  # Y += 1 4 번, num+=1 반복
num = 2  # num: 내가 넣을 숫자 변수
m_size = 5
snail[0][0] = 1
for i in range(4):  # 0 1 2 3
    snail[X][Y + 1] = num
    Y += 1
    num += 1
for j in range(0, 2):  # 0 1
    for i in range(4 - 2 * j):
        snail[X + 1][Y] = num
        X += 1
        num += 1
    for i in range(4 - 2 * j):  # 4 2
        snail[X][Y - 1] = num
        Y -= 1
        num += 1
    for i in range(3 - 2 * j):  # 3 1
        snail[X - 1][Y] = num
        X -= 1
        num += 1
    for i in range(3 - 2 * j):  # 3 1
        snail[X][Y + 1] = num
        Y += 1
        num += 1

pprint(snail)