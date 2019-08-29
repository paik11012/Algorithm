def is_ok(y,x):  # 해당 좌표가 이동 가능한지 여부 체크
    return 0 <= y < n and 0 <= x < n and my_map[y][x] != 1


def find_map(start_y, start_x):  # 재귀함수
    # 1. 종료조건 만들기
    global result
    if my_map[start_y][start_x] == 3:
        result = 1
        return result
    # 2. 반복 검색
    # 3. 네 방향 검색
    # 4. 방문 여부 검색
    visited.append((start_y, start_x))
    
    if is_ok(start_y, start_x+1) and (start_y, start_x+1) not in visited:
        find_map(start_y,start_x+1)  # 오른쪽에 갈 수 있는지 and 안간 좌표이면 우측으로 이동하기
    if result == 0 and is_ok(start_y+1, start_x) and (start_y+1, start_x) not in visited:
        find_map(start_y+1,start_x)  #  하
    if result == 0 and is_ok(start_y, start_x - 1) and (start_y, start_x-1) not in visited:
        find_map(start_y,start_x-1)  # 좌
    if result == 0 and is_ok(start_y-1, start_x) and (start_y-1, start_x) not in visited:
         find_map(start_y-1,start_x)  # 위

n = 5  # 한 변의 길이
my_map = [[1,3,1,0,1],
          [1,0,1,0,1],
          [1,0,1,0,1],
          [1,0,1,0,1],
          [1,0,0,2,1]]
# 시작지점 찾기
start_x = -1
start_y = -1
for y in range(n):
    for x in range(n):
        if my_map[y][x] == 3:
            start_y, start_x = y, x
#  미로에서 항상 필요한 것: 방문했던 위치 저장
visited = []
result = 0  # 목적지 도착 여부 확인
print(find_map(start_y, start_x))
