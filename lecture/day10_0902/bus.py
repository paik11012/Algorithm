import sys
sys.stdin = open('bus.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    print('#{}'.format(tcc), end = ' ')
    tcnum = int(input())
    empty = [0] * 5001
    for i in range(tcnum):
        a, b = map(int, input().split( ))
        for j in range(a, b+1):  # 1 3, 2 5
            empty[j] += 1
    empty.pop(0)
    busstop = int(input())
    for i in range(busstop):  # 0 1 2 3 4
        aa = int(input())
        print(empty[aa-1], end = ' ')
    print()

