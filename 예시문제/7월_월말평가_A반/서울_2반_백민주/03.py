# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """


a = 'aabbaacc'
# 몇 개 있는지 세기
j = 1
for i in range(len(a)-1): # 8
    if a[i] != a[i+1]:
        print(a[i], end = '')
        print(j, end = '')
        j = 1
    else:
        j += 1        

    

    




# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
# if __name__ == '__main__':
#     print(summary('aabbaacc'))
#     print(summary('ffgggeeeef'))
#     print(summary('abcdefg'))
