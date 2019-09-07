from pprint import pprint
import sys
sys.stdin = open('ladder.txt','r')

for tcc in range(1, 11):
    tc = int(input())
    box = []
    for j in range(100):
        box.append(list(map(int,input().split())))

    def out_idx(i, j):
        if i<0 or i > 99: return True
        if j<0 or j > 99: return True
        return False

    for x in range(100):
        for y in range(100):
            if box[x][y] == 2:
                X = x
                Y = y

    visited = [[0] * 100 for i in range(100)]
    visited[X][Y] = 1  # 첫 방문 채워주기

    while X != 0:  # 맨 위에 닿을 때까지 계속해라
        visited[X][Y] = 1
        if out_idx(X,Y+1) == False and box[X][Y+1] == 1 and visited[X][Y+1] != 1:  # 왼쪽이 1이고 visited가 체크되어있지 않으이면
            Y =  Y+1
        elif out_idx(X,Y-1) == False and box[X][Y-1] == 1 and visited[X][Y-1] != 1: # 왼쪽으로 가는 것 체크
            Y = Y-1
        elif box[X-1][Y] == 1:  # 왼쪽오른쪽이 없으면 위로 올라가라
            X = X -1
        print(X,Y)
    visited[X][Y] =1
    # print(Y)
    # pprint(visited)

