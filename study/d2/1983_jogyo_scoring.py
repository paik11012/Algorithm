import sys, math
sys.stdin = open('1983.txt','r')

def bub(n):
    for i in range(len(total)-1):
        for j in range(len(total)-1-i):
            if n[j] < n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

tc = int(input())
for tcc in range(1, tc+1):
    abc = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D']
    l, k = map(int, input().split())
    total = []
    for i in range(l):
        a, b, c = map(int, input().split())
        score = a * 0.35 + b * 0.45 + c * 0.2
        total.append(round(score))
    want = total[k-1]
    sort = bub(total)
    want_index = sort.index(want)
    r = want_index / (l / 10)
    print('#{} {}'.format(tcc, abc[math.floor(r)]))