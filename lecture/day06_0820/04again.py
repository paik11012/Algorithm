tc = int(input())
for tcc in range(1, tc+1):
    lists = list(str(input()))
    stack = []
    for i in lists:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()

    print('#{} {}'.format(tcc, len(stack)))