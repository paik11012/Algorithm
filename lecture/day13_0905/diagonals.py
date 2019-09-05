import sys
sys.stdin = open('diagonals.txt','r')
def first(n):  # 몇 번째 줄에 속하는가
    if n < 3:
        return n
    return first(n-1) + n - 1

def getcha(j, k): # 몇 컴마 몇에 숫자가 몇이 들어가나
    if j == 1 and k == 1: return 1
    cnt = first(j)  # 높이
    for i in range(k-1): # 0 1 2
        cnt += (i+j+1)
    return cnt

num_list = [[0] * 151 for _ in range(150)]
for x in range(1, 150):
    for y in range(1, 150):
        num_list[x][y] = getcha(x,y)


tc = int(input())
for tcc in range(1, tc+1):
    a, b = map(int, input().split())
    for xx in range(150):
        for yy in range(150):
            if num_list[xx][yy] == a:
                x1 = xx
                y1 = yy
    for xxx in range(150):
        for yyy in range(150):
            if num_list[xxx][yyy] == b:
                x2 = xxx
                y2 = yyy
    print('#{} {}'.format(tcc,getcha(x1 + x2, y1 + y2))) # 새로운 좌표 만들기
