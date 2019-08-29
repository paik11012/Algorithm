import sys
from pprint import pprint
sys.stdin = open('answer.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N = N + 6
    arr = [['0'] * N for i in range(N)]

    for i in range(3, N - 3):
        s = list(input())
        print(s)
        arr[i][3:N - 3] = s[:]
    #
    # pprint(arr)
