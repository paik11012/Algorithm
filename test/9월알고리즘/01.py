import sys
from pprint import pprint
sys.stdin = open('01.txt', 'r')
tc = int(input())
for tcc in range(1, tc+1):
    n = int(input())
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    # pprint(box)
    total = []
    small = []
    minn = 999
    for x in range(n):  # 0
        for y in range(n):  # 0
            comp = []
            for xx in range(n):
                comp.append(box[x][xx])
                comp.append(box[xx][y])
            comp.remove(box[x][y])
            # print(comp)  # 7개 모음
            nums = []
            for i in range(1, 4):
                nums.append(comp.count(i))
            # print(nums)
            small.append(nums[1]+nums[2]*2)  # 1이 기준
            # print(nums[1]+nums[2]*2)
            small.append(nums[0]*1+nums[2]*1) # 2가 기준
            # print(nums[0]*1+nums[2]*1)
            small.append(nums[0]*2+nums[1])  # 3이 기준
            # print(nums[0]*2+nums[1])
    minn = min(small)  # 비용
    for kk in range(len(small)):  # 위치
        if minn == small[kk]:
            total.append(kk % 3 + 1)

    print('#{} {} {}'.format(tcc, minn, min(total)))
# print(minn, min(total))