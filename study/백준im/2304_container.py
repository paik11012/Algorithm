import sys
sys.stdin = open('2304.txt','r')
n = int(input())
nums = []
result = 0  # 창고 크기
for _ in range(n):
    nums.append(list(map(int, input().split())))
nums.sort(key=lambda x: x[0])
maxx = 0  # 가장 높은 기둥의 높이
for i in range(len(nums)):
    if nums[i][1] > maxx:
        maxx = nums[i][1]
maxx_num = []  # 가장 높은 기둥의 인덱스!!!, 몇번째 모음
for j in range(len(nums)):
    if nums[j][1] == maxx:
        maxx_num.append((nums[j][0], j))
print(maxx_num)

result += maxx
f_compare = 0
f_list=[]
for f in range(maxx_num[0][1]): # 0 1 2
    if nums[f][1] > f_compare:
        f_compare = nums[f][1]
        f_list.append((nums[f][0], f_compare))
f_list.append((maxx_num[0][0], maxx))  # 계산 편하게 하려고 더하기
print(f_list)
for ff in range(len(f_list)-1):
    result += (f_list[ff+1][1]-f_list[ff][1]) * f_list[ff][1]
print(result)
b_list=[]
b_compare = 0
for b in range(n-1, maxx_num[0][1], -1): # 6 5 4
    if nums[b][1] > b_compare:
        b_compare = nums[b][1]
        b_list.append((nums[b][0], b_compare))
b_list.append((maxx_num[0][0], maxx))
for bb in range(len(b_list)-1):
    result += (b_list[bb][0]-b_list[bb+1][0])*b_list[bb][1]
print(result)