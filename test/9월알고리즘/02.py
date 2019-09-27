from pprint import pprint
import sys
import collections
sys.stdin = open('02.txt', 'r')


zero = int(input())
box = []
for _ in range(10):
    box.append(list(map(int, input().split())))
pprint(box)