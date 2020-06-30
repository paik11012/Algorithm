''' 가격이 떨어지지 않은 기간은 몇 초?
숫자 각각을 맨 마지막 자리까지 비교하기
/Desktop/git/Algorithm/study/kakao1
'''

def solution(prices):
    answer = [0]* len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: # 뒤에 수가 같거나 크면 계속 더해라
                answer[i] += 1
            else: # 이전 것보다 숫자가 작아지면 떨어지면 거기 까지 더한 수를 반환하라 i > j 일 때
                answer[i] += 1  # 여기가 핵심 숫자가 떨어지더라도 어쨌든 1초 지나게 하고 break할 것
                break
    return answer

prices = [ 1, 2, 3, 2, 3, 1 ]
print(solution(prices))
# [ 5, 4, 1, 2, 1, 0 ] .