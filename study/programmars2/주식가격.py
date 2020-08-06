''' 가격이 떨어지지 않은 기간은 몇 초?
숫자 각각을 맨 마지막 자리까지 비교하기
'''

def solution(prices):
    answer = [0 ]* len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else: # 이전 것보다 숫자가 작아지면 떨어지면
                answer[i] = 1
                break
    return answer

prices = [1, 2, 2, 4, 3] # [3, 2, 1, 1, 0]
print(solution(prices))
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]