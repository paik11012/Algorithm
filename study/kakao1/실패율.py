def solution(N, stages):
    temp = [0 for _ in range(N+1)]
    for i in stages:
        for j in range(1, i+1):
            if i >= j:
                temp[j-1] += 1
    print(temp[:-1])
    



print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))