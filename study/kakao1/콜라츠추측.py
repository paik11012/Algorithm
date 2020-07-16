def solution(n):
    answer = 0
    # n == 1 이 될 때까지 while문을 돌려라
    while True:
        if n == 1: return answer
        elif answer >= 500: return -1
        else:
            if n % 2 == 0:
                n = n//2
                answer += 1
            else: # 홀수면
                n = n * 3 + 1
                answer += 1
        # print(n)
    return answer

print(solution(626331))