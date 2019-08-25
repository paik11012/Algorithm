tc = int(input())
for tcc in range(1, tc+1):
    num = list(map(int, input().split()))
    num.remove(min(num))
    num.remove(max(num))
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    ave = sum / len(num)
    print('#{} {}'.format(tcc, round(ave)))
