import sys
from pprint import pprint
sys.stdin = open('1486.txt', 'r')
# 완전탐색 코드


def dfs(ls, idx):  # ls는 키를 더할 리스트, i는 시작지점
    global mn
    if sum(ls) > s:  # sum과 s의 최소값 저장하기
        if sum(ls) - s < mn:
            mn = sum(ls)-s
        return None # 탈출 조건을 설정해야 함
    for i in range(idx, m):  # idx부터 포문을 돌면서
        ls.append(height[i])
        dfs(ls, idx+1)
        dfs(ls, idx)


m, s = map(int, input().split())  # 5, 16
height = list(map(int, input().split()))
mn = 9999999999999
rs = []
dfs([], 0)
print(mn-s)
