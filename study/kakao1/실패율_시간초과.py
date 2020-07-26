def solution(N, stages):
    temp = [0 for _ in range(N)]
    t2 = [0 for _ in range(N)]
    for i in range(len(stages)): # 이중포문을 포문 한 번으로 바꾸기
        for j in range(1, N+1):
            if stages[i] == j:
                temp[j-1] += 1
                t2[j-1] += 1
            if stages[i] > j:
                temp[j-1] += 1
    dic = dict() # 숫자 순서대로 딕셔너리
    for k in range(len(temp)):
        dic[k+1] = t2[k]/temp[k]
    print(dic)
    # .items() 이용해서 key, value를 튜플 형태로 묶기
    tuple_dict = dic.items()
    # lambda 이용해서 정렬 기준(key)을 x[1] = value로 설정 / x[0] = key로 설정
    # reverse=True 오름차순
    result = sorted(tuple_dict, key=lambda x: x[1], reverse=True)
    answer = []
    for a in result:
        answer.append(a[0])
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))