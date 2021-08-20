'''어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
이 중 가장 큰 숫자는 94 입니다.
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
순서는 바뀔 수 없다'''

'''
내가 생각한 방법
숫자를 쭉 보면서 가장 작은 수를 k개 제거한다
나머지 숫자를 합친다 
->제거하는 방법은 좋지 않다!!!
작은숫자가 뒤에 있으면 효과가 별로임
대안: 큰 숫자 남기기 기법

'''
def solution(number, k):
    number_list = []
    for n in range(len(number)):  # 숫자로 쪼개기
        number_list.append(int(number[n]))
    # print(number_list)
    for _ in range(k):  # k 번 반복
        delete_candidate = min(number_list)
        print(number_list, 'b')
        number_list.remove(delete_candidate)
        print(number_list)
    # ans = ''
    # for _ in number_list:
    #     ans += str(_)
    # return ans


answer="4177252841"
k=4
# "775841"
print(solution(answer, k))