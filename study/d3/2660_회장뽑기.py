import sys
from pprint import pprint
sys.stdin = open('2660.txt','r')

def bfs(x):
    cnt = 1
    visited = [False] * (n + 1)
    q = []
    q.append(num[x])
    visited[x] = True  # 1
    while q:  # 큐에 무엇인가 있는 동안 돌아가라
        print(q)
        node = q.pop()
        print(node)
    #     if not visited[node]:  # false이면
    #         visited[node] = True  # 자기처리
    #         q.append(visited[node])
    #         cnt += 1
    # return cnt



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
