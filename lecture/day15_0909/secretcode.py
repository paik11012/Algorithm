import sys
sys.stdin = open('code.txt','r')
#  “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
tc = int(input())
numbers = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tcc in range(1, tc+1):
    line, n = map(int,input().split())
    for i in range(line):
        one = str(input())
        if '1' in one:
            new = one  # 1이 있는 줄

    last1 = 0  # 마지막 1 위치
    for j in range(len(new)):
        if new[j] == '1':
            if j > last1:
                last1 = j
    data = new[last1+1-56:last1+1]  # 암호만 모인 숫자
    # print(data)
    secret_code = []
    for k in range(8):
        neww = data[k*7:k*7 + 7]
        for kk in range(10):
            if neww == numbers[kk]:
                secret_code.append(int(kk))
    code = 0
    # print(secret_code)
    if ((secret_code[0]+secret_code[2]+secret_code[4]+ secret_code[6])*3 + secret_code[1]+secret_code[3]+secret_code[5]+secret_code[7]) % 10 == 0:
    # print(summ)
        for ii in range(8):
            code += int(secret_code[ii])
    print('#{} {}'.format(tcc,code))

