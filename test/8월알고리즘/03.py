import sys
from pprint import pprint
sys.stdin = open('033.txt','r')
total = int(input())
for tot in range(1, total+1):
    island_num = 0
    bigmap = []
    size = int(input())
    # 큰 맵 만들기
    for r in range(size):
        line = list(map(int, input().split()))
        bigmap.append(line)


    def is_island(a, b):
        if empty[a][b+1] == 0 and empty[a+1][b-1] == 0 and empty[a+1][b] == 0 and empty[a+1][b+1] == 0:
            return True
        else: return False

    # 방향 바꾸는 함수 우, 우하, 하, 우좌
    dx = [0, 1, 1, 1]
    dy = [1, -1, 0, 1]
    d = 0
    sum = 0
    # 빈 리스트 만들기
    # 0인지 체크하기
    for x in range(size):
        for y in range(size):
            if is_island(x, y):
                sum += 1
                else:  #island가 아니면 방향전환 해라

    print(bigmap)




