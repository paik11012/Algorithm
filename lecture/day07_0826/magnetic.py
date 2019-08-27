box = [[1, 0, 2, 0, 1, 0, 1],
       [0, 2, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 2, 2],
       [0, 0, 0, 0, 0, 1, 0],
       [0, 0, 2, 1, 0, 2, 1],
       [0 ,0 ,1, 2, 2, 0, 2]]


stack = []
tot_cnt = 0
for i in range(7):
    cnt = 0  # 줄이 바뀔때마다 cnt = 0
    stack = []
    for j in range(7):
        if box[j][i] == 1:
            stack.append(1)
        elif box[j][i] == 2:
            if len(stack) == 0:  # 짝이 안 맞게 2만 들어오면
                stack.append(2)
                break
            elif stack[-1] == 1:
                stack.pop()
        else: continue  # 0이면 무시
        if not stack:  # 스택이 비었으면 cnt에 1을 추가하라
            cnt += 1
    tot_cnt += cnt  #줄이 끝날 때마다 cnt를 tot_cnt에 추가하라
print(tot_cnt)
