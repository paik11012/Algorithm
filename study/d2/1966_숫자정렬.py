import sys
from typing import Any, Union
sys.stdin = open('1966.txt','r')

def bubsort(n):
    for i in range(len(n)):
        for j in range(len(n)-1-i):  # 뒤에 갈수록 비교 개수를 줄인다, 큰것 맨 뒤에 보내고 또 정렬
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

tc = int(input())
for tcc in range(1, 11):
    num = int(input())
    nums = list(map(int, input().split()))
    r = bubsort(nums)
    print('#{}'.format(tcc), end = ' ')
    print(' '.join(list(map(str, r))))