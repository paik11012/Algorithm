def solution(n, m):
    a = []
    b = []
    for i in range(1, n//2+1):
        if n % i == 0:
            a.append(i)
    for j in range(1, m//2+1):
        if m % j == 0:
            b.append(j)
    a.append(n)
    b.append(m)
    r = [] # 공약수 모음
    if len(a) < len(b): # b가 크면
        for k in a:
            if k in b:
                r.append(k)
    else:
        for l in b:
            if l in a:
                r.append(l)
    # 최소공배수 구하기
    ma = m * n // r[-1]       
    return [r[-1], ma]