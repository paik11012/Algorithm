import sys
sys.stdin = open('2_1.txt', 'r')


ran, pat = map(int, input().split())  # 10 10
for i in range(pat):
    a = input()
    print(a)

