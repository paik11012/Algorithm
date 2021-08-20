def solution(n, arr1, arr2):
    r1 = []
    r2 = []
    for i in range(n):
        r = bin(arr1[i])
        r = r[2:]
        if len(r) < n:
            r = '0' * (n-len(r)) + r
        print(r)
        r1.append(r)
    for i in range(n):
        r = bin(arr2[i])
        r = r[2:]
        if len(r) < n:
            r = '0' * (n-len(r)) + r
        r2.append(r)
    board = []
    for j in range(n):
        temp = ''
        for k in range(n):
            if r1[j][k] == '1' or r2[j][k] == '1':
                temp += '#'
            else: temp += ' '
        board.append(temp)
    return board