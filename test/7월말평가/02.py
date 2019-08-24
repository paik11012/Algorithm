# 파일명 및 함수명을 변경하지 마시오.
def alphabet_count(word):
    """
    알파벳을 key로, 갯수를 value로 가지는 딕셔너리를 반환합니다.
    """
    new = list(word)
    n_dict = {}  # 빈 딕셔너리 만들기
    for i in range(len(new)):  # 5
        n_dict[new[i]] = 0  # 모두 0인 딕셔너리 만들기
    for i in new:  # 알파벳 한 개씩 가져오기
        if i in new:
            n_dict[i] += 1  # value를 한개씩 올리기
    return n_dict


# # 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
