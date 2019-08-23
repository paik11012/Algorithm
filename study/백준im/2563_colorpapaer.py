# 3
# 3 7
# 15 7
# 5 2
from pprint import pprint
import sys
sys.stdin = open('2563.txt','r')
color = [[0] * 26 for _ in range(26)]
total = int(input())
for i in range(total):
    ac, ar = map(int, input().split())
    for x in range(ac, ac+10):
        for y in range(ar, ar+10):
            if color[x][y] == 0:
                color[x][y] = 1
            else: pass

pprint(color)
cnt = 0
for x in range(26):
    for y in range(26):
        if color[x][y] == 1:
            cnt += 1
print(cnt)