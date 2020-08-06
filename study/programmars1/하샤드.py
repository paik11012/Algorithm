'''x가 자릿수의 합으로 나누어떨어져야 함'''
def solution(n):
    num_list = list(str(n))
    summ = 0
    for j in range(len(num_list)):
        summ += int(num_list[j])
    # print(summ)
    if n % summ == 0: 
        return True
    else: return False


print(solution(13))