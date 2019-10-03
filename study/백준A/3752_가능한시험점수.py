import sys
from pprint import pprint
sys.stdin = open('3752.txt', 'r')

# 모든 부분집합 구하기 문제 비슷
# 백트래킹으로 짜려고 했으나 모든 경우의 수가 2의 100승이 나오므로 불가능


def sums(idx):
    if idx >= n:
        small_sum = 0
        for j in range(n):
            if arr[j] == 1:
                small_sum += nums[j]
        big_sum.append(small_sum)
    else:
        for k in range(2):  # arr의 숫자가 0 혹은 1 없다
            arr[idx] = k
            sums(idx + 1)


big_sum = []
n = int(input())
arr = [0] * n  # 숫자 01 배열
nums = list(map(int, input().split()))
sums(0)
print(big_sum)
# print(len(set(big_sum)))
