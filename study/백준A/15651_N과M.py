def permutation(idx):
    if idx >= n:
        arr2 = [0] * n
        for j in range(n):
            arr2[j] = str(arr[j])
        print(' '.join(arr2))
    else:
        for i in range(1, m+1):
            arr[idx] = i
            permutation(idx + 1)

m, n = 4, 2
arr = [0] * n
permutation(0)
