import sys
from pprint import pprint
sys.stdin = open('work11.txt','r')
tc = int(input())
for tcc in range(1, tc+1):
    n = int(input())
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    # pprint(box)


def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return

        # 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

print(permutation([1, 2, 3], 3))