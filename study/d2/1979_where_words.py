import sys
from typing import Any, Union
sys.stdin = open('1979.txt','r')

N, K = map(int, input().split())
row_list = [''.join(input().split()) for n in range(N)]  # 값을 str로 바꿈(행)
col_list = [''.join(i) for i in zip(*row_list)]  # 값을 str로 바꿈(열) zip(*)

cnt = 0
for l in (row_list, col_list):
    for i in l:
        cnt += i.split('0').count('1' * K)
# new = '01001'.split('0')  = ['', '1', '', '1']
# new = ['','111','1'].count('1'*3)
# print(new)

# column_box = list(map(list, zip(*list_temp)))


