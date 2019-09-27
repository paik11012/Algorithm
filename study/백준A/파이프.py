import sys
from pprint import pprint
sys.stdin = open('17070.txt', 'r')


def dfs(xi, yi, pipe):
    global cnt
    if xi == n-1 and yi == n-1:
        cnt += 1
        return
    if pipe == 0:
        if yi+1 < n and box[xi][yi+1] == 0:
            dfs(xi, yi+1, 0)
        if xi+1 < n and yi+1 < n and box[xi+1][yi+1] == 0 and box[xi][yi+1] == 0 and box[xi+1][yi] == 0:
            dfs(xi+1, yi+1, 2)
    if pipe == 1:
        if xi+1 < n and box[xi+1][yi] == 0:
            dfs(xi+1, yi, 1)
        if xi+1 < n and yi+1 < n and box[xi+1][yi+1] == 0 and box[xi][yi+1] == 0 and box[xi+1][yi] == 0:
            dfs(xi+1, yi+1, 2)
    if pipe == 2:
        if yi+1 < n and box[xi][yi+1] == 0:
            dfs(xi, yi+1, 0)
        if xi+1 < n and box[xi+1][yi] == 0:
            dfs(xi+1, yi, 1)
        if xi+1 < n and yi+1 < n and box[xi+1][yi+1] == 0 and box[xi][yi+1] == 0 and box[xi+1][yi] == 0:
            dfs(xi+1, yi+1, 2)


n = int(input())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))
cnt = 0
dfs(0, 1, 0)
print(cnt)

