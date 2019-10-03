from pprint import pprint
import sys
import collections
sys.stdin = open('02.txt', 'r')


def bfs(x, y, cnt):
    q = collections.deque([])
    visited[x][y] = 1  # 방문 표시
    box[x][y] = 0
    q.append((x, y, cnt))
    while q:
        xi, yi, cnt = q.popleft()
        if box[xi][yi] == 1 or box[xi][yi] == 2 or box[xi][yi] == 3 or box[xi][yi] == 4 or box[xi][yi] == 5 or box[xi][yi] == 6:
            box[xi][yi] = 0
            cnt_list.append(cnt)
            break
        for ii in range(4):  # 네 방향 탐색
            if 0 <= xi+dx[ii] < 10 and 0 <= yi+dy[ii] < 10:  # 인덱스 밖이 아니고
                if visited[xi+dx[ii]][yi+dy[ii]] != 1 and box[xi+dx[ii]][yi+dy[ii]] != 9:  # visited하지 않았고, 1~6이 아니면
                    visited[xi+dx[ii]][yi+dy[ii]] = 1  # 방문처리
                    q.append((xi+dx[ii], yi+dy[ii], cnt + 1)) # q에 더하기
                    # print(q)


tc = int(input())
for tcc in range(1, tc+1):
    zero = int(input())
    box = []
    for _ in range(10):
        box.append(list(map(int, input().split())))
    visited = [[0] * 10 for _ in range(10)]
    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]
    cnt_list = []
    # main
    for i in range(10):
        for j in range(10):
            if box[i][j] == 9:  # 로봇이면
                visited = [[0] * 10 for _ in range(10)]
                bfs(i, j, 0)
    print('#{} {}'.format(tcc, sum(cnt_list)))
