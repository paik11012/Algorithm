import sys
sys.stdin = open('sample_1.txt','r')
# 2
# 2 2 4 4 1
# 3 3 6 6 2


    first = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]
    area_num = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())  # 포문을 돌면서 리스트를 한 개씩 생성하겠다

    nn0 = [0] * 2
    nn1 = [0] * 2
    nn2 = [0] * 2
    for k in range(area_num):  # 0 1 2
        for i in range(2):
            nn0[i] = [n0[2 * i], n0[2*i+1]]
            nn1[i] = [n1[2 * i], n1[2 * i + 1]]
            try:
                nn2[i] = [n2[2 * i], n2[2 * i + 1]]
            except IndexError:  # 케이스 2개 들어오면 패스
                pass
    total = 0
    if area_num == 2:
        X_max = nn0[0][0], nn1[0][0]
        X_min = nn0[1][0], nn1[1][0]
        Y_max = nn0[0][1], nn1[0][1]
        Y_min = nn0[1][1], nn1[0][1]
        third = ((min(X_min) - max(X_max) + 1) * (min(Y_min) - max(Y_max) + 1))
        total += third
        print(total)

    if area_num == 3:
        X_max = nn1[0][0], nn2[0][0]
        X_min = nn1[1][0], nn2[1][0]
        Y_max = nn1[0][1], nn2[0][1]
        Y_min = nn1[1][1], nn2[1][1]
        first = ((min(X_min) - max(X_max) + 1) * (min(Y_min) - max(Y_max) + 1))
        total += first

        X_max = nn0[0][0], nn2[0][0]
        X_min = nn0[1][0], nn2[1][0]
        Y_max = nn0[0][1], nn2[0][1]
        Y_min = nn0[1][1], nn2[0][1]
        second = ((min(X_min) - max(X_max) + 1) * (min(Y_min) - max(Y_max) + 1))
        total += second

    print('#{0} {1}'.format(tot,total))







