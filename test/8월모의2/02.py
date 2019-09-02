import sys
from pprint import pprint
sys.stdin = open('02_t.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    num, size = map(int,input().split())
    # print(num, size)
    box = []
    for _ in range(num):
        box.append(list(map(int, input().split())))
    # pprint(box)
    max_ab = 0
    for x in range(num - size + 1):  # 0 1
        for y in range(num - size + 1):  # 0 1 시작점 잡기
            sum1 = 0
            sum2 = 0
            for a in range(size):  # 0 1 2
                sum1 += box[x + a][y + a]
            for b in range(size):  # 0 1 2
                sum2 += box[x + size - b - 1][y + b]
            ab = abs(sum1 - sum2)
            if ab > max_ab:
                max_ab = ab
    print(tcc, '번 케이스', max_ab)