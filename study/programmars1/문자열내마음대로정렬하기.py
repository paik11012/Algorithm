def solution(strings, n):
    # 이중배열 만들어서 하기?, 딕셔너리?? 어떻게 첫번째 문자 같으면 두번째 같으면 세번째 이렇게 처리하지? 재귀함수?
    comp = []
    r = []
    for i in range(len(strings)):
        comp.append(strings[i][n]+strings[i])
    comp.sort()
    for j in comp:
        r.append(j[1:])
    return r
'''
sorted는 비교하기 전에 각 리스트 요소에 대해 호출할 함수를 지정하는 key 매개 변수를 가지고 있습니다.
x[n]이 그 key가 되겠다
https://docs.python.org/ko/3/howto/sorting.html
'''

# def solution(strings, n):
#     return sorted(strings, key=lambda x: x[n])
    # strings를 sort한다 

print(solution(["abce", "abcd", "cdx"],2))
