import sys
from typing import Any, Union
sys.stdin = open('1946.txt','r')

num = int(input())

for i in range(num):
    alpha, number = map(str, (input().split()))
    times = int(number)
    if times < 10:
        print(alpha * times)
    elif times == 10:
        print(alpha * times)
    else:
        na = times % 10
        print((times-na) * alpha)
        print(alpha * na)