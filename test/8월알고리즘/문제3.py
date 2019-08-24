import sys
sys.stdin = open('033.txt','r')
from pprint import pprint

# DFS 문제 
# 1 재귀를 이용한 풀이

# def check(i,j,num):
#     # i,j 영역이 지도 밖이거나, 이미 방문한 지역이거나, 바다이면
#     # 처리하지 않고 돌려보낸다.
#     if not (0 <= i < n): return False  # 지도 밖 영역
#     if not (0 <= j < n): return False
#     if visited_box[i][j] > 0 : return False  # 방문한 곳
#     if box[i][j] == 0 : return False  # 바다

#     # 섬이 몇 개나 될지 알 수 없으므로 섬의 면적을 저장한 islands는
#     # 동적으로 구성한다. 각 섬에 해당하는 영역을 발견할 때마다 면적 증가
#     # 방문한 것으로 체크(단, 체크는 섬의 번호로 한다.)
#     if num-1 == len(islands):
#         islands.append(0)
#     islands[num-1] += 1
#     visited_box[i][j] = num
#     # 좌상단부터 시계방향으로 8방향을 재귀적으로 체크한다. 
#     dx = [-1,0,1,-1,1,-1,0,1]
#     dy = [-1,-1,-1,0,0,1,1,1]
#     for idx in range(8):  # 다음 방문할 곳 땅인지 체크하기
#         check(i+dx[idx], j+dy[idx],num)
#     return True

# # 테스트케이스 T
# for T in range(int(input())):
#     n = int(input())
#     # 기존에 주어진 지도를 표시하는 box
#     # 방문여부와 각 섬들을 다르게 표시하는 0으로 만들어 진 visited_box 를 선언
#     box = [] 
#     visited_box = [[0]*n for _ in range(n)]
#     for _ in range(n):
#         box.append(list(map(int,input().split())))


#     #num은 몇 번째 섬인지, islands는 각 섬들의 크기를 저장한다.
#     num = 1 
#     islands = [0]
#     # 지도가 n*n의 정사각형 box이므로 각 점마다 돌면서 섬인지를 체크한다.
#     # check 함수는 재귀적으로 구성되어 있다.
#     # 만약 check 함수가 한 번 다 돌고나면 num를 증가시켜서 섬의 번호를 올림.
#     for i in range(n):
#         for j in range(n):
#             if check(i,j, num):
#                 num += 1

#     print('#{} {}'.format(T+1, len(islands)))
# # =================================================

# 2.스택을 이용한 풀이
def checkandprint(i,j,num):
    #방문여부, 지도 밖인지, 원래 지도에서 바다인지만을 체크한다.
    #체크후 여기는 반드시 섬이므로 stack에 넣고 값을 입력한다.
    if not (0 <= i < n): return False
    if not (0 <= j < n): return False
    if visited_box[i][j] > 0 : return False
    if box[i][j] == 0 : return False
    
    stack.append((i,j))  # True이면 stack에 더해라
    visited_box[i][j] = num
    return True


dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
for T in range(int(input())):
    n = int(input())
    # 원 지도와 방문 여부 지도를 작성한다. 
    box = [] 
    visited_box = [[0]*n for _ in range(n)]  # 똑같은 크기의 0으로 만들어진 2차원배열
    for _ in range(n):
        box.append(list(map(int,input().split())))
    # stack 에 앞으로 방문할 영역들을 저장하고, 하나씩 꺼내서 주변을 체크.
    stack = []

    #num은 섬의 번호, islands는 각 섬의 영역 크기를 뜻한다.
    num = 1
    islands = [0]
    for i in range(n):
        for j in range(n):
            # 원지도를 따라 반복하면서, 바다가 아니고, 방문한 적이 없으면 스택에 넣으면서 표시한다.
            if box[i][j] > 0 and visited_box[i][j] == 0:
                stack.append((i,j)) # 방문한 적 없는 곳
                visited_box[i][j] = num
                # 스택이 한 번 끝나서 while이 종료되면 섬 하나가 완성, num을 증가시킨다.
                while stack: # 스택이 0이 될때까지 반복
                    top = stack.pop()
                    # 1과 동일하게 동적 처리 및 영역크기 증가
                    if len(islands) == num-1:
                        islands.append(0)
                    islands[num-1] += 1
                    # 주변 8방향을 좌상단부터 시계방향으로 돌면서 check를 통과하면 stack에 넣는다.
                    for idx in range(8):
                        checkandprint(top[0]+dx[idx], top[1]+dy[idx],num)
                else:
                    num += 1
    print('#{} {}'.format(T+1, len(islands)))
# #========================================================