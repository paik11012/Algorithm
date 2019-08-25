# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )


def my_max(args):
    length = num
    max_value = args[0]
    for i in range(1,length):
        if max_value < args[i]:
            max_value = args[i]
    return max_value


def my_min(args):
    length = num
    min_value = args[0]
    for i in range(1,length):
        if min_value > args[i]:
            min_value = args[i]
    return min_value


case_num = int(input())
for total in range(1,case_num+1):
    num = int(input())
    ai = list(map(int, input().split()))
    result = my_max(ai) - my_min(ai)
    print('#{0} {1}'.format(total, result))
