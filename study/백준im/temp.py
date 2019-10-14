def dfs(i):
    visited[i] = True
    for j in info[i]:
        if not visited[j]:
            # print(visited)
            visited[j] = True
            p.append(j)
            dfs(j)


nums = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
info = [[] for _ in range(8)]
for k in range(len(nums)//2):
    info[nums[2 * k]].append(nums[2*k+1])
    info[nums[2 * k+1]].append(nums[2*k])
print(info)
visited = [False] * 8
p = []
p.append(1)
dfs(1)
print(p)

