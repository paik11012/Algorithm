import sys
from pprint import pprint
sys.stdin = open('maze.txt','r')

a = int(input())
box = []
for _ in range(a):
    box.append(list(map(int,list(input()))))
pprint(box)
