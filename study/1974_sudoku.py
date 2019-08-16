import sys
from pprint import pprint
from typing import Any, Union
sys.stdin = open('1974.txt','r')
total = int(input())
for tot in range(total):
    n= []  #큰 리스트
    for z in range(9):
        b = list(map(int,input().split()))
        n.append(b)
    
    cnt = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
        for j in range(9):
            cnt[i] += n[i][j]
    if 46 in cnt:
        print('F')
    else:
        print('Y')
