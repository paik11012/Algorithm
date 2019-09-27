import collections
import sys
from pprint import pprint
sys.stdin = open('2667.txt','r')


def out_idx(y, x):
    if x < 0 or x > n-1: return True
    if y < 0 or y > n-1: return True
    return False


def bfs(x, y):
    global cnt
    box[x][y] = 2  # 방문처리
    cnt = 1
    q.append((x, y))
    while q:
        xi, yi = q.popleft()
        for i in range(4):
            if not out_idx(xi+dx[i], yi+dy[i]) and box[xi+dx[i]][yi+dy[i]] == 1:
                if box[xi+dx[i]][yi+dy[i]] == 1:  # 단지이면
                    q.append((xi+dx[i], yi+dy[i]))  # 큐에 더해라
                    box[xi+dx[i]][yi+dy[i]] = 2  # 방문처리
                    cnt += 1
    return cnt

n = int(input())
q = collections.deque([])
box = []
for _ in range(n):
    kk = list(map(int, input()))
    box.append(kk)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 우 하 좌 상
cnt = 0
total = []
for i in range(n):
    for j in range(n):
        if box[i][j] == 1:
            total.append(bfs(i, j))
print(len(total))
for kkk in total:
    print(kkk)