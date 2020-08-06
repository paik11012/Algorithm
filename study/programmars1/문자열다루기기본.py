def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
        for i in range(len(s)):
            if s[i].isalpha() == True:
                answer = False
                break  # 한개라고 알파벳이 있으면 false하고 for문 break
    return answer

# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)
print(solution("a234"))