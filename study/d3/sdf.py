import sys
from pprint import pprint
sys.stdin = open('2667.txt','r')


def out_idx(y, x):
    if x < 0 or x > n-1: return True
    elif y < 0 or y > n-1: return True
    return False

n = int(input())

visited = [[0] * n for _ in range(n)]
dx = [1, 0, -1, 0]  # 우 하 상 좌
dy = [0, 1, 0, -1]
q = []
box = []
for _ in range(n):
    kk = list(map(int, input()))
    box.append(kk)

total = []

for y in range(n):
    for x in range(n):
        q.append((y, x))
        visited[y][x] = 1
        cnt = 1
        while q:  # 큐가 차있는 동안
            y, x = q.pop()
            # print(q)
            for dir in range(4):
                Y = y + dy[dir]
                X = x + dx[dir]
                if not out_idx(Y, X) and box[Y][X] == 1 and visited[Y][X] == 0:  # 범위 밖이 아니고 단지이고 방문하지 않았으면
                    q.append((Y, X))
                    # print(Y, X)
                    visited[Y][X] = 1  # 방문 했다고 처리
                    cnt += 1
        total.append(cnt)
print(total)
