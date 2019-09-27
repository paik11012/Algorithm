import collections
import sys
from pprint import pprint
sys.stdin = open('보물섬.txt', 'r')

m, n = map(int, input().split())
box = []
for _ in range(m):
    box.append(list(str(input())))


def out_idx(i, j):  # x는 5까지 가능
    if i > m-1 or i < 0: return True  # 5부터 out_idx
    if j > n-1 or j < 0: return True  # 7부터 out_idx
    return False


def bfs(x, y, cnt):
    q = collections.deque([])
    visited[x][y] = 1  # 방문 처리
    q.append((x, y, cnt))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            xi = x+dx[i]
            yi = y+dy[i]  # 범위 밖이 아니고, 육지이고, 방문하지 않았으면
            if not out_idx(xi, yi) and box[xi][yi] == 'L' and visited[xi][yi] == 0:
                visited[xi][yi] = 1  # 방문 처리
                q.append((xi, yi, cnt + 1))
    return cnt


dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]

total = []
for xx in range(m):
    for yy in range(n):
        if box[xx][yy] == 'L':
            visited = [[0] * n for _ in range(m)]  # visited 초기화
            total.append(bfs(xx, yy, 0))
print(max(total))
