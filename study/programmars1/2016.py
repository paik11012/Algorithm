def solution(a, b):
    weekday = ["THU","FRI","SAT","SUN","MON","TUE","WED"] # 나머지가 0부터 시작하므로
    month=[31,29,31,30,31,30,31,31,30,31,30,31] 
    days = 0
    for i in range(a-1):
        days += month[i]
    result = days + b
    answer = weekday[result % 7]
    return answer

print(solution(1,1))