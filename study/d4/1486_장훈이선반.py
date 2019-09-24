import sys
from pprint import pprint
sys.stdin = open('1486.txt', 'r')

tc = int(input())
for tcc in range(tc):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    print(b)
    print(height)