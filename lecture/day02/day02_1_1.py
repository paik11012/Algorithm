import json
import sys
from typing import Any, Union
sys.stdin = open('sample_1.txt','r')


def cnt(arr):  #숫자가 3이면 세는 함수
    cnt = 0
    for a in range(10):
        for b in range(10):
            if arr[a][b] == 3:
                cnt += 1
    return cnt


total = int(input())
for tot in range(1, total+1):
    first = [[0]*10 for m in range(10)]  #숫자 넣을 빈 리스트 만들기
    area_num = int(input())  # 몇 번 숫자 넣을건지 받아오기
    for i in range(area_num):
        r1, c1, r2, c2, color = map(int, input().split())  # 포문을 돌면서 숫자 5개 생성
        for k in range(r1,r2+1):  # 1, 3
            for l in range(c1,c2+1):  # 2, 3 행 열에 색 채우기
                first[k][l] += color
    print('#{0} {1}'.format(tot, cnt(first)))