from pprint import pprint
import sys
sys.stdin = open('2563.txt','r')

big = []  # 빙고 리스트
for i in range(5):
    a = list(map(int, input().split()))
    big.append(a)

num = []  # 부르는 수 리스트
for i in range(5):
    num_list = list(map(int, input().split()))
    for j in num_list:
        num.append(j)

k = 0
for x in range(5):
    for y in range(5):
        if big[x][y] == num[k]:
            big[x][y] = 0
            k += 1

pprint(big)