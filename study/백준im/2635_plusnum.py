number = 100
max_cnt = 2
for i in range(int(number/2), number+1):
    num1 = number
    num2= i
    num_list = [num1, num2]
    cnt = 2

    while True:
        num3 = num1 - num2
        if num3 > 0:
            num_list.append(num3)
            cnt += 1
            num1 = num2
            num2 = num3
        else: break
    if len(num_list) == max_cnt: 
        print(num_list)
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)