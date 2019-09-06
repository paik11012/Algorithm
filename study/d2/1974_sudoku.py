import sys
from pprint import pprint
from typing import Any, Union
sys.stdin = open('1974.txt','r')
total = int(input())
for tcc in range(1, total+1):
    box = []  #큰 리스트
    for z in range(9):
        b = list(map(int,input().split()))
        box.append(b)
    # pprint(box)
    flag = 1  # 문제 없음
    cnt = [0,0,0,0,0,0,0,0,0]  # 가로랑 세로라인 더한 것(90이 10개 나오면 정상)
    for i in range(9):
        for j in range(9):
            cnt[i] += box[i][j]
            cnt[i] += box[j][i]
    if cnt.count(90) != 9:
        flag = 0

    set_list = []
    for x in range(0, 9, 3):  # 0 3 6
        for y in range(0, 9, 3):  # 0 3 6
            check = []  # 매번 초기화
            for i in range(x, x+3):
                for j in range(y, y+3):
                    check.append(box[i][j])
            set_list.append(len(set(check)))
    if set_list.count(9) != 9: flag = 0

    print('#{} {}'.format(tcc, flag))