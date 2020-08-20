
def solution(numbers):
    big = ''
    zero = 0
    num_list = [] # [(3, 333333333333), (30, 303030303030), (34, 343434343434), (5, 555555555555), (9, 999999999999), (30000, 300003000030)]
    for i in numbers:
        if i == 0:
            zero += 1  # 0 처리하기
        num = str(i) * 12
        int_num = num[:12]
        num_list.append((i,int(int_num)))
    if zero == len(numbers): return 0
    num_list.sort(key=lambda x: x[1], reverse=True)
    for one in num_list:
        big += str(one[0])
    return big


# print(solution([6, 10, 2])) # 6210
# print(solution([3, 30, 34, 5, 9]))	#9534330
print(solution([0,0,0]))	#9534330