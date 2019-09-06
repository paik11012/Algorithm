from pprint import pprint
box = [[1,0,0,0,1,0,1],
       [1,0,0,0,1,0,1],
       [1,1,1,1,1,0,1],
       [1,0,0,0,1,1,1],
       [1,0,0,0,1,0,1],
       [1,0,0,0,1,0,1],
       [1,0,0,0,2,0,1]]

def out_idx(i, j):
    if i<0 or i > 6: return True
    if j<0 or j > 6: return True
    return False


for x in range(7):
    for y in range(7):
        if box[x][y] == 2:
            X = x
            Y = y

visited = [[1] * 7 for i in range(7)]
visited[X][Y] = 9  # 첫 방문 채워주기

while X != 0:  # 맨 위에 닿을 때까지 계속해라
    if box[X-1][Y] == 1:  # 위에가 1이면 위로 올라가라, 위치를 바꿔라
        X = X -1
        visited[X][Y] = 9
        if box[X][Y+1] == 1 and visited[X][Y+1] != 9 and out_idx(X,Y+1) == False:  # 왼쪽이 1이고 visited가 체크되어있지 않으이면
            visited[X][Y] = 9  # 먼저 현재 채우기
            Y =  Y+1
            visited[X][Y] = 9  # 이동 후 채우기
            while box[X-1][Y] != 1 and out_idx(X,Y+1) == False:  # 위칸이 1일 때까지
                visited[X][Y] = 9
                X = X-1

            pprint(visited)

