import sys, math
sys.stdin = open('1204.txt','r')

tc = int(input())
for tcc in range(1, tc+1):
    tccc = int(input())
    i = list(map(int, input().split()))
    # print(i)
    num = [0] * 101
    for j in range(len(i)):  # 0부터 i의 갯수까지
        num[i[j]] += 1  # 10
    print(num)
    maxx = max(num)  # 18이 최빈값
    max_list = []
    for i in range(100):  # 단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라
        if num[i] == maxx: # 최빈수랑 같은 것은 모두 max_list에 더하기
            max_list.append(i)
    print('#{} {}'.format(tcc, max_list[-1]))