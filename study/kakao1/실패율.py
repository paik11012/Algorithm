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
            if i == '#':
                num.append(-int(temp))
            # elif i == '*':
    print(num)
   

    # return answer
    



print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))