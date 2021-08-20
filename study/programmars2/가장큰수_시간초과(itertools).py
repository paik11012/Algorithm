import itertools

def solution(numbers):
    big = 0
    mypermuatation =  itertools.permutations(numbers)
    for i in mypermuatation:
        num = int("".join(map(str,list(i))))  # 리스트로 만들어 합치기
        if num > big:
            big = num
    return big


# print(solution([6, 10, 2])) # 6210
print(solution([3, 30, 34, 5, 9]))	#9534330