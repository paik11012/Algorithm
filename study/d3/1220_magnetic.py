import sys
from pprint import pprint
sys.stdin = open('1220.txt','r')
for tcc in range(1, 11):
    box = []
    cnt = 0
    n = int(input())
    for _ in range(n):
        line = list(map(int, input().split()))
        box.append(line)

    for i in range(100):
        flag = False
        for j in range(100):
            if box[j][i] == 1:
                if box[j][i] == 2:
                    flag = True
                    cnt += 1
                    flag = False
            elif flag == 'white' and box[j][i] == 2:
                pass
    print(cnt)