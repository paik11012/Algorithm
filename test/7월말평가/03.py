# def summary(word):
    # 요약된 문자열을 반환합니다.
a = 'aabbaacc'
b = list(a)  
dif_list = [] # 1 3 5
for i in range(len(b)-1): # 8
    if b[i] != b[i+1]:
        dif_list.append(i)
for i in range(dif_list[i]-1, dif_list[i]):  # 1 3 5
    print(b[i])



# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
# if __name__ == '__main__':
#     print(summary('aabbaacc'))
#     print(summary('ffgggeeeef'))
#     print(summary('abcdefg'))
