num_list = [629, 3497, 7202, 7775, 4325, 3982, 4784, 8417, 2156, 1932]
down = []
for a in range(len(num_list)-1):
    if num_list[a] > num_list[a+1]:
        down.append(num_list[a])
print(down)  # 이 숫자 이후에 작아짐
