import sys
from pprint import pprint
sys.stdin = open('2660.txt','r')


def bfs(x):
    visited = [False] * (n + 1)
    q = []
    visited[x] = True
    for j in range(len(num[x])):
        q.append(j)
    cnt = 0
    v_cnt = visited.count(True)
    while v_cnt < 5:
        node = q.pop()
        if visited[node] == False:
            for jj in range(len(num[node])):
                q.append(jj)
                visited[jj] = True
            cnt += 1
            if v_cnt == 5: break
    return cnt


n = int(input())
a, b = map(int, input().split())
box = [[0] * (n+1) for _ in range(n+1)]
while a != -1 and b != -1:  # a와 b가 -1이 아닌 동안 받아라
    box[a][b] = 1
    box[b][a] = 1
    a, b = map(int, input().split())
num = [[] for _ in range(n+1)]  # 연결된 노드 모음 [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
# pprint(box)

for i in range(n+1):
    for j in range(n+1):
        if box[i][j] == 1:
            num[i].append(j)



print(bfs(1))