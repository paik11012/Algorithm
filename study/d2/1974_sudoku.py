import sys
from pprint import pprint
from typing import Any, Union
sys.stdin = open('1974.txt','r')
total = int(input())
for tot in range(1, total+1):
    n = []  #큰 리스트
    for z in range(9):
        b = list(map(int,input().split()))
        n.append(b)
    cnt = [0,0,0,0,0,0,0,0,0]  # 가로랑 세로라인 더한 것(90이 10개 나오면 정상)
    for i in range(9):
        for j in range(9):
            cnt[i] += n[i][j]
            cnt[i] += n[j][i]
    cnt_90 = 0  # 90이 몇 개 있는지 세기(정상적인 가로 세로 열 합)
    for k in cnt:
        if k == 90:
            cnt_90 += 1
    if cnt_90 == 9:  # 정상이면 1, 아니면 0
        result = 1
    else: result = 0
    # 3x3 검증
    x = 0
    y = 0
    check = []
    for i in range(x, x+3):  # 0 3 6
        for j in range(y, y+3):  # 0 3 6
            check.append(n[i][j])
    if len(set(check)) != 9:
        result = 0


    print(check)




    # print('#{} {}'.format(tot, result))