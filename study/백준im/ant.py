import sys
from pprint import pprint
sys.stdin = open('ant.txt','r')
tc = int(input())
for tc in range(1, tc+1):
    box_size = int(input())  # 10
    box = []
    for _ in range(box_size):
        line = list(map(int, input().split()))
        box.append(line)

    def wall1(x, y):  # <<방향>> 전환만 하는 함수
        if x == 0 and y == 1: return 'up'
        if x == 0 and y == -1: return 'down'
        if x == -1 and y == 0: return 'right'
        if x == 1 and y == 0: return 'left'

    def wall2(x, y):  # 방향전환만 하는 함수
        if x == 0 and y == 1: return 'down'  # 좌
        if x == 0 and y == -1: return 'up'  # 우
        if x == -1 and y == 0: return 'left'  # 상
        if x == 1 and y == 0: return 'right'  # 하

    X = 0  # 위치
    Y = 0
    dx = 0  # 이동 방향
    dy = 1
    cnt = 0
    while True:
        X = X + dx
        Y = Y + dy
        if X < 0 or X >= box_size: break
        if Y < 0 or Y >= box_size: break  # 숫자가 있는 범위에서 벗어나면 break
        cnt += 1
        if box[X][Y] == 1:
            if wall1(dx, dy) == 'up':
                dx, dy = -1, 0
            elif wall1(dx, dy) == 'down':
                dx, dy = 1, 0
            elif wall1(dx, dy) == 'left':
                dx, dy = 0, -1
            elif wall1(dx, dy) == 'right':
                dx, dy = 0, 1
        elif box[X][Y] == 2:
            if wall2(dx, dy) == 'up':
                dx, dy = -1, 0
            elif wall2(dx, dy) == 'down':
                dx, dy = 1, 0
            elif wall2(dx, dy) == 'left':
                dx, dy = 0, -1
            elif wall2(dx, dy) == 'right':
                dx, dy = 0, 1
        print(X, Y)
    print('#{} {}'.format(tc,cnt))

