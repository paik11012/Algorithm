# 시간초과 걸리는 것

def solution(n):
    sosu = [2 for _ in range(n)] # 나와 1 빼고 시작 
    for a in range(2, n+1): # 10인 상황  2 3 4 5 6 7 8 9 10
        count = 0
        for b in range(2, a):
            if a % b == 0:
                sosu[a-1] += 1
    count = 0
    for i in range(1, len(sosu)):
        if sosu[i] == 2:
            count += 1
    return count