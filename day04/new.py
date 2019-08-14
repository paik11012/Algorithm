a = 'CCBBCCBAABC'
b = list(a)

cnt = 0  # 최대 회문 길이
for x in range(100):
    num = 1
    for z in range(num):  # num이 4니까 2번 비교, 기준
        if a[x] != a[num+z]:  # [0] [1]
            break
        else:
            num = num+1
            cnt = cnt+1