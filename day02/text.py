import json
import sys
from typing import Any, Union
sys.stdin = open('sample_1.txt','r')


first = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def cnt(first):
    cnt = 0
    for a in range(10):
        for b in range(10):
            if first[a][b] == 3:
                cnt += 1
    return cnt


total = int(input())


for tot in range(1, total+1):
    area_num = int(input())  # 숫자 만큼 받아오기
    for i in range(area_num): # 0 1 2
        r1, c1, r2, c2, color = map(int, input().split())  # 포문을 돌면서 리스트를 한 개씩 생성하겠다
        for k in range(r1,r2+1):  # 1, 3
            for l in range(c1,c2+1):  #2, 3
                first[k][l] += color

    print('#{0} {1}'.format(tot, cnt(first)))




