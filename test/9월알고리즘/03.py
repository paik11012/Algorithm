import sys
from pprint import pprint
import collections
sys.stdin = open('03.txt', 'r')


def bfs(x, y, cnt):
    q = collections.deque([])
    q.append(x, y, cnt)
    while



a, b, c = map(int, input().split())
box = []
for _ in range(b):
    box.append(list(map(int, input().split())))
pprint(box)
for i in range(b):
    for j in range(a):
        if box[i][j] == 1:
            bfs(i, j, c)