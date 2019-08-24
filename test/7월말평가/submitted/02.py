# 파일명 및 함수명을 변경하지 마시오.
def alphabet_count(word):
    """
    아래에 코드를 작성하시오.
    word는 소문자로만 구성되어 있습니다.
    알파벳을 key로, 갯수를 value로 가지는 딕셔너리를 반환합니다.
    """
    a = list(word)
    alpha = []
    for al in a:
        if al not in alpha:
            alpha.append(al)
    diction = {}
    for i in alpha:
        diction[i]=0  # 0이 포함된 딕셔너리 만들기

        for k in a:  # h e l l o 한개씩 반화
            if k == diction'0'  # word내의 스트링이 딕셔너리의 키와 일치한다면
            diction[i] += 1  # 딕셔너리에 value에 1씩 더해라
    return diction



# # 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
