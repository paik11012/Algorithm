import sys
from pprint import pprint
sys.stdin = open('5_1.txt', 'r')

num = int(input())
a = []
count = 1
for i in range(100):
    a.append(list(input()))  # 100x100 2차행렬 만듬

for x in range(100):  # 행
    for y in range(100):  # 열
        num = 1
        for z in range(num): # num이 4니까 2번 비교, 기준
            if a[x][y+z] != a[x][num+y-z]: # [0][0]
                break
            else:  # [0][0]과 [0][1]이 같으면 [0][0]과 [0][2]를 비교해라
                num += 1


