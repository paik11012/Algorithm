def solution(n):
    answer = ''
    while n >= 1:
        remain = n % 3  # 나머지
        n = n // 3  # 몫
        if remain == 0:
            remain = 4
            n = n - 1 ############### 이부분 ################
        elif remain == 1:
            remain = 1
        elif remain == 2:
            remain = 2
        answer = str(remain) + answer
    return answer
    
# def solution(n):
#     num = ['1','2','4']
#     answer = ""
#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3
#     return answer


print(solution(3))