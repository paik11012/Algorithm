import sys
import collections
from pprint import pprint
sys.stdin = open('2636.txt', 'r')


def bfs(x, y, cnt):
    global visited, a, b
    q = collections.deque([])
    q.append((x, y, cnt))
    while q:
        print(q)
        xn, yn, cntn = q.popleft()
        for i in range(4):
            xii = xn + dx[i]
            yii = yn + dy[i]
            if 0 <= xii < a and 0 <= yii < b:
                if box[xii][yii] == 1 and not visited[xii][yii]:  # 주변에 1이 하나라도 있거나 방문하지 않았으면
                    visited[xii][yii] = 1
                    q.append((xii, yii, cntn + 1))


a, b = map(int, input().split())
box = []
for _ in range(a):
    box.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * b for _ in range(a)]
pprint(visited)
for xx in range(a):  # 13 세로
    for yy in range(b):  # 12  가로
        if 0 <= xx < a and 0 <= yy < b:  # 범위 안이면
            if box[xx][yy] == 0:
                bfs(xx, yy, 0)
pprint(visited)