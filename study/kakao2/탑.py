def solution(heights):
    answer = []
    for i in range(len(heights)): # 69574 한개씩 보면서
        temp = 0
        for j in range(i+1,1, -1):
            if heights[j-2] > heights[i]: # 왼쪽이 더 크면
                temp = j-1 # 왼쪽 위치를 기록
                break
        answer.append(temp)  # 0이 되더라도 0을 기록
    return answer

# 비슷한데 더 단순
# def solution(heights):
#     h = len(heights)
#     ans = [0] * h
#     for i in range(h-1, 0, -1):
#         for j in range(i-1, -1, -1):
#             if heights[i] < heights[j]:
#                 ans[i] = j+1
#                 break
#     return ans