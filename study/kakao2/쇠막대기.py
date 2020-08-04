def solution(brackets):
    answer = 0
    openn = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':  # 여는 괄호면
            openn += 1
        else: # 닫는 괄호면
            if brackets[i-1] == '(':  # 레이저면
                openn -= 1
                answer += openn
            else:  # 닫는게 계속 들어오면
                openn -= 1
                answer +=1  # 삐져나오는 것 처리 제일 중요하다!!!!!!
    return answer
print(solution('()(((()())(())()))(())'))
# print(solution('(((()())(())()))'))
# print(solution('(()()())'))
