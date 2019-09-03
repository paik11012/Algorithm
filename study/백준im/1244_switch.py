import sys
sys.stdin = open('switch.txt','r')
s_num = int(input())  # 스위치 갯수
switch = list(map(int, input().split()))
case_num = int(input())
for case in range(case_num):
    gen, num = map(int, input().split())
    if gen == 1: ## 남자라면 배수 바꾸기
        change_list1 = []  # 남자가 바꿀 숫자의 인덱스(0부터 시작)
        change_cnt = s_num // num
        for i in range(1, change_cnt+1): # 1부터 몫+1까지
            change_list1.append(num * i - 1)
        for idx1 in change_list1:
            if switch[idx1] == 0: switch[idx1] = 1
            elif switch[idx1] == 1: switch[idx1] = 0
    elif gen == 2:  # 여자라면 가장 큰 회문 찾아서 바꾸기
        idx2 = num - 1  # 기준이 되는 수의 인덱스
        if switch[idx2] == 1:  # 기준점은 무조건 바꾼다
            switch[idx2] = 0
        elif switch[idx2] == 0:
            switch[idx2] = 1

        for i in range(1, len(switch) // 2):  # 17
            out_idx = False
            f_idx = idx2 - i
            e_idx = idx2 + i
            if f_idx < 0 or f_idx > (s_num-1): break
            if e_idx < 0 or e_idx > (s_num-1): break
            if out_idx == False:
                if switch[f_idx] != switch[e_idx]:
                    break  # 이분 중요!!!!! i를 하나씩 늘리면서 바꾸다가 하나라도 앞뒤가 나르면 break 그만 바꿔라
                else:
                    if switch[f_idx] == 0: switch[f_idx] = 1
                    elif switch[f_idx] == 1: switch[f_idx] = 0
                    if switch[e_idx] == 0: switch[e_idx] = 1
                    elif switch[e_idx] == 1: switch[e_idx] = 0

for s in range(len(switch)):
    print(switch[s], end=' ')
    if (s + 1) % 20 == 0:
        print('')

# # 0 0 1 1 1 0 1 1 0 1 1 1 0 1 0 1 0 0 0 1 
# # 1 0 0 0 0 0 0 0 0 1 0 0 1 0 0 