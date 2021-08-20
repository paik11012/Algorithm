'''로또 1부터 45까지 6개로 구성, 오름차순 정렬, 중복 없음'''
def solution(numbers):
    answer = True
    lotto = numbers.split(' ')
    nums = []  # 숫자 리스트
    big = 0  # 오름차순 체크
    for _ in lotto:
        one_num = int(_)
        if one_num >= 1 and one_num <= 45:
            if one_num > big:  # 오름차순 확인
                big = one_num
                nums.append(int(_))
            else: answer = False
        else: # 숫자 범위가 안 맞으면
            answer = False
    check_num = set(nums)
    if len(check_num) == 6:  # 갯수 확인
        pass
    else: answer = False
    return answer

print(solution('1 2 3 5 9 122'))