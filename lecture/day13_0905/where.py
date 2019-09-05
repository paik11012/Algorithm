tc = int(input())
for tcc in range(1, tc+1):
    n, t = map(int, input().split())
    cnt = 0
    big = []
    for i in range(n):
        box = input().split()
        new = ''
        for j in box:
            new += j
        new = new.split('0')
        for k in new:
            if k == '1' * t:
                cnt += 1
        big.append(box)
    # print(cnt)
    newbig = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            newbig[x][y] = big[y][x]
    for z in range(n):
        line = ''
        for zz in newbig[z]:
            line += zz
        line = line.split('0')
        for line1 in line:
            if line1 == '1'*t :
                cnt += 1
    print('#{} {}'.format(tcc, cnt))
