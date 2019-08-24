import sys
sys.stdin = open('02.txt','r')

# n, m, k를 받아서 가운데의 합을 구하는 함수
def squaresum(i, j, k):
    smallsum = 0
    for x in range(i, i+k):  # 가로 행 0~2 1~3 
        for y in range(j, j+k): # 세로 열 0~2 1~3 2~4
            smallsum += bigbox[x][y]
    return smallsum


total = int(input())
for tot in range(1, total+1):
    n, m, k = map(int,input().split())
    bigbox = []  # 전체 숫자 리스트
    maxsum = 0
    for _ in range(n):
        line = list(map(int,input().split()))
        bigbox.append(line)

    for i in range(n - k + 1): # i 위아래 검사 횟수 0 1 
        for j in range(m - k + 1):  # j 좌우 검사 횟수 0 1 2
            tsum = squaresum(i, j, k) - squaresum(i+1, j+1, k-2)
            if tsum > maxsum:
                maxsum = tsum

    print('#{} {}'.format(tot, maxsum))