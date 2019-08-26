def fac(n):
    result = 1
    if n < 1:
        result = 1
    else:
        result = fac(n-1) * n
    return result

total = int(input())
for tot in range(1, total+1):
    N = int(input())
    n = int(N/10)
    t = int(N//20)
    sums = 0
    for i in range(1, t+1):  # 70 이면 1 2 3
        sums += (2 ** i) * (fac(n-i)/(fac(i) * fac(n-2*i)))
    print('#{} {}'.format(tot, int(sums)+1))



# def strange(num):
#     if num == 10:
#         return 1
#     elif num == 20:
#         return 3
#     return strange(num-20) * 2 + strange(num-10)
#
# total = int(input())
# for tot in range(1, total + 1):
#     n = int(input())  # 너비
#     print('#{} {}'.format(tot, strange(n)))