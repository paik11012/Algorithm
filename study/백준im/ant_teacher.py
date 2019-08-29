import sys
from pprint import pprint
sys.stdin = open('ant.txt','r')

move = [[3, 2], [2, 3], [1, 0], [0, 1]]  # 앞이 1번벽 뒤가 2번벽 // #  0 1 2 3 인덱스 뜻은 아래 위 우 좌로 이동
# 3의 의미: 위치 인덱스가 0 이니까 아래로 가다가 1번벽을 만나면 3번 방향 왼쪽으로 틀어라
# 2의 의미: 위치 인데스가 0 이니까 아래로 가다가 2번벽을 만나면 2번 방향 오른쪽으로 틀어라

for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    x, y = 0, 0
    di = 3  # 움직인는 방향 인덱스
    while True:
        if di == 0:
            y -= 1
        elif di == 1:
            y += 1
        elif di == 2:
            x -= 1
        else:
            x += 1
        if 0 > x or x >= N or 0 > y or y >= N:
            break
        if board[y][x]:
            di = move[di][board[y][x] - 1]
        cnt += 1
        # print(y, x)
    print('#{0} {1}'.format(case, cnt))