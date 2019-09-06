import sys
sys.stdin = open('1961.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    a = []
    n = int(input())
    for _ in range(n):
        a.append(list(map(int,input().split())))


    num = len(a)
    empty90 = [[0]*num for i in range(num)]
    empty180 = [[0]*num for i in range(num)]
    empty270 = [[0]*num for i in range(num)]

    for i in range(num):  # 0 1 2
        for j in range(num):  # 0 1 2
            empty270[i][j] = a[j][(n-1)-i]

    for i in range(num):
        for j in range(num):
            empty90[i][j] = a[(n-1)-j][i]

    for i in range(num):
        for j in range(num):
            empty180[i][j] = a[(n-1)-i][(n-1)-j]

    big = []  # 전체 리스트로 모아서 프린트하기
    for j in empty90:
        new = ''.join(list(map(str,j)))
        big.append(new)
    for j in empty180:
        new = ''.join(list(map(str,j)))
        big.append(new)
    for j in empty270:
        new = ''.join(list(map(str,j)))
        big.append(new)
    print('#{}'.format(tcc))
    for k in range(n): # 0 1 2 3 4 5
          print(big[k], big[n+k], big[2*n+k])











