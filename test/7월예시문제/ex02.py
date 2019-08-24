# 파일명 및 함수명을 변경하지 마시오.
# 아래와 같이 수식 문자열이 주어졌을 때, 이를 계산을 해주는 calc 함수를 작성하시오.
# 이 계산기는 덧셈과 뺄셈만 가능하다.
# equation = '-12+12-7979+9191'
# new = equation.replace('-', ' -')
# neww = new.replace('+', ' +')
# newww = neww.split(' ')
# del newww[0]
# k = 0
# for i in newww:
#     k += int(i)
# print(k)


def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    new = equation.replace('-', ' -')
    neww = new.replace('+', ' +')
    newww = neww.split(' ')
    del newww[0]
    k = 0
    for i in newww:
        k += int(i)
    return k






# # # 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))