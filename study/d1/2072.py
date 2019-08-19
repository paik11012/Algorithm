# 3  #1 200

# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1


def odd_sum(n):
    sums = 0
    for i in n:
        sums += i
    return (sums)


total = input(int())
for a in range(1,total+1):
    num_list = list(map(int,input().split()))
    new = odd_sum(num_list)
    print('#{} {}'.format(a, new))