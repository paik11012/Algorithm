# a = '((()((((()()((()())((())))))'
# a = '()()((()))'
stack = [0] * 100
top = -1
str = '((()((((()()((()())((())))))'

result = True
for i in range(len(str)): # push
    if str[i] == '(':
        top += 1
        stack[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            result = False
            break
        top -= 1

if top == -1 and result == True:
    print('Correct')
else: print('Wrong')