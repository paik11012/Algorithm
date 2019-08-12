# 10
# 
# 가장 큰 수 뽑고 지우기, 작은 수 뽑고 지우기 / 홀 짝 이용
k = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
N = len(k)
nums = list(k)
print(nums)
def(maxmin):
    min = max = i
    for i in range(i+1, N):
        if i % 2==0:
            for j in range(i+1, N):
                if nums[max] < nums[j]: max=j
            nums[i], nums[max] = nums[max], nums[i]