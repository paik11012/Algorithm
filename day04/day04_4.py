import sys
sys.stdin = open('4.txt', 'r')

for tot in range(1, 11):
    num = int(input())
    a = []  # 2x2 매트릭스 완성
    for i in range(8):
        b = a.append(list(input()))

    count = 0
    for x in range(8):  # 행
        for y in range(8-num+1):  # 열
            for z in range(int(num//2)): # num이 4니까 2번 비교
                if a[x][y+z] != a[x][num+y-z-1]: # [0][0]
                    break
            else:
                count += 1
            for z in range(int(num // 2)):
                if a[y+z][x] != a[num+y-z-1][x]:
                    break
            else:
                count += 1
    print('#{0} {1}'.format(tot, count))