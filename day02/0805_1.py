

def my_max(z):
    max_value = total_list[0]
    for i in total_list:
        if i > max_value:
            max_value = i
    return max_value


test_num = 1
for t in range(1, test_num+1):
    case_num = input(int())  # 1 2 3 4 5 6 7 8 9 10
    num_list = []
    for row in range(100):
        num_list1 = list(map(int, input().split()))  # 100개가 들어간 한 리스트(행), 100개 가져와야 함(열)
        num_list.append(num_list1)

    sum_list1 = [0] * 100
    for m in range(len(num_list)): # 0 1 2 3 4 .. 99
        for n in range(len(num_list)): # 0 1 2 3 4 ...99
            sum_list1[m] += num_list[m][n]

    sum_list2 = [0] * 100
    for j in range(len(num_list)):
        for k in range(len(num_list)):
            sum_list2[j] += num_list[k][j]

    sum_list3 = [0]
    for a in range(len(num_list)):
        for b in range(len(num_list)):
            if a == b:
                sum_list3[0] += num_list[a][b]

    sum_list4 = [0]
    for a in range(len(num_list)):
        for b in range(len(num_list)):
            if a + b == 100:
                sum_list4[0] += num_list[a][b]

    total_list = sum_list1 + sum_list2 + sum_list3 + sum_list4
    print('#{0} {1}'.format(case_num, my_max(total_list)))
    print('#')
