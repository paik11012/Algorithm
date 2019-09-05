import sys
sys.stdin = open('2304.txt','r')
n = int(input())
minn = 0
start = 9999  # 데이터가 시작하는 x축 값
maxx_list = []
maxy_list = []
big = []
for i in range(n):
    a = list(map(int, input().split()))
    big.append(a)
# 앞 번호를 기준으로 정리하기
for j in range(len(big)):



#     if b > minn:
#         minn = b
#         maxx_list.append(a)  # 가로
#         maxy_list.append(b)  # 높이
#     if a < start:
#         start = a
# print(maxx_list)
# print(maxy_list)

#for j in max_list:  # [4, 8, 10]


# print(max_list[-1])  # 가장 큰 값