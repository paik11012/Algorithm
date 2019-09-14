import sys
from pprint import pprint
sys.stdin = open('1253.txt','r')

n = int(input())
box = []
for _ in range(8):
    box.append(list(str(input())))
cnt = 0
for x in range(8): # 0~7
    for y in range(8-n+1):  # 시작점 설정  # 0~4까지
        flag = False
        for z in range(n//2):  # 0 1
            if box[x][y+z] == box[x][y+n-z-1]:
                flag = True
            else:
                flag = False
                break
        if flag == True:  # flag가 true면
            cnt += 1

for x in range(8):  # 0~7
    for y in range(8 - n + 1):  # 시작점 설정  # 0~4까지
        flag = False
        for z in range(n // 2):  # 0 1
            if box[y + z][x] == box[y + n - z - 1][x]:
                flag = True
            else:
                flag = False
                break
        if flag == True:  # flag가 true면
            cnt += 1
print(cnt)


