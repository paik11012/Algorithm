num_list = [[4, 4, 3, 2, 1],
            [2, 2, 1, 6, 5],
            [3, 5, 4, 6, 7],
            [4, 2, 5, 9, 7],
            [8, 1, 9, 5, 6]]


def my_max(z):
    max_value = total_list[0]
    for i in total_list:
        if i > max_value:
            max_value = i
    return max_value


sum_list1 = [0] * 5
for m in range(len(num_list)): # 0 1 2 3 4 행
    for n in range(len(num_list[0])): # 0 1 2 3 4 열
        sum_list1[m] += num_list[m][n]

sum_list2 = [0] * 5
for j in range(len(num_list[0])):
    for k in range(len(num_list)):
        sum_list2[j] += num_list[k][j]

sum_list3 = [0]
for a in range(len(num_list)):
    for b in range(len(num_list[0])):
        if a == b:
            sum_list3[0] += num_list[a][b]

sum_list4 = [0]
for a in range(len(num_list)):
    for b in range(len(num_list[0])):
        if a + b == 4:
            sum_list4[0] += num_list[a][b]

total_list = sum_list1 + sum_list2 + sum_list3 + sum_list4
print(my_max(total_list))

