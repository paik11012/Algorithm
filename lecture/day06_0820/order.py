import sys
from pprint import pprint
sys.stdin = open('order.txt', 'r')
# in_degree = [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]

for num in range(1, 11):
    node, line = map(int, input().split())  #  노드 수, 간선 수
    my_map = [[0] * (node+1) for _ in range(node+1)]
    # 간선 정보
    data = list(map(int, input().split()))  # 2 1 1 3
    n = int(len(data)/2)
    for i in range(n):
        start = data[i * 2]  # 짝수  0 2 4 6 8
        end = data[i * 2 + 1] # 홀수  1 3 5 7 9
        my_map[start][end] = 1
    # 도착이 없는 곳이 시작이다

    result = []
    while True:
        if len(result) == node:  # 전체 노드가 경로에 모두 저장되면
            break
        start_col = []
        for col in range(1, node):  # 모든 칼럼을 검색
            if 1 not in my_map[col] and col not in result:  # 작업 경로에 등록이 안 되어있으면 등록하라
                start_col.append(col)

        for col in start_col:
            result.append(col)  # 작업 경로에 등록
            for row in range(len(my_map)):
                my_map[row][col] = 0  # 출발하는 노드로 연결되는 정보 삭제

    print('#{}'.format(num), end = '')
    for i in result:
        print('{}'.format(i), end = '')
    print()




