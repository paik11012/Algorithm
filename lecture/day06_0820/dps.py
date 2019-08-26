num = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]

visited = [False] * 8
stack = []  # 방문할 곳
path = []
stack.append(1)  # 1

while stack:  # stack이 0이 될 때까지
    node = stack.pop()
    if not visited[node]:  # visited의 값이 false라면
        visited[node] = True
        path.append(node)  # 1
        stack += num[node]  # 2 3

result = ''
for i in path:
    result += str(i)
print(result)