import sys
from pprint import pprint
sys.stdin = open('2667.txt','r')


def out_idx(y, x):
    if x < 0 or x > n-1: return True
    if y < 0 or y > n-1: return True
    return False


def bfs(y, x):
    global cnt
    if box[i][j] == 1:
        q.append((i, j))
        box[i][j] = 2
        cnt = 1
        while q:  # 큐가 차있는 동안
            y, x = q.pop()
            # print(q)
            for dir in range(4):
                Y = y + dy[dir]
                X = x + dx[dir]
                if not out_idx(Y, X) and box[Y][X] == 1:  # 범위 밖이 아니고 단지이고 방문하지 않았으면
                    q.append((Y, X))
                    # print(Y, X)
                    box[Y][X] = 2  # 방문 했다고 처리
                    cnt += 1
    return cnt

n = int(input())
dx = [1, 0, -1, 0]  # 우 하 상 좌
dy = [0, 1, 0, -1]
q = []
box = []
total = []
for _ in range(n):
    kk = list(map(int, input()))
    box.append(kk)
for i in range(n):
    for j in range(n):
        cnt = 0
        if box[i][j] == 1:
            cnt += bfs(i, j)
            total.append(cnt)
total.sort()
print(len(total))
for jj in range(len(total)):
    print(total[jj])