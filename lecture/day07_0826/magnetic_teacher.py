import sys
sys.stdin = open('mag.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    box = []
    for _ in range(n):
        line = list(map(int,input().split()))
        box.append(line)
    my_count = 0
    # 세로방향 검색
    for i in range(n):
        meet = False  # 초기 값 false로
        for j in range(n):
            if box[j][i] == 1:
                meet = True
            elif box[j][i] == 2 and meet == True:  # 앞에 1이 있고 2가 나오면 1씩 더해준다
                my_count += 1
                meet = False  # 다시 초기화
    print('#{} {}'.format(tc, my_count))