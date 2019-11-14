import sys
from pprint import pprint
import collections
sys.stdin = open('2573.txt', 'r')

'''
빙산이 물을 만나면 물을 만난 회수 만큼 빙산을 1씩 줄여나가고 0이 되면 물이 된다
한 턴을 돌릴 때마다 빙산의 갯수가 몇 개 남았는지 확인해나가고 그 빙산의 개수가 2개가 되면
몇 번 턴을 돌렸는지 세어 그 횟수를 반환한다
빙산을 녹인다 -> 빙산이 몇 개 남았는지 확인한다 -> 빙산이 2개 이상이면 break, 2개 미만이면 1년을 더하고 또 녹인다
1. 빙산이 2개인가?
2. 아니라면 주변 0의 개수만큼 ice 값을 녹여준다.
3. iceCnt 를 갱신
4. ans(년의 횟 수)++
'''


def bfs(xi, yi):  # 섬 몇개인지 세기
    q = collections.deque([])
    visited[xi][yi] = 1
    q.append((xi, yi))
    copied = [[0] * n for _ in range(m)]
    for xx in range(m):
        for yy in range(n):
            copied[xx][yy] = box[xx][yy]
    while q:
        x, y = q.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0 <= X < m and 0 <= Y < n and box[X][Y] == 0 and visited[X][Y] == 0:
                visited[X][Y] = 1
                copied[x][y] -= 1
                q.append((X, Y))
    pprint(copied)

m, n = map(int, input().split())
box = []
for _ in range(m):
    box.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * n for _ in range(m)]
q = collections.deque([])
cntt = 0
for ii in range(m):
    for j in range(n):
        if box[ii][j] != 0 and visited[ii][j] == 0:
            # cntt += 1  # 처음에 들어갈 때 cntt늘려주기
            bfs(ii, j)
