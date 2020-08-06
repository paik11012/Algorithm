def solution(answers):
    global a, b, c
    temp = [0, 0, 0]
    for i in range(len(answers)): # 숫자
        if a[i%5] == answers[i]:
            temp[0] += 1
        if b[i%8] == answers[i]:
            temp[1] += 1
        if c[i%10] == answers[i]:
            temp[2] += 1
            
    result = []
    maxx = max(temp)
    for j in range(3):
        if maxx == temp[j]:
            result.append(j+1)
    return result

a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
print(solution(answers))