tc = int(input())
for tcc in range(1, tc + 1):
    num = int(input())
    print('#{}'.format(tcc))
    box = [[0] * (i + 1) for i in range(num)]
    box[0][0] = 1
    if num > 1:
        box[1][0], box[1][1] = 1, 1
    for j in range(2, num):  # 2 3 4
        for k in range(1, j):  # 0 1 2
            box[j][k] = box[j - 1][k - 1] + box[j - 1][k]
            box[j][0] = 1
            box[j][-1] = 1
    for i in range(num):  # 0 1 2 3 4
        print(' '.join(list(map(str, box[i]))))
