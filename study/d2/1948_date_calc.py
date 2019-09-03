# 3
m1, d1, m2, d2 = 5, 5, 8, 15
date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2:
    result = d2 - d1 + 1
else:
    datesum1, datesum2 = 0, 0
    for i in range(m2):  # 7월까지 합
        datesum2 += date[i]
    for j in range(m1):
        datesum1 += date[j]  # 4월까지 합
    result = ((datesum2 + d2) - (datesum1 + d1) + 1)
print(result)