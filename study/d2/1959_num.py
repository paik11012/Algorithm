# a, b = 3, 5
# al = [1, 5, 3]
# bl = [3, 6, -7, 5, 4]

a, b = 14, 6
al = [-9, 9, 0, -7, 8, 10, 7, -3, 2, 3, 0, 0, 0, -2]
bl = [8, 1, -9, 3, 0, -7]

sums = 0
num = abs(a-b) + 1
max_num = 0
if a < b:
    for i in range(num):  # 5
        sums = 0
        for j in range(a):  # 11
            sums += al[j] * bl[i+j]
        if sums > max_num:
            max_num = sums
else:
    for i in range(num):  # 5
        sums = 0
        for j in range(b):  # 11
            sums += bl[j] * al[i + j]
            # print(j, i+j)
        if sums > max_num:
            max_num = sums
print(max_num)

#

