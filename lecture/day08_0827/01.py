TC = int(input())
for tc in range(1, TC+1):
    data = list(input().split())
    n = len(data) # 반복 횟수
    stack = []
    errorFlag = False  # 예외발생여부
    
    for i in range(n-1): # 연산식 만큼 반복 숫자면 스택에 저장
        try: 
            if data[i].isdigit():
                stack.append(data[i])
            else:  #숫자가 아니면 후위표기법 계산
                num1, num2 = int(stack.pop(),int(stack.pop()))  # 마지막 이전숫자, 연산자, 마지막숫자
                if data[i] == '+': result = num1 + num2
                elif data[i] == '-': result = num1 - num2
                elif data[i] == '*': result = num1 * num2
                elif data[i] == '/': result = num1 // num2
                stack.append(result)  #계산결과를 스택에 저장
        except: errorFlag = True
        #for문 끝
    if errorFlag == False and len(stack)== 1:
        print('#{} {}'.format(tc, result))
    elif errorFlag == True or len(stack) > 1:
        print('#{} error'.format(tc))
