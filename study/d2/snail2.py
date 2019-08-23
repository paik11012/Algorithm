from pprint import pprint

snail = [[0] * 5 for _ in range(5)]  # 숫자를 넣으려고 하는 리스트
# 배열이 뭐냐? 변수 여러개
X = 0  # 내가 숫자를 넣으려고 하는 좌표(인덱스) => 행
Y = 0  # 열
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    if snail[x][y] != 0: return True
    return False

num = 1
for i in range(1,6):  # 10
    if not iswall(X+dx[d], Y+dy[d]):
        snail[X][Y] = num
        X += dx[d]
        Y += dy[d]  # 여기를 0을 변수로 써야 함
        num += 1
        print(X, Y)
    else: #wall이 있으면 꺾어라
        d = i % 4
        snail[X][Y] = num

pprint(snail)

# num = 1
# for i in range(1,10):  # 10
#     snail[X][Y] = num
#     X += dx[d]
#     Y += dy[d]  # 여기를 0을 변수로 써야 함
#     num += 1
#     print(X, Y)
#     if iswall(X+dx[d], Y+dy[d]):  # wall이 있으면 꺾어라
#         d = i % 4
# pprint(snail)

