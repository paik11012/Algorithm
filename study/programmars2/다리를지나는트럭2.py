def solution(bridge_length, weight, truck_weights): 
    answer = 0
    bridge = [0] * bridge_length
    while truck_weights:
        answer += 1  # 우선 시간은 흐른다
        if truck_weights[0] + bridge[-1] <= weight:
            bridge.append(truck_weights[0])  # 우선 추가
            bridge.pop(0)  # 숫자 2개 맞춰주기
            truck_weights.pop(0) # 빼내기
        else:
            bridge.append(0)  # 우선 움직이기
            bridge.pop(0)
        print(bridge)
    while bridge: # 다 빠져나가도록 기다리자
        answer += 1
        bridge.pop(0)
    return answer

print(solution(100, 100, [10, 10, 10]))