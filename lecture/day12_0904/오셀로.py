import sys
from pprint import pprint
sys.stdin = open('오셀로.txt', 'r')

def out_idx(i,j):
    if i < 0 or i >= n: return True
    if j < 0 or j >= n: return True
    return False
# dx = [0,1,1, 1, 0,-1,-1,-1]  # 8 방향 탐색 잡기, 시작은 오른쪽부터 시계방향으로 돌아가면서
# dy = [1,1,0,-1, -1,-1, 0, 1]

tc = int(input())  # 6 4 5 6 6
for tcc in range(1, tc + 1):
    n, m = map(int,input().split())  # 판 사이즈, 데이터 갯수
    h = int(n/2)
    box = [[0] * n for _ in range(n)]  # 흑1 백2
    box[h-1][h-1], box[h][h] = 2, 2  # 처음 네개 채우기
    box[h][h-1], box[h-1][h] = 1, 1

    for i in range(m):  # 데이터 하나씩 넣기
        oy, ox, color = map(int,input().split())  #origin x,y
        x = ox-1  # 인덱스 맞추어주기
        y = oy-1
        box[x][y] = color  # 선택한 것 바꿔주기

        for j in range(y, n-1):  # 오른쪽으로 최대 세 번 이동
            dx, dy = 1, 0
            x = x + dx  # 다음 것으로 이동
            y = y + dy
            if out_idx(x, y) == True: break
            elif box[x][y] == color: # 색이 같으면 그 안에 다른 색 바꾸기
                for k in range(oy, y):
                    if box[x][k] != color: box[x][k] = color
            elif box[x][y] == 2: pass # 색이 다르면 같은 것 만날때까지 이동
            elif box[x][y] == 0: break  # 0 만나면 반복 그만하기

    pprint(box)



    # pprint(box)
# 1 1 2
# 4 3 1
# 4 4 2
# 2 1 1
# 4 2 2
# 3 4 1
# 1 3 2
# 2 4 1
# 1 4 2
# 4 1 2
# 3 1 2