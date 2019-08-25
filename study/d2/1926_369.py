num = 33
for i in range(1,num+1):
    cnt_list = [0]* 3  # 3 6 9 갯수 리스트
    list_num = list(str(i))
    cnt_list[0] = list_num.count('3')
    cnt_list[1] = list_num.count('6')
    cnt_list[2] = list_num.count('9')
    total = cnt_list[0] + cnt_list[1] + cnt_list[2]
    if total != 0:
        print('-' * total, end = ' ')
    else:
        print(i, end = ' ')
