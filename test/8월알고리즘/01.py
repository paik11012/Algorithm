import sys
sys.stdin = open('01.txt','r')
total = int(input())
for tot in range(1, total+1):
    size, n = map(int,input().split())
    arr = [[0] * size for i in range(size)]
    cnt = 0
    for num in range(n):
        r1, c1, r2, c2 = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    cnt += 1
    print('#{} {}'.format(tot,cnt))
