number = 100
max_cnt = 0
max_num = []  # 가장 긴 숫자들을 넣을 리스트
for i in range(number+1):
    num1 = number
    num2= i
    num_list = [num1, num2]  # 먼저 처음 두 숫자 넣어놓기
    cnt = 2  # 작은 숫자로 설정
    while True:
        num3 = num1 - num2
        if num3 >= 0:
            num_list.append(num3)
            cnt += 1
            if len(max_num) < len(num_list):  # 가장 긴 숫자 리스트 찾아서 저장하기
                max_num = num_list
            num1 = num2  # 숫자들 
            num2 = num3
        else: break
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)
print(' '.join(list(map(str,max_num))))