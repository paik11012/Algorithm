def solution(s):
    words = s.split(' ') # 우선 공백 기준으로 나누기
    answer = ''
    for j in words:
        for i in range(1, len(j)+1):
            if i % 2 == 1: # 홀수
                answer += j[i-1].upper()
            else: # 짝수
                answer += j[i-1].lower()
        answer += ' ' # 단어 끝날 때마다 한 칸 띄우기
    return answer[:-1] # 맨 마지막 공백 없애기