def solution(prices):
    answer = []
    prices = list(reversed(prices))
    while prices:
        temp = 0
        for i in range(len(prices)-2, -1, -1):  # 3210
            if prices[-1] <= prices[i]:  # 떨어지지 않았으면
                temp += 1
            else:  # 떨어졌으면
                temp += 1
                break
        answer.append(temp)
        prices.pop()  # pop(0)은 오래걸리니까 웬만하면 쓰지 말것
    return answer

print(solution([1,2,3,2,3]))