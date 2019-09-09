import sys
from pprint import pprint
sys.stdin = open('maze.txt','r')
n = 5
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
# pprint(maze)

def out_idx(yy,xx):
    if xx < 0 or xx > n-1: return True
    if yy < 0 or yy > n-1: return True
    return False

def bfs(y,x):
    global result
    q.append((y,x))
    while q:  # q에 무엇이 있는 동안
        y, x = q.pop()
        for d in range(4):  # 네 방향을 돌면서  상 하 좌 우
            Y = y + dy[d]
            X = x + dx[d]
            if out_idx(Y,X) == False and maze[Y][X] != 1 and visited[Y][X] == 0: # 그 노드가 밖 범위가 아니고 방문하지 않았으면
                q.append((Y,X))  # 큐에다가 넣어라
                print(q)
                # print(Y, X)
                visited[Y][X] = 1  # 방문으로 표시
                if maze[Y][X] == 3:
                    result = 1
                    return

for i in range(n):  # y
    for j in range(n):  # x
        if maze[i][j] == 2:
            starty = i
            startx = j
# print(starty, startx)
q = []
result = 0
visited = [[0] * n for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1] # 하 상 좌 우
bfs(starty, startx)  # 0 1
print(result)
pprint(visited)