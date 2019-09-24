def bfs(x):
    visited = [False] * (n + 1)
    q = []
    q.append(x)
    visited[x] = True
    while q:
        node = q.pop(0)
        print(node)
        for i in info_list[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n = 5
info_list = [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
bfs(1)


print('--------------------------------')


def dfs(node):
    visitedd[node] = True  # 자기처리
    print(node)
    for i in connected_list[node]:
        if not visitedd[i]:
            dfs(i)


nums = 5  # node가 5개
connected_list = [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
visitedd = [False] * (nums+1)
dfs(1)