import sys
sys.stdin = open('단조증가.txt', 'r')
tc = int(input())
for tcc in range(1, tc + 1):
    num = int(input())
    n_list = list(map(int, input().split()))
    nn = len(n_list)
    check = 0
    for i in range(nn - 1):  # 2 4 7
        for j in range(nn-1,i,-1):
            multiple = str(n_list[i] * n_list[j])
            for k in range(len(multiple)):
                if len(multiple) > 1:
                    for jari in range(len(multiple)-1):  # 앞뒤 비교할 횟수
                        flag = False
                        if multiple[jari] <= multiple[jari + 1]:  # 앞자리보다 뒷자리가 크다면
                            flag = True
                        else: break
                    if flag == True:
                        if int(multiple) > check:
                            check = int(multiple)
    if check == 0:
        check = -1
    print('#{} {}'.format(tcc, check))  # 한 번이라도 커진 것들 담김
