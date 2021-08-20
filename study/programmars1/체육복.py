'''만약 lost주변에 reverse가 있으면 lost에게 나눠줄 것
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이거 고려하기'''

def solution(n, lost, reserve):
    answer = 0
    array = [1] * n  # 우선 모든 애들이 체육복 가져왔다고 가정
    for i in  lost:
        array[i-1] -= 1
    for j in reserve:
        array[j-1] += 1
    for k in range(n):
        if k == 0 : # 맨 앞인 경우
            if array[k] == 0 and array[k+1] == 2: # 내 오른쪽이 2인 경우
                array[k] += 1
                array[k+1] -= 1
        elif k == (n-1): # 맨 마지막인 경우
            if array[k] == 0 and array[k-1] == 2:
                array[k] += 1
                array[k-1] -= 1
        else: # 중간인 경우
            if array[k] == 0 and array[k-1] == 2:
                array[k] += 1
                array[k-1] -= 1
            if array[k] == 0 and array[k+1] == 2:
                array[k] += 1
                array[k+1] -= 1
      
    for l in range(n):
        if array[l] >= 1:
            answer += 1
    return answer

n= 5
lost = [1,3,5]
reserve	=[2,4]
print(solution(n, lost, reserve))