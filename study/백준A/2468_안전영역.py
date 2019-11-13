import sys
from pprint import pprint
import collections
sys.stdin = open('2468.txt', 'r')

def bfs(x, y):
    q = collections.deque([])
    visited[x][y] = 1  # 들어가자마자 visited처리하기(bfs)
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for kk in range(4):  # 네 방향 탐색하면서 안전영역 탐색하기
            X = xx + dx[kk]
            Y = yy + dy[kk]
            if 0 <= X < size and 0 <= Y < size and visited[X][Y] == 0 and box[X][Y] > rain:
            #  만약 X, Y 둘다 범위 안이고 아직 방문하지 않았고 안전영역이라면옛
                visited[X][Y] = 1
                q.append((X, Y))


size = int(input())
box = []  # 처음 맵 만들기
for _ in range(size):
    box.append(list(map(int, input().split())))
maxx = 0  # 영역의 최대값을 구해 그 영역까지 비가 잠긴다고 가정한다
for i in range(size):
    for j in range(size):
        if maxx < box[i][j]:
            maxx = box[i][j]

big = 0  # 결과: 가장 큰 안전영역의 개수 저장하기
dx = [1, 0, -1, 0]  # 네 방향 탐색 위해 dx, dy 마련
dy = [0, -1, 0, 1]
for rain in range(0, maxx):
    cnt = 0
    visited = [[0] * size for _ in range(size)]
    for ii in range(size):
        for jj in range(size):
            if box[ii][jj] > rain and visited[ii][jj] == 0:
                # pprint(visited)
                cnt += 1  # 이 부분이 제일  중요!!!!
                bfs(ii, jj)
    if cnt > big:
        big = cnt
print(big)
