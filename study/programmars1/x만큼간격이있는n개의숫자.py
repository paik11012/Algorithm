def solution(x, n):
    answer = []
    if x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
    elif x == 0:
        answer = [0 for _ in range(n)]
    else:
        for i in range(x, x*n-1, x):
            answer.append(i)
    return answer

# return [i for i in range(x, x*n+1, x)]