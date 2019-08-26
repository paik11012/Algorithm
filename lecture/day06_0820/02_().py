import sys
sys.stdin = open('02.txt', 'r')

a = int(input())  # 3
for num in range(1,a+1):
    aa = str(input())
    new = '"' + aa + '"'
    r = ''  # 괄호모음
    for i in new:
        if i == '{' or i =='}' or i =='(' or i ==')':
            r += i
    stack = [] # 미리 빈 스택 만들기
    result = 1
    for i in range(len(r)):
        if r[i] == '(' or r[i] == '{':  # push
            stack.append(r[i])
        elif r[i] == ')' or r[i] == '}':
            # 처음 시작이 )} 이면
            if len(stack) == 0:  # 잘못된 문장
                stack.append(r[i])
                break
                # 짝이 안 맞으면
            elif (r[i] == ')' and stack[-1] != '(') or r[i] == (r[i] == '}' and stack[-1] != '{'):
                stack.append(r[i])
                break
            else:
                stack.pop(-1)
    # 문장검사 종료
    if len(stack) == 0: print('#{} 1'.format(num))
    else: print('#{} 0'.format(num))