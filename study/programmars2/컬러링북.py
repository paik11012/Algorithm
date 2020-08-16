from pprint import pprint

def is_wall(x, y, m, n):
    if x < 0 or x >= m or y < 0 or y >= n:
        return True
    else: return False

def solution(m, n, picture):
    x_dir = [-1, 0, 1, 0] # 좌 상 우 하
    y_dir = [0, 1, 0, -1]
    copied = []  # 0으로 바꿀 것 복사하기
    part = 0  # 영역 갯수
    can = 0  # 가장 큰 영역 수
    for x in range(m):
        temp = []
        for y in range(n):
            temp.append(picture[x][y])
        copied.append(temp)
    for x in range(m):
        for y in range(n):
            now = copied[x][y]
            copied[x][y] = -1  # 갓던 곳은 -1로 바꾸어주기
            for i in range(4): #  네 방향을 보면서 움직일 좌표 찾기
                new_x = x + x_dir[i]
                new_y = y + y_dir[i]
                
                if is_wall(new_x, new_y, m, n) == False and copied[new_x][new_y] != -1:  # 갔던 곳이 아니고 벽이 아니면
                    if copied[new_x][new_y] == now:  # 새로 탐색할 곳이 원래 있던 숫자랑 수가 같으면
                        print(new_x,new_y, '같다')
                        can += 1 #  영역의 수 1 늘리기
            print(can)
            can = 0
            #             copied[new_x][new_y] = -1  # 간 곳은 -1로 바꾸기
            #         else: # 새로운 색이면
            #             part += 1
            #         pprint(copied)
            #     print(can)
            #     can = 0  # 초기화


m = 6	
n = 4	
picture= [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

print(solution(m, n, picture))

'''bfs생각하기
'''