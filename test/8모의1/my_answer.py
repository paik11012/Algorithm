from pprint import pprint
import sys
sys.stdin = open('one.txt','r')

row, col, num = map(int, input().split())
box = [[0] * col for _ in range(row)]
new_box = [[0] * col for _ in range(row)]

for _ in range(num):
    r1, c1, r2, c2, color = map(int, input().split())
    check = []
    for x in range(r1, r2+1):
        for y in range(c1, c2+1):
            check.append(box[x][y])
            box[x][y] = color


    if max(check) <= color:
        for iii in range(r1, r2 + 1):
            for jjj in range(c1, c2 + 1):
                new_box[iii][jjj] = color
#
pprint(new_box)