import sys
sys.stdin = open('input_nasa.txt','r')

total = int(input())

for tot in range(1, total + 1):

    n = int(input())
    nasa = list(map(int, input().split()))
    start = nasa[0::2]  # 나사 앞 번호
    end = nasa[1::2]  # 나사 뒷 번호
    num_list = []

    for i in range(len(start)):
        if start[i] not in end:  # 나사의 앞 번호가 뒷번호에 있지 않으면
            idx = i  # 외톨이 앞 나사의 인덱스를 저장해라, 맨 앞에 나올 후보

    num_list.append(start[idx])
    num_list.append(end[idx])  # start point, 현재 각 줄당 2개씩 나온다 [2,3]

    for i in range(len(start)):
        for i in range(len(start)):
            if end[idx] == start[i]:  # 뒤와 앞이 같다면
                idxx = i
                num_list.append(start[idxx])
                num_list.append(end[idxx])
                end[idx] = end[idxx]

    string = ''
    for st in num_list:
        string += str(st)
        string += ' '

    print('#{0} {1}'.format(tot, string))

# 맨 앞 나사는 연결되는 게 없어야 나올 수 있다

