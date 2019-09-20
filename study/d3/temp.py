def bfs(node):
    q = []
    q.append(node)
    visited[node] = True
    while q:
        node = q.pop()
        print(node)
        for i in connected_list[node]:
            if visited[i] == False:
                q.append(i)

num = 5  # node가 5개
connected_list = [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
visited = [False] * (num + 1)
bfs(1)