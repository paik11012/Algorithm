import collections
import sys
from pprint import pprint
sys.stdin = open('5105.txt', 'r')


def dfs(x, y, cnt):
    q.append((x, y, cnt))
    visited[x][y] = 1
    while q:
        xi, yi, cnt = q.popleft()
        for ii in range(4):
            xii = xi + dx[ii]
            yii = yi + dy[ii]
            if 0 <= xii < size and 0 <= yii < size and not visited[xii][yii] and box[xii][yii] != '1':  # 범위 안이고 방문하지 않았으면
                visited[xii][yii] = 1
                q.append((xii, yii, cnt + 1))
                if box[xii][yii] == '3':
                    return cnt


size = int(input())
box = []
for _ in range(size):
    box.append(list(input()))
q = collections.deque([])
visited = [[0] * size for _ in range(size)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(size):
    for j in range(size):
        if box[i][j] == '2':
            result = dfs(i, j, 0)
if not result:
    result = 0
print(result)
