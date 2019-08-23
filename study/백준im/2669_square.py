big = [[0]*100 for i in range(100)]
cnt = 0

for i in range(4):
    a = list(map(int,input().split()))
      # 8 * 8 빈 행렬 나중에는 100곱하기 100으로
    for x in range(a[0], a[2]):  #
        for y in range(a[1], a[3]):  #
            if not(big[x][y]): # 비지 않았다면
                big[x][y] = 1
                cnt += 1
print(cnt)