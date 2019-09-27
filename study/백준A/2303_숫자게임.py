import sys
from pprint import pprint
from itertools import combinations

sys.stdin = open('2303.txt', 'r')

n = int(input())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))
# pprint(box)
maxx = [0] * n
for i in range(n):
    ls = box[i]
    one = list(combinations(ls, 3))
    # print(one)
    for ii in range(len(one)):
        result = str(sum(one[ii]))[-1]  # 합의 일의자리 수 구하기
        # print(result)
        if maxx[i] < int(result):
            maxx[i] = int(result)
print(maxx)
m = max(maxx)
print(maxx.index(m)+1)
