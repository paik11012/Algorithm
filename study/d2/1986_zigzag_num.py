tc = int(input())
for tcc in range(1, tc+1):
    num = int(input())
    result = 0
    for i in range(1, num+1): # 1 2 3 4 5
        if i % 2 == 1 :
            result += i
        else:
            result += (-1 * i)
    print('#{} {}'.format(tcc, result))