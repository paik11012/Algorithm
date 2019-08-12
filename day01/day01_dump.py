import sys
from typing import Any, Union
sys.stdin = open('input.txt','r')


def bubsort(n):  # 한 번 정렬 함수
    n[0] += 1
    n[-1] -= 1
    for i in range(len(n)-1, 0, -1):  #
        for j in range(0,i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

total_case = 10
for total in range(1,total_case+1):
    dump_num = int(input())
    box_list = list(map(int, input().split()))  # 그래프 높이 리스트
    a = box_list
    for i in range(len(a)-1,0,-1):  # 첫 정렬 range(834)
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    # 첫 정렬 후 최솟값에 +1, 최댓값에 +1 넣기
    for k in range(dump_num):
        a = bubsort(a)
        result = a[-1]-a[0]
    print('#{0} {1}'.format(total, result))



