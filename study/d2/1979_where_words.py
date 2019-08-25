import sys
from pprint import pprint
sys.stdin = open('1979.txt','r')
# total = int(input()) # 10
# for num in range(1, total+1):
n, k = map(int, input().split())  # n 행렬크기 k 문자열 길이
box = []
for _ in range(n):
    temp = ''
    line = list(map(int, input().split()))
    for i in line:
        temp += str(i)
    print(temp)
    if '111' in temp:
        print(1)
    else:
        print(0)





    # total = 0
    # for i in range(n): # 0 1 2 3 4 행
    #     if num_list[i].count(1) == k and num_list[i].count(0) == (n-k):
    #         for j in range(n-k+1): # 012 #123 #234
    #             if num_list[i][j] == 1: #1이 연속 k번 반복된다면
    #                 total += 1
    # colunm_list = []
    # for a in range(n): # 0 1 2 3 4 열
    #     for b in range(n): # 0 1 2 3 4 열
    #         colunm_list.append(num_list[b][a])  
    # # print(colunm_list)
    # # (0,5) (5,10) (10,14) (15,19) (20,24) (25,29)
    # a = []  # 새로운 열 행렬 만들기!!! 드디어 끝
    # for k in range(n): # 30 / 5 = 6 -> 0 1 2 3 4 5
    #     new = colunm_list[k*5:k*5+5] # 행렬 5개 만들기
    #     a.append(new)
    # # print(a) 
    # for i in range(n): # 0 1 2 3 4 행
    #     if a[i].count(1) == k and a[i].count(0) == (n-k):
    #         for j in range(n-k+1): # 0 1 2
    #             if a[i][j] == 1 and a[i][j+1] == 1 and a[i][j+2] == 1:
    #                 total += 1
    # print('#{0} {1}'.format(num,total))