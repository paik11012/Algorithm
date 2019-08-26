num = [[], [2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
visited = [False] * len(num)

path = []  # 가야할 곳
stack = []  # 쌓이는 곳
stack.append(1)

# while stack:  # stack이 빌 때 까지

node = stack(pop)  # 내가 있는 곳 1
if not visited[node]:  # 아직 방문하지 않았다면, false라면
    path.append(path)
    visited[node] = True  # 자기처리
print(path)