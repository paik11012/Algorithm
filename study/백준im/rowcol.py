import sys
from pprint import pprint
sys.stdin = open('rowcol.txt','r')
case = int(input())
box = []
for _ in range(case):
    box.append(list(map(int,input().split())))


for i in range(case):
    for j in range(case):
        if box[i][j] != 0:
            print(i, j)



# pprint(box)