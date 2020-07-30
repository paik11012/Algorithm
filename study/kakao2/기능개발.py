from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            days.append((100-progresses[i])//speeds[i])
        else: days.append(((100-progresses[i])//speeds[i])+1)
    answer.append(1)  # 우선 1 넣고 시작
    compare = days[0]
    for j in range(len(days)-1):
        if compare >= days[j+1]:
            answer[-1] += 1
        else:
            compare = days[j+1]  # 7
            answer.append(1)
    return answer

print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))