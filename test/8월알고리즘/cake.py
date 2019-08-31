import sys
from pprint import pprint
sys.stdin = open('cake.txt','r')

n = int(input())
box = []
for i in range(n):
    box.append(list(map(int,input().split())))

pprint(box)