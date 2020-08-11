'''모든 약수 확인하기
압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return'''

def solution(s):
    answer = 0
    temp = ''
    for i in range(1, len(s)//2+1):
        repeat = s[:i]  #  문자열 압축할 개수
        print(repeat)
    # for dump in yaksu:  # 1 2 4
    #     repeat = s[:dump]  # 반복가능한 문자열
    #     # 만약 이 repeat이 끝까지 반복된다면
    # return answer


# print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('xababcdcdababcdcd'))


# "aabbaccc"	7
# "ababcdcdababcdcd"	9
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	17