import sys
sys.stdin = open('0_1.txt', 'r')
num = int(input())
new = []  # 100 x 100 행렬
for i in range(100):
    ladder = list(map(int,input().split()))
    new.append(ladder)
if 2 in ladder:
    idx = ladder.index(2)
print(idx)