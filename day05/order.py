g, t = 9, 9
num_list = [4, 1, 1, 2, 2, 3, 2, 7, 5, 6, 7, 6, 1, 5, 8, 5, 8, 9]
visit = ''
new = [[] for i in range(g)]
for i in range(g):
    new[i].append(num_list[2 * i])
    new[i].append(num_list[2 * i + 1])
# [[4, 1], [1, 2], [2, 3], [2, 7], [5, 6], [7, 6], [1, 5], [8, 5], [8, 9]]
end_list = []  # [1, 2, 3, 7, 6, 6, 5, 5, 9]
for i in range(g):
    end_list.append(new[i][1])

def lonely(list):
    lone = []
    for i in range(g):
        if new[i][0] not in end_list:
            lonely.append(new[i][0])
    return max(lonely)  # 8로 시작

visited = [False] * g
stack = []  # 방문할 곳
path = []
stack.append(lonely(new))  # 1

while stack:
    node = stack.pop()
    if not visited[node]:  # F라면
        visited[node] = True # 자기처리
        path.append(node)
        candidate = []
        for l in range(g):
            if new[l][0] == node:
                candidate.append(new[l][0])
                stack += candidate
print(candidate)
