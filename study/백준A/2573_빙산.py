import sys
import copy
from pprint import pprint
import collections
sys.stdin = open('2573.txt', 'r')

'''
빙산이 물을 만나면 물을 만난 회수 만큼 빙산을 1씩 줄여나가고 0이 되면 물이 된다
한 턴을 돌릴 때마다 빙산의 갯수가 몇 개 남았는지 확인해나가고 그 빙산의 개수가 2개가 되면
몇 번 턴을 돌렸는지 세어 그 횟수를 반환한다
단 녹이고 -> 녹아서 바다가 된 부분 처리하고 -> 빙산 남았는지 확인하고 -> 확인해서 남았으면 bfs로 빙산 덩어리 개수 셌어
'''


def bfs(xii, yii):  # cnt는 섬 몇개인지 세기
    global cntt, years  # 0으로 시작
    # 녹인다
    while cntt < 2:  # while한 번 돌 때마다 한 번 녹이는 작업
        global copied  # 처음에는 박스 복사
        years += 1  # 1년 추가
        new_copied = [[0] * n for _ in range(m)]  # copied를 복사
        for xxx in range(m):
            for yyy in range(n):
                new_copied[xxx][yyy] = copied[xxx][yyy]

        for x in range(m):
            for y in range(n):
                if copied[x][y] != 0:  # copied 참고
                    for ii in range(4):
                        if copied[x+four_x[ii]][y+four_y[ii]] == 0:
                            new_copied[x][y] -= 1  # 바꾸는건 c_box
                            if new_copied[x][y] < 0:
                                new_copied[x][y] = 0
        # 녹아서 바다로 된 부분을 처리한다
        for xi in range(m):
            for yi in range(n):
                copied[xi][yi] = new_copied[xi][yi]

        # while을 한 번 돌릴 때마다 섬이 몇 개 남았는지 센다
        cntt += 1  # 처음 들어갈 때 cntt늘리기
        visited[xii][yii] = 1
        q.append((xii, yii))
        while q:
            X, Y = q.popleft()
            for i in range(4):  # 5m 7n
                # 범위를 넘지 않았고, 주변에 숫자가 있고, 방문하지 않았다면
                if 0 <= X + four_x[i] <= n and 0 <= Y + four_y[i]<= m and box[X + four_x[i]][Y + four_y[i]] != 0 and visited[X + four_x[i]][Y + four_y[i]] == 0:
                    visited[X + four_x[i]][Y + four_y[i]] = 1
                    q.append((X + four_x[i], Y + four_y[i]))


m, n = map(int, input().split())
box = []
for _ in range(m):
    box.append(list(map(int, input().split())))

copied = [[0] * n for _ in range(m)]
for xx in range(m):
    for yy in range(n):
        copied[xx][yy] = box[xx][yy]

four_x = [1, 0, -1, 0]
four_y = [0, 1, 0, -1]

visited = [[0] * n for _ in range(m)]
q = collections.deque([])
cntt = 0
years = 0
for i in range(m):
    for j in range(n):
        if box[i][j] != 0 and visited[i][j] == 0:
            cntt += 1
            bfs(i, j)
print(cntt, years)
