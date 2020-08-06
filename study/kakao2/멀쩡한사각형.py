'''최소공약수 먼저 구해서 패턴 파악하기
멀쩡한 사각형은?
그림그래서 패턴 찾기
w+h-1 만큼 사용한다'''

def solution(w,h):
    minn = min(w, h)
    yaksu = []
    big = 0  # 최대공약수
    for i in range(1, minn):
        if w % (i+1) == 0:
            yaksu.append(i+1)
    for j in range(len(yaksu)-1, -1, -1):  #  제일 큰 수부터 거꾸로 본다
        if h % yaksu[j] == 0:
            big = yaksu[j]
            break
    if  big == 0:  # 약수가 없을 경우 그냥 계산
        answer = w * h - (w + h -1)
        return answer
    else: 
        pattern_w = w//big  # 몇 개 들어가는지 확인
        pattern_h = h//big
        origin = (pattern_w * pattern_h) - (pattern_w + pattern_h - 1)  # 한 패턴 당 멀쩡한 애
        pattern_number = w//pattern_w
        answer = w * h - (pattern_number * pattern_w * pattern_h) + origin * pattern_number
        # 전체 - 패턴넣을 곳 + 멀쩡한 애들
        return answer

print(solution(6,24))