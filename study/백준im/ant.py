import sys
from pprint import pprint
sys.stdin = open('antex.txt','r')

def wall1(i, j):  # 받는 인자 = 현재 이동 방향 (0, 1)이면 우측 이동
    if i == -1 and j == 0: return  # 상




box_size = int(input())
box = []
for _ in range(box_size):
    line = list(map(int, input().split()))
    box.append(line)
pprint(box)