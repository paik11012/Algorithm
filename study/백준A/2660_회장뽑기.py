import sys
from pprint import pprint
sys.stdin = open('2660.txt', 'r')


def bfs(x):
    visited = [False] * (n + 1)
    q = []
    q.append((x, 0))
    visited[x] = True
    while q:
        # print(q)
        node, cnt = q.pop(0)
        # print(node)
        for ii in num[node]:  # 연결된 노드 모음 [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
            if not visited[ii]:  # ii중에 방문하지 않은 node가 1개라도 있으면 cnt를 +1
                visited[ii] = True
                q.append((ii, cnt+1))
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

candidate = []
for jj in range(1, n+1):
    candidate.append(bfs(jj))
m = min(candidate)
result = []
for jjj in range(n):
    if candidate[jjj] == m:
        result.append(jjj+1)
print(m, len(result))
print(' '.join(list(map(str, result))))