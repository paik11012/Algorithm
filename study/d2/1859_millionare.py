import sys
sys.stdin = open('1859.txt','r')
total = int(input())
for tot in range(1, total+1):
    num = int(input())
    num_list = list(map(int,input().split()))
    total_sum = 0
    while len(num_list) > 1:  # num_list길이가 0이되면 끝내라
        mmax = num_list[0]
        for a in num_list: #max 구하는 함수
            if a > mmax:
                mmax = a
        idx = num_list.index(mmax)
        for a in range(idx):  # 최초 max가 있는 인덱스까지
            total_sum += num_list[idx]-num_list[a]
        num_list = num_list[idx+1:]  # 찾은 max 뒤에부터 탐색해라
    print('#{} {}'.format(tot, total_sum))

    # for i in range(idx+1):
    #     del num_list[0]  # 최고 max가 있는 인덱스까지 삭제, 나머지 남기기
    # if len(num_list) == 0 or len(num_list) == 1:  # 맨 마지막이 max이거나 max가 아닌 경우가 있어서 0 or 1로해야 돌아감

