a, b = 10, 3
data = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
ans = -9999
sum_list = []
for i in range(a-b+1):
    sums = 0
    for j in range(i, i+b): 
        sums += data[j]
    sum_list.append(sums)
# print(sum_list)
print(max(sum_list))
