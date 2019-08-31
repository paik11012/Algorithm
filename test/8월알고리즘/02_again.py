import sys
from pprint import pprint
sys.stdin = open('02.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    n, m, k = map(int,input().split())
    box = []  # 숫자가 들어있는 박스
    for _ in range(n):
        box.append(list(map(int, input().split())))

    maax = 0
    for i in range(n-k+1):  # 시작점 잡았음 2
        for j in range(m-k+1):  # 3
            ssum1 = 0
            ssum2 = 0
            for x in range(i, i+k):
                for y in range(j, j+k):
                    ssum1 += box[x][y]
            for x in range(i+1, i+k-1):  # 맨 끝칸 두개 빼고 ssum2에 더해라
                for y in range(j+1, j+k-1):
                    ssum2 += box[x][y]
            gap = ssum1 - ssum2
            if maax < gap:
                maax = gap
    print('#{} {}'.format(tcc,maax))
