import sys
from pprint import pprint
sys.stdin = open('order.txt', 'r')
for num in range(1):
    node, line = map(int, input().split())  #  노드 수, 간선 수
    my_map = [[0] * (node+1) for _ in range(node+1)]
    # 간선 정보
    data = list(map(int, input().split()))  # 2 1 1 3
    input_degree = []
    for i in range(len(data)):
        if i % 2 == 1:
            input_degree.append(data[i])
    id = [0] * (node+1)  # 진입차수의 모음 리스트
    for j in input_degree:
       id[j] += 1
    stack = []
    input_data = [[],[2,5],[3,7],[],[1],[6],[0],[6],[5,9],[]]
    path = []

    # [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]

    for j in range(1, node):
        if id[j] == 0:
            stack.append(j)

    node = stack.pop()
    path.append(node)
    for k in input_data[node]:
        stack.append(k)
        if id[k] > 0:
            id[k] -= 1


    if id[stack[-1]] == 0:
        node = stack.pop()
        path.append(node)
        for k in input_data[node]:
            stack.append(k)
            if id[k] > 0:
                id[k] -= 1

    # if id[node] > 0:
    #     id[node] -= 1
    # for k in input_data[node]:
    #     stack.append(k)
    #
    # print(stack, node)
    # print(id)
    # print(path)
    #
    # node = stack.pop()
    # path.append(node)
    # if id[node] > 0:
    #     id[node] -= 1
    # for k in input_data[node]:
    #     stack.append(k)


    # node = stack.pop()
    # visited[node] = True
    # path.append(node)
    # for k in input_data[node]:
    #     id[k] -= 1
    #     stack.append(k)
    #
    #
    # node = stack.pop()
    # visited[node] = True
    # path.append(node)
    # for k in input_data[node]:
    #     id[k] -= 1
    #     stack.append(k)
    #
    # node = stack.pop()
    # visited[node] = True
    # for k in input_data[node]:
    #     id[k] -= 1
    #     stack.append(k)
    # print(stack)



    # print(visited)

    # path.append(node)
    # print(path)
