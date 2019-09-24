import sys
from pprint import pprint
sys.stdin = open('17070.txt', 'r')
# def out_idx(x,y):
#     if x > n-1 or x < 0: return True
#     if y > n-1 or y < 0: return True
#     return False


def dfs(x, y, pipe):  # 파이프 번호를 함께 소지하고 움직인다
    global cnt
    # print(x, y, pipe)
    if x == n-1 and y == n-1:
        cnt += 1
        return
    if pipe == 0:  # 우
        if y+1 < n and box[x][y+1] == 0: # 0 0 오른쪽이 비었고 범위 밖이 아니면
            dfs(x, y+1, 0)  # 오른쪽, 오른쪽 아래, 아래쪽이 박스 밖이 아니고, 0이라면
        if x+1 < n and y+1 < n and box[x + 1][y] == 0 and box[x + 1][y + 1] == 0:
            dfs(x+1, y+1, 2)  # 애는 위에가 다 돌아가길 기다리는 중
    if pipe == 1:  # 하
        if x+1 < n and box[x+1][y] == 0:
            dfs(x+1, y, 1)
        if  x+1 < n and y+1 < n and box[x][y + 1] == 0 and box[x + 1][y] == 0 and box[x + 1][y + 1] == 0:
            dfs(x+1, y+1, 2)
    if pipe == 2:  # 우하
        if y+1 < n and box[x][y+1] == 0: # 0 0 오른쪽이 비었고 범위 밖이 아니면
            dfs(x, y+1, 0)
        if x+1 < n and box[x+1][y] == 0: # 0 0 아래쪽이 비었고 범위 밖이 아니면
            dfs(x+1, y, 1)
        if x+1 < n and y+1 < n and box[x][y + 1] == 0 and box[x + 1][y] == 0 and box[x + 1][y + 1] == 0:
            dfs(x+1, y+1, 2)


n = int(input())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))
cnt = 0
dfs(0, 1, 0)
print(cnt)
