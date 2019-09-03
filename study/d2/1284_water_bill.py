tc = int(input())
for tcc in range(1, tc+1):
    # A사 : 1리터당 P원의 돈을 내야 한다.
# B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W < R:
        B = Q
    else: B = Q + (W-R) * S
    print('#{} {}'.format(tcc, min(A, B)))
    # print(min(A, B))