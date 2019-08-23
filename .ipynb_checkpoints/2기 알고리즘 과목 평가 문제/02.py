import sys
sys.stdin = open('02.txt','r')
total = int(input())
for tot in range(1, total+1):
    n, m, k = map(int,input().split())
    arr = []
    for yo in range(n):
        line = list(map(int,input().split()))
        arr.append(line)

    new = [[0] * (m - k + 1) for i in range(n - k + 1)]  # 세로 x 가로 넣을 것 만들기
    n_list = []
    if k == 3:
        for i in range(n - 2):  # 0 1 2
            for j in range(m - k + 1):  # 0 1 2
                new[i][j] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 2] + \
                            arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
                n_list.append(new[i][j])

    elif k == 4:
        for i in range(n - k + 1):  # 0 1 2
            for j in range(m - k + 1):  # 0 1 2
                new[i][j] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3] \
                            + arr[i + 1][j] + arr[i + 1][j + 3] \
                            + arr[i + 2][j] + arr[i + 2][j + 3] \
                            + arr[i + 3][j] + arr[i + 3][j + 1] + arr[i + 3][j + 2] + arr[i + 3][j + 3]
                n_list.append(new[i][j])


    def maxx(num):
        maxnum = num[0]
        for p in num:
            if p > maxnum:
                maxnum = p
        return maxnum

    print('#{} {}'.format(tot, maxx(n_list)))