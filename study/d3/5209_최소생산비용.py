import sys
from pprint import pprint
sys.stdin = open('5209.txt', 'r')


def per(idx, cnt):
    global minn
    if cnt > minn:
        return
    if idx == size:
        if minn > cnt:
            minn = cnt
    else:
        for i in range(1, size+1): #
            if not visited[i]:
                visited[i] = True
                arr[idx] = i
                per(idx + 1, cnt + box[idx][i-1])  # 바로 커진 것을 넘긴다
                visited[i] = False


size = int(input())
box = []
arr = [0] * size
minn = 9999
visited = [False] * (size+1)
for _ in range(size):
    box.append(list(map(int, input().split())))
per(0, 0)
print(minn)