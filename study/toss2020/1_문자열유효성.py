'''1뒤에는 항상 2
2 뒤에는 1혹은 2 가능'''

def solution(numbers):
    answer = True
    if numbers[-1] == 1: 
        answer = False
        return answer
    for i in range(1,len(numbers)-1):
        if numbers[i] == 1:
            if numbers[i+1] == 2:
                pass
            else: 
                answer = False
                return answer
    return answer

# 1 2 1 경우 맨 뒤 1 뒤에 2가 없으므로 false
numbers = [1, 2]
print(solution(numbers))

