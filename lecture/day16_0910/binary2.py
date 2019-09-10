import sys
sys.stdin = open('bi2.txt','r')


tc = int(input())
for tcc in range(1, tc+1):
    strr = ''
    a = float(input())
    while a != 0:
        a = a * 2
        strr += str(int(divmod(a, 1)[0]))
        a = divmod(a, 1)[1]
        if len(strr) > 12:
            strr = 'overflow'
            break
    print('#{} {}'.format(tcc, strr))





