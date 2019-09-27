import sys
from pprint import pprint
sys.stdin = open('1486.txt', 'r')

# 백트래킹 코드

def dfs(tall, ls, idx):  # ls는 키를 더할 리스트, i는 시작지점
    global mn
    if tall > s:
        if mn > tall:
            mn = tall
            rs.append(tall)
        return 0 # 탈출 조건을 설정해야 함
    for i in range(idx, m):  # 처음부터 포문을 돌면서
        dfs(tall + height[i], ls+[i], i + 1)
        ls.append(i)
        dfs(tall+height[i],ls, i+1)
        ls.pop()


# 완전탐색 코드
# def dfs(ls, idx):  # ls는 키를 더할 리스트, i는 시작지점
#     if sum(ls) > s:
#         print(sum(ls))
#         return 0 # 탈출 조건을 설정해야 함
#     for i in range(idx, m):  # 처음부터 포문을 돌면서
#         # ls.append(height[i])
#         # dfs(ls, i+1)
#         # ls.pop()
#         dfs(ls+[height[i]], i+1)





m, s = map(int, input().split())  # 5, 16
height = list(map(int, input().split()))
mn = 9999999999999
rs=[]
dfs(0, [], 0)
# dfs([], 0)
print(mn-s)

