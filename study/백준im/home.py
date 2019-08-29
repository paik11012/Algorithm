from pprint import pprint
import sys
# 기지국 A는 위 아래 오른쪽 왼쪽을 한 칸씩 커버하고
# 기지국 C는 위 아래 오른쪽 왼쪽을 세 칸씩 커버한다. (자신 제외)
# 첫째줄은 테스트케이스 수, 둘째줄은 데이터를 받는 갯수를 뜻한다.
# 문제: 집 중에서 기지국의 신호를 받지 못하는 집의 갯수는?


sys.stdin = open('home.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    data_num = int(input())
    box = []  # 한 개씩 잘려진 박스
    for _ in range(data_num):
        line = list(map(str,input()))
        box.append(line)

    padding = [[0] * (data_num+6) for i in range(data_num+6)]
    for x in range(3, data_num+3):
        for y in range(3, data_num+3):
            padding[x][y] = box[x-3][y-3]
    # pprint(padding)


    for x in range(3, 12):
        for y in range(3, 12):
            if padding[x][y] == 'A':
                padding[x][y+1] = 'X' #d
                padding[x][y - 1] = 'X' #u
                padding[x+1][y] = 'X' # 오른쪽
                padding[x-1][y] = 'X' # 왼쪽
            if padding[x][y] == 'C':
                padding[x][y + 1] = 'X'
                padding[x][y + 2] = 'X'
                padding[x][y + 3] = 'X'
                padding[x][y - 1] = 'X'
                padding[x][y-2] = 'X'
                padding[x][y - 3] = 'X'
                padding[x + 1][y] = 'X'
                padding[x + 2][y] = 'X'
                padding[x + 3][y] = 'X'
                padding[x - 1][y] = 'X'
                padding[x - 2][y] = 'X'
                padding[x - 3][y] = 'X'

    cnt = 0
    for r in padding:
        cnt += r.count('H')
    print(cnt)
