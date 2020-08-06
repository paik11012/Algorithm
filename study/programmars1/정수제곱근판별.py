def solution(n):
    answer = 0
    answer = n ** (1/2)
    remainder = answer % 1
    if remainder == 0:
        return (answer+1) ** 2
    else: return -1