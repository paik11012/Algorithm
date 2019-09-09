TC = int(input()) #테스트 횟수
for tc in range(1, TC+1):
    data = list(input().split()) #공백기준 나눈 후 리스트로 변환
    stack = []
    errorflag= False
    for i in range(len(data)-1):  # 어차피 마지막은 .이니까 -1
        try:
            if data[i].isdigit() == True:
                stack.append(int(data[i]))
            if data[i].isdigit() == False:
                s = int(stack.pop())
                f = int(stack.pop())
                if data[i] == '+': new = f + s
                elif data[i] == '*': new = f * s
                elif data[i] == '/': new = f // s
                elif data[i] == '-': new = f - s
                stack.append(new)
        except: errorflag = True

    if errorflag == False and len(stack) == 1: print("#%d %d" %(tc,stack[0]))
    elif errorflag == True or len(stack) > 1: print("#%d error" % (tc))
    #연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

