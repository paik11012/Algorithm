import sys
sys.stdin = open('input.txt','r')  # standard in file, 이 파일을 열겠다, file redirection

def bubble(num):
    for i in range(3, 0, -1):  # 줄이 4개여서 range(3)이용, 3 2 1 0으로 이용하기
        for j in range(0, i):  # 
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num[-1]

# def getMax(idx):
#     tmax = heights[idx - 2]
#     if tmax < heights[idx - 1]: tmax = heights[idx - 1]
#     if tmax < heights[idx + 1]: tmax = heights[idx + 1]
#     if tmax < heights[idx + 2]: tmax = heights[idx + 2]
#     return tmax



for total in range(1,11):  # 데이터가 10번 들어옴
    k = 0
    a = int(input())  # 첫 데이터 줄
    b = list(map(int,input().split( )))  # 두번째 데이터 줄, 데이터를 리스트로 가져오기
    for i in range(2, a-2):
        mymax = bubble([b[i-2],b[i-1],b[i+1],b[i+2]])  # 왼쪽 두개, 오른쪽 두개 줄 중 가장 높은 줄이 mymax
        result = (b[i] - mymax)  # 기준 라인에서 mymax 빼서 그 차 구하기
        if result > 0:
            k += result  # 조망권이 양수인 것 더하기
    print("#{0} {1}".format(total, k))  # 특정 형태로 나타내기
