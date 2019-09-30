import sys
from pprint import pprint
sys.stdin = open('17136.txt', 'r')


def dfs(papers, x, y, cnt):
    big = 0
    if papers[0] < 1 or papers[1] < 1 or papers[2] < 1 or papers[3] < 1 or papers[4] < 1:
        big += cnt
        return big  # 빠져나가는 조건
    for i in range(10):
        for j in range(10):
            if box[i][j] == 1:  # dfs시작
                x = i
                y = j





    # 1장 설정
    if x < n and y < n and visited[x][y] == 0 and box[x][y] == 1:  # 범위 안이고 방문하지 않았으면
        print(x, y)
        visited[x][y] = 1  # visited 표시
        papers[0] -= 1
        # print(x, y)
        dfs(x, y+1, cnt + 1)  # 다음 1로 이동
    # 2장 설정
    if x+1 < n and y+1 < n: # 범위 내라면
        for p in range(2):  # 0 1
            for q in range(2): # 네 칸을 확인하면서
                if box[x+p][y+q] == 1 and visited[x+p][y+q] == 0:
                    visited[x+p][y+q] = 1 # visited 표시
                    papers[1] -= 1
                    dfs(x, y+2, cnt+1)

    # # 3장
    # if x+2 < n and y+2 < n:
    #     for p in range(3):
    #         for q in range(3): # 네 칸을 확인하면서
    #             if box[x+p][y+q] == 1 and visited[x+p][y+q] == 0:
    #                 visited[x+p][y+q] = 1 # visited 표시
    #                 papers[2] -= 1
    #                 dfs(x, y+3, cnt+1)

n = 10
box = []
for _ in range(10):
    box.append(list(map(int, input().split())))
visited = [[0] * 10 for _ in range(10)]
dfs([0, 5, 5, 5, 5, 5], 0, 0, 0)
