import sys
from pprint import pprint
sys.stdin = open('maze.txt','r')
n = 5
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def out_idx(yy,xx):
    if xx < 0 or xx > n-1: return True
    if yy < 0 or yy > n-1: return True
    return False

def dfs(y,x):
    global result
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if out_idx(Y,X) == False and visited[Y][X] == 0 and maze[Y][X] != 1:
            visited[Y][X] = 1
            # print(Y, X)
            if maze[Y][X] == 3:
                result = 1
                break
            else: return dfs(Y, X)

for i in range(n):  # y
    for j in range(n):  # x
        if maze[i][j] == 2:
            starty = i
            startx = j
# print(starty, startx)

result = 0
visited = [[0] * n for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]  # 하 상 좌 우
dfs(starty, startx)  # 0 1
print(result)
pprint(visited)