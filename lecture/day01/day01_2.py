# 5 20 5 K N M /  거리 정류장 충전소
# 4 7 9 14 17
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K

import sys
from typing import Any, Union
sys.stdin = open('sample_input.txt','r')
case_num=int(input())
for total in range(1,case_num+1):
    distance, stop, charge = map(int, input().split()) # 5 20 5
    stop_list=list(map(int, input().split()))
    result = 1
    count = 0  # 총 충전횟수
    num = 0  # 이동거리

    for i in range(charge-1):  # range(4) = 0 1 2 3 4
        if stop_list[i+1] - stop_list[i] > distance:
            result = 0
    while num < stop and result:  # 이동거리가 버스보다 작고 result가 0이 아니면, 둘 다 True면
        for plus in range(distance):  # 0 1 2 3 4
            move = num + distance - plus
            if move in stop_list:  # 4, 7, 9, 14, 17
                num = move
                count = count + 1
                break
            elif move == stop:
                num = move
                break
    result = count
    print('#{0} {1}'.format(total, result))



# for i in range(charge-1):  # range(4) = 0 1 2 3
#     if stop_list[i+1] - stop_list[i] > distance:
#         result = 0
#     else:
#         for plus in range(distance):  # range(5) = 0 1 2 3 4
#             count = 1
#             num = stop_list[0]  # 4
#             if num in stop_list:  # 9 8 7 6 5
#                 num = num + distance - plus
#                 count = count + 1
#         result = count
#     print(result)
