number = 100
cnt_list = []
for i in range(int(number/2), number):
    cnt = 0
    num1 = number
    num2= i
    num_list = [num1, num2]
    while True:
        num3 = num1 - num2
        if num3 > 0:
            num_list.append(num3)
            cnt += 1
            num1 = num2
            num2 = num3
        else: break
    cnt_list.append(cnt)

my_max = print(max(cnt_list))
`
if (cnt+2) == my_max:
    print(8)
    print(' '.join(map(str,num_list)))

# print('#{} {}'.format(tcc,cnt+2))


