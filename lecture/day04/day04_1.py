# 3
# XYPV
# EOGGXYPVSY

import sys
sys.stdin = open('1.txt', 'r')


def is_same(c,d):
    P = len(c)
    T = len(d)
    pi = 0  # 패턴 인덱스 X
    ti = 0  # 토탈 인덱스 E
    while pi < P and ti < T:
        if t[ti] != p[pi]:  # 서로 0번째 인덱스 비교, 같지 않다면
            ti = ti - pi  # 토탈인덱스를 패턴인덱스 크기만큼 줄인다
            pi = -1  # 패턴인덱스를 하나 앞으로 당긴다 V
        ti = ti+1
        pi = pi+1  # 만약 첫 패턴과 토탈의 글자가 일치한다면 그 뒤에것도 비교해라
    if pi == P:  # 만약 패턴인데스와 패턴이 일치한다면, 검색성공
        return 1
    else: return 0


total = int(input())
for tot in range(1, total+1):  # 0 1 2
    p = input()
    t = input()
    print('#{0} {1}'.format(tot, is_same(p,t)))