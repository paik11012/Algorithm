from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    check = deque()
    for j in range(bridge_length):
        check.append(0)
    trucks = deque()
    for i in range(len(truck_weights)):
        trucks.append(truck_weights[i])
    now_weight = 0  # 현재 다리에 올라간 무게 설정
    while trucks:
        answer += 1
        x = check.popleft()  # 나갈것 내보내고
        now_weight -= x  # 나간 만큼 무게 빼기
        if trucks[0] + now_weight > weight:  # 못 들어가면
            check.append(0)
        else:  # 들어가면
            y = trucks.popleft()
            check.append(y)
            now_weight += y  # 들어간 만큼 무게 더하기
    while len(check) != 0:
        answer += 1
        check.popleft()
    return answer

bridge_length=2
weight=10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))