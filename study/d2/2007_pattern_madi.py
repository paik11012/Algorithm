# 3
# KOREAKOREAKOREAKOREAKOREAKOREA
# SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
# GALAXYGALAXYGALAXYGALAXYGALAXY
import sys
sys.stdin = open('2007.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    a = str(input())
    result_list = []  # 같은 마디의 길이가 나오는 리스트 'ABCABCABCABC'같은 경우는 369 등등이 들어갔음
    for i in range(len(a)):
        criteria = a[0:i]
        for j in range(1, len(a)):
            madi = ''
            madi += a[j: 2 * j]
            if madi == criteria:
                result_list.append(len(criteria))
                break
    result = result_list[0]  # 그 중 가장 앞에 것 프린트
    print('#{} {}'.format(tcc, result))

 

