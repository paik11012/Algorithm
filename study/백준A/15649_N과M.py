def permutation(idx):
    if idx >= n:
        arr2 = [0] * n
        for j in range(n):
            arr2[j] = str(arr[j])
        print(' '.join(arr2))
    else:
        for i in range(1, m+1):
            if not visited[i]:
                visited[i] = True
                arr[idx] = i
                permutation(idx + 1)
                visited[i] = False

# 123 124 213 214 231 234 312 314 321 324 342 421 423 431 432
# m, n = list(map(int, input().split()))
m, n = 4, 2
arr = [0] * n
visited = [False] * 5
permutation(0)
