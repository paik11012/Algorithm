'''
문자를 앞에서부터 읽으며 점수를 매기다가
*이 나오면 앞에 두 점수에 2를 곱하고
#이 나오면 앞 점수에 -1을 곱한다
'''

def solution(dartResult):
    num = []
    temp = ''
    for i in dartResult:
        if ord(i) >= 48 and ord(i) <= 57: # 숫자면
            temp += i
        else: # 문자면                
            if i == 'S':
                num.append(int(temp))
            elif i == 'D':
                num.append(int(temp) ** 2)
            elif i == 'T':
                num.append(int(temp) ** 3)
            else: # 다른 문자면
                if i == '#':
                    num[-1] = num[-1] * -1
                else: # * 이면
                    num[-1] = num[-1] * 2
                    if len(num) > 1:  # num길이가 1일 수도 있으니 체크
                        num[-2] = num[-2] * 2
            temp = ''
    return sum(num)
   
print(solution("1T2D3D#"))