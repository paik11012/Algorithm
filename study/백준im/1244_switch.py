import sys
sys.stdin = open('switch.txt','r')
# 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은
# 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
# 8  스위치 갯수
# 0 1 0 1 0 0 0 1  스위치
# 2  사람 수
# 1 3  성별, 기준점
# 2 3
# 출력 1 0 0 0 1 1 0 1
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
            if f_idx < 0 or f_idx > (s_num+1): out_idx = True
            if e_idx < 0 or e_idx > (s_num+1): out_idx = True
            if out_idx == False and switch[f_idx] == switch[e_idx]:  # 회문이면서 인덱스에서 벗어나지 않는다면
                if switch[f_idx] == 0: switch[f_idx] = 1
                elif switch[f_idx] == 1: switch[f_idx] = 0
                if switch[e_idx] == 0: switch[e_idx] = 1
                elif switch[e_idx] == 1: switch[e_idx] = 0

# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다. 
# 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.
mock = len(switch)//10
na = len(switch) % 10  # 나머지
m_list = []  # 몫 리스트
n_list = []  # 나머지 리스트
for i in range(mock): # 스위치 킬이가 21이면 2번 동안(0 1 2)
    m_list = [] # 몫에 10개만 들어가야 하니 초기화
    for j in range(i * 10, i * 10 + 10): # (0,10) (10,21) 열개씩 뽑기 
        m_list.append(switch[j])
    print(' '.join(list(map(str, m_list))))

for i in range(mock * 10, mock * 10 + na):  # 나머지
    n_list.append(switch[i])
print(' '.join(list(map(str, n_list))))