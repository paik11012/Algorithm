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
    maxx = 0
    for x in range(n):  # 0
        for y in range(n):  # 0
            comp = []
            if box[x][y] > maxx:
                maxx = box[x][y]
            for xx in range(n):
                comp.append(box[x][xx])
                comp.append(box[xx][y])
            comp.remove(box[x][y])
            # print(comp)  # 7개 모음
            nums = []
            for i in range(1, 6):
                nums.append(comp.count(i))
            # print(nums)
            small.append(nums[1]+nums[2]*2+nums[3]*3+nums[4]*4)  # 1 기준
            small.append(nums[0]+nums[2]+nums[3]*2+nums[4]*3)  # 2 기준
            small.append(nums[0]*2+nums[1]+nums[3]*2+nums[4]*3)  # 3 기준
            small.append(nums[0]*3+nums[1]*2+nums[2]+nums[4])  # 4 기준
            small.append(nums[0]*4+nums[1]*3+nums[2]*2+nums[3])  # 5 기준
    print(small)
    minn = min(small)  # 비용
    # print(minn)
    # print(maxx)
    for kk in range(len(small)):  # 위치
        if minn == small[kk]:
            total.append(kk)
    print(total)
    # print('#{} {} {}'.format(tcc, minn, min(total)))
# print(minn, min(total))