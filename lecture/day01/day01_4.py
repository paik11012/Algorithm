# n개의 정수가 들어있는 배열에서 이웃한 m개의 합을 계산하는 것
# m의 합이 가장 큰 경우와 가장 작은 경우의 차이 출력
# n은 총갯수, m은 기준갯수
# 10 3
# 1 2 3 4 5 6 7 8 9 10
import sys
from typing import Any, Union
sys.stdin = open('sample_input.txt', 'r')


total_case = int(input())
for total in range(1, total_case + 1):  # 1 2 3
    total_num, sta_num = map(int, input().split())  # 10 3
    max_value = sum
    min_value = 0
    num_list = list(map(int, input().split()))  # 숫자 열 개
    for i in range(n-m+1):
        sum = 0
        for j in range(i, i+m):
            sum += v[j]
        if max_value < sum: max_value = sum
        if min_value > sum: min_value = sum
        result = max_value - min_value

        print('#{0} {1}'.format(total, max_value-result))

# 숫자 카운트해서 리스트 만들기
# [0 1 2 3 4 5]
# [0 1 4 2 1 0]
# [0 0 5 3 0 0]
# 뒤에 한 개씩 접근하고 앞에 한 개 지우기(빠르게) // 행렬접근에서도 가능
