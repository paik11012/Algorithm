num_list = []
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 2
while True:
    a = 1295
    if len(num_list) == 10:
        print(a * num)
        break
    else:
        b = list(str(a))
        for i in b:  # 1 2 5 9
            if i not in num_list:
                num_list.append(i)
                num += 1

#
# b = list(str(a))
# for i in b:  # 1 2 5 9
#     if i not in num_list:
#         num_list.append(i)
# print(num_list)
# c = a * 2
# b = list(str(c))
# for i in b:  # 1 2 5 9
#     if i not in num_list:
#         num_list.append(i)
# print(num_list)
# d = a * 3
# b = list(str(d))
# for i in b:  # 1 2 5 9
#     if i not in num_list:
#         num_list.append(i)
# print(num_list)
# e = a * 4
# b = list(str(e))
# for i in b:  # 1 2 5 9
#     if i not in num_list:
#         num_list.append(i)
# f = a * 5
# b = list(str(f))
# for i in b:  # 1 2 5 9
#     if i not in num_list:
#         num_list.append(i)
# if len(num_list) == 10:
#     print(f)
#     print(num_list)
