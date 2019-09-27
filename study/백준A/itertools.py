import itertools
import sys
sys.stdin = open('2303.txt', 'r')

n = int(input())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))
# print(box)
for i in range(n):
    one = box[i]
    print(list(itertools.combinations(one, 3)))
    print('--------')
    print(list(itertools.permutations(one, 3)))
    print('--------')