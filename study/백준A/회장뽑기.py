import sys
from pprint import pprint
sys.stdin = open('2660.txt', 'r')

n = int(input())
a, b = map(int, input().split())
box = [[0] * (n+1) for _ in range(n+1)]
while a != 1 and b != 1:
    box[a][b] = 1
    box[b][a] = 1
    a, b = map(int, input().split())
    print(a, b)
pprint(box)