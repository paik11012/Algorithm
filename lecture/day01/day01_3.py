# 0~9 n장의 카드
# 가장 많은 카드에 적힌 숫자, 몇 번인지 출력 // 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다. #1 9 2
# 카드 장수 n
import sys
from typing import Any, Union
sys.stdin = open('sample_input.txt','r')


def my_max(c):
    length = len(c)
    max_value = c[0]
    for k in range(length):
        if max_value <= c[k]:  # 부등호가 들어감!
            max_value = c[k]
    return max_value


total_case=int(input())
for total in range(1,total_case+1):
    c = [0] * 10  # [0,0,0,0,0,0,0,0,0,0] 0짜리 10개 생성, 가장 큰 값 구하기 위해
    total_card = int(input())
    card = int(input())
    for i in range(total_card):  # 각 값 갯수 구하기
        c[card % 10] += 1
        card //= 10

        

    for k in range(len(c)):  # index구하기
        if c[k] == my_max(c):
            idx = k

    print('#{0} {1} {2}'.format(total, idx, my_max(c)))  # 최대값이 몇 번 등장하는가

# print(c.index(max(c)), max(c))


