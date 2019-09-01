import sys
sys.stdin = open('rccar.txt', 'r')
total = int(input())
for tot in range(1,total+1):  #1
    num = int(input())  #2
    speed = 0  # 현재 속도
    final = 0  # 이동 거리
    for i in range(num):  # 0
        change= list(map(int, input().split()))  # 데이터가 1개만 들어오는 경우가 있어서 리스트로 받았음
        d = change[0]  # 가속 감속 유지 오더
        if d == 1:  # 가속
            how = change[1]  # 얼만큼 가속할 것인지
            speed += how
            final += speed
        elif d == 2:  # 감속
            how = change[1]
            if how > speed:  # 현재 속도보다 감속할 속도가 더 클 경우, 속도는 0 m/s 가 된다.
                speed = 0
            else:
                speed -= how
                final += speed
        elif d == 0:
            final += speed
        # print(speed, final)
    print('#{0} {1}'.format(tot,final))