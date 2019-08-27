tc = int(input())
for tcc in range(1, tc+1):
    print('#{}'.format(tcc))
    
    l=[]  # 숫자 전체 리스트
    num = int(input())
    for i in range(1, (num*num)+1): # 1부터 16
        l.append(i)
    snail = [[0] * num for _ in range(num)]  # 숫자를 넣으려고 하는 리스트
    # 배열이 뭐냐? 변수 여러개
    X = 0  # 내가 숫자를 넣으려고 하는 좌표(인덱스) => 행
    Y = 0  # 열
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0

    def iswall(x,y):
        if x < 0 or x >= num: return True
        if y < 0 or y >= num: return True
        if snail[x][y] != 0: return True
        return False


    for i in range(1, num*num+1):
        snail[X][Y] = i
        X += dx[d]
        Y += dy[d]
        if iswall(X+dx[d], Y+dy[d]): # wall이면 방향 전환
            d = (d + 1) % 4

    for ii in range(num):
        p = ''
        for jj in range(num):
            p += str(snail[ii][jj]) + ' '
        print(p)

