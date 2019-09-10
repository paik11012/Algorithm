# 16진법을 2진법으로 바로 변환하려면 각 자릿수를 2진법으로 변환하면 된다.
# 예를 들면 25FB16를 0010(2) 0101(5) 1111(F) 1011(B)처럼 끊어서 변환한 다음 전부 붙여주고 앞의 00을 떼준 뒤 100101111110112로 적으면 된다.
import sys
sys.stdin = open('secret.txt','r')
numbers = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
c, r = map(int, input().split())
secret_list = []  #  숫자 모두 들어간 곳
for _ in range(c):
    secret_list.append(str(input()))
last = 0  # 알파벳이 있는 마지막 곳
first = 9999
longest = 0
for i in range(c):
    ii = secret_list[i]
    if '1' in ii or '2' in ii or '3' in ii or '4' in ii or '5' in ii or '6' in ii or '7' in ii or '8' in ii or '9' in ii:
        if '0' in secret_list[i]:
            new = secret_list[i].replace('0','')
            if longest < len(new):
                longest = len(new)
            if longest == len(new):
                one_line = secret_list[i]  # 0이 포함된 가장 긴 줄
first = 9999
last = 0
for j in range(len(one_line)):
    if one_line[j] != '0':
        if first > int(one_line.index(one_line[j])):
            first = int(one_line.index(one_line[j]))
one_last = one_line[first:]
one_last = list(one_last)
while one_last[-1] == '0':  # 리스트로 만들어서 0 없애기
    one_last.pop()
# last = ''.join(list(map(str,one_last)))
# print(one_last)  # 0이 앞뒤에 없는 리스트
big_str = ''
for i in range(len(one_last)):
    n = int(one_last[i], 16)
    nn = '{0:b}'.format(n)
    if len(nn) != 4:
        big_str += ('{}{}'.format((4-len(nn))*'0',nn))
    else: big_str+=nn

data = big_str
print(data)
# secret_code = []
# for k in range(8):
#     newww = data[k*7:k*7 + 7]
#     for kk in range(10):
#         if newww == numbers[kk]:
#             secret_code.append(int(kk))
# print(secret_code)
#
# code = 0
# if ((secret_code[0]+secret_code[2]+secret_code[4]+ secret_code[6])*3 + secret_code[1]+secret_code[3]+secret_code[5]+secret_code[7]) % 10 == 0:
#     # print(summ)
#     for ii in range(8):
#         code += int(secret_code[ii])
#     result = code
# else: result = 0
# print(result)
    # print('#{} {}'.format(code))