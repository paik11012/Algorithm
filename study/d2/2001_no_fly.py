import sys
from pprint import pprint
sys.stdin = open('2001.txt','r')

def boxsum(i, j, m): # 4 4
    val = 0 
    for x in range(i, i+m):
        for y in range(j, j+m):
            val  += box[x][y]
    return val

n, m = map(int, input().split())  # n 박스 크기 m 파리채 크기
box = []
for _ in range(n):
    line = list(map(int, input().split()))
    box.append(line)

max_sum = 0
for i in range(n-m+1):
    for j in range(n-m+1):
        res =  boxsum(i, j, m)
        if max_sum < res:
            max_sum = res
print(max_sum)