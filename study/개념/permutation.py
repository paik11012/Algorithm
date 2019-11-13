def per(idx):
    global per_list
    if idx >= n:
        arr2 = [0, 0, 0, 0]
        for j in range(4):
            arr2[j] = arr[j]
        per_list.append(arr2)
    else:
        for i in range(4, 0, -1):
            if not visited[i]:
                visited[i] = True
                arr[idx] = i
                # print(arr)
                per(idx + 1)
                visited[i] = False


per_list = []
n = 4
arr = [0] * 4
visited = [False] * 5
per(0)
print(per_list)