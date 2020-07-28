from collections import deque
'''
맨 앞에 있는 문서의 우선순위를 비교하면서
우선순위가 가장 크면 프린트, 아니면 맨 뒤로 보내기
location이 print되면 멈추기
문제 제대로 읽기!
'''
def findMax(q):
    maxx = 0
    for i in range(len(q)):
        if q[i][1] >= maxx:
            maxx = q[i][1]  # 가장 큰 값 maxx에 저장하기
    return maxx

def solution(priorities, location):
    answer = []  
    q = deque()
    for j in range(len(priorities)):
        q.append((j+1, priorities[j]))
    maxx = findMax(q)  # 4
    while q: # 큐가 남아있는 동안 반복해라
        if q[0][1] == maxx:  # 뒤 앞에 있는 수가 max이면
            answer.append(q[0][0])  # 답에 우선 넣기
            q.popleft()
            maxx = findMax(q)  # 다시 max 찾기
        else: # 가장 큰 값이 아니면
            app = q.popleft()
            q.append(app)  # 맨 오른쪽에 넣어라
    for z in range(len(answer)):
        if answer[z] == location+1:
            return z+1


print(solution([2,1,3,2], 2))