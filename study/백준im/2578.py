from pprint import pprint
import sys
sys.stdin = open('2578.txt','r')

def check(k):
    for x in range(5):
        for y in range(5):
            if big[x][y] == k:
                big[x][y] = 0

def cnt_bingo(j):
    cnt = 0
    # 세로 빙고
    for x in range(5):
        
        for y in range(5):
            if big[y][x] == 0:
                cnt += 1

    # 가로 빙고
    # 대각선 빙고
    if big[0][0] == 0 and big[1][1] == 0 and big[2][2] == 0 and big[3][3] == 0 and big[4][4] == 0: cnt += 1
    if big[0][4] == 0 and big[1][3] == 0 and big[2][2] == 0 and big[3][1] == 0 and big[4][0] == 0: cnt += 1


    
    return cnt


big = []  # 빙고 리스트
for i in range(5):
    a = list(map(int, input().split()))
    big.append(a)

num = []  # 부르는 수 리스트
for i in range(5):
    num_list = list(map(int, input().split()))
    for j in num_list:
        num.append(j)






pprint(big)
