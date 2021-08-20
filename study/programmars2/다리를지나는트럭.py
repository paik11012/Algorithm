'''대기하는 차량이 있다면 진입 여부를 확인
진입 가능하면 진입, 진입하면 1칸씩 이동
더 진입 가능하면 진입하고 아니면 기다리기'''

def solution(bridge_length, weight, truck_weights):  # truck weight 처리
    answer = 0
    bridge_on = [0] * bridge_length
    now_weight = 0
    while truck_weights:
        answer += 1  # 우선 1초
        bridge_out = bridge_on.pop(0)  # 나갈것 = 다리에 올라간것 중 앞에 것
        now_weight -= bridge_out  # 나가는 차 무게 빼기
        if now_weight + truck_weights[0] <= weight :  # 차를 올릴 수 있다면
            truck = truck_weights.pop(0)  # 올릴 트럭 무게
            bridge_on.append(truck)
            now_weight += truck
        else: # 못 올리면 빈것 넣기
            bridge_on.append(0)
    # print(bridge_on, answer)
    while now_weight > 0:  # 도로에 남은것 처리
        answer += 1
        print(bridge_on)
        bridge_out = bridge_on.pop(0)
        now_weight -= bridge_out
    return answer

print(solution(2, 10, [7,4,5,6]))