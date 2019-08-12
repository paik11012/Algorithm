
import sys
from typing import Any, Union
sys.stdin = open('sample_2.txt','r')
# N, K = 3, 6
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)
total_num = int(input())
for tot in range(1,total_num+1):
    N, K = map(int, input().split())
    candidate = []
    result = []
    total = 0

     #  bit이용하기
    n = len(arr)  # 12
    for i in range(1 << n):  # 2의 12승-1까지 생성 
        result += [[arr[j] for j in range(n) if i & (1 <<j)]]

    for n in result:
        if len(n) == N:
            candidate += [n]

    for z in candidate:
        if sum(z) == K:
            total += 1
    print('#{0} {1}'.format(tot,total))




