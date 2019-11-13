import sys
from pprint import pprint
sys.stdin = open('등산로.txt', 'r')
'''
우선 가장 높은 숫자를 
'''


m, n = map(int, input().split())
box = []
for _ in range(m):
    box.append(list(map(int, input().split())))
pprint(box)
