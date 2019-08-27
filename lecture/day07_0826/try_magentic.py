import sys
sys.stdin = open('mag.txt', 'r')
for tc in range(1, 11):
    n = int(input())
    box = []
    for _ in range(n):
        line = list(map(int,input().split()))
        box.append(line)
    # print(box)
    stack = []
    tot_cnt = 0
    for i in range(n):
        cnt = 0
        stack = []
        for j in range(n):
            if box[j][i] == 0:  # 0이 들어오면 무시
                continue
            elif box[j][i] == 1:  # 1이 들어오면 스택에 넣기
                stack.append(1)
            elif box[j][i] == 2:
                if len(stack) == 0:  # 짝이 안 맞게 2만 들어오면 break
                    stack.append(2)
                    break
                elif stack[-1] == 1:
                    stack.pop()
        if not stack:
            cnt += 1
        tot_cnt += cnt
    print(tot_cnt)




