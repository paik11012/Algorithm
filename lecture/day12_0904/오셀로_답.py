import sys
from pprint import pprint
sys.stdin = open('오셀로.txt', 'r')

TC = int(input())

def isWall(x, y, chesspan_length):
    if x < 0 or x > chesspan_length - 1: return True
    if y < 0 or y > chesspan_length - 1: return True
    return False

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

for test_case in range(1, TC + 1):
    chesspan_length, N = map(int, input().split())

    # 체스판 만들기
    chesspan = [[0] * chesspan_length for _ in range(chesspan_length)]
    chesspan[chesspan_length // 2][chesspan_length // 2] = chesspan[(chesspan_length // 2) - 1][
        (chesspan_length // 2) - 1] = 2
    chesspan[chesspan_length // 2][(chesspan_length // 2) - 1] = chesspan[(chesspan_length // 2) - 1][
        chesspan_length // 2] = 1

    for _ in range(N):
        x, y, color = list(map(int, input().split()))
        x -= 1
        y -= 1
        chesspan[y][x] = color  # 자기 것 바꿔주기

        checks = []
        for diff in range(8):  # 0부터 7까지 방향
            check = []
            new_x = x + dx[diff]  # 방향 바꾸기
            new_y = y + dy[diff]
            while True:  # 계속 돌아라 break할 때까지
                if isWall(new_x, new_y, chesspan_length) == True:
                    check = []  # 초기화
                    break
                if chesspan[new_y][new_x] == 0:
                    check = []  # 초기화
                    break
                if chesspan[new_y][new_x] == color:  # 같은 색깔이면 깨고 다음으로 이동
                    break
                else:  # 그렇지 않으면(색이 다르면) check에 색이 다른 좌표 넣는다
                    check.append([new_y, new_x])
                    new_x = new_x + dx[diff]
                    new_y = new_y + dy[diff]
            checks.extend(check)

            # print(checks)
        # print(checks)
        for i in checks:
            chesspan[i[0]][i[1]] = color

        # 돌 색깔 세기
        black = 0
        white = 0
        for i in range(chesspan_length):
            for j in range(chesspan_length):
                if chesspan[i][j] == 1:
                    black += 1
                if chesspan[i][j] == 2:
                    white += 1

    print('#%s %s %s' % (test_case, black, white))