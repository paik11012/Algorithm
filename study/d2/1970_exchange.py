# 50,000 원
# 10,000 원
# 5,000 원
# 1,000 원
# 500 원
# 100 원
# 50 원
# 10 원
# 0 3 0 2 1 3 1 0
import sys
from pprint import pprint
from typing import Any, Union
sys.stdin = open('1970.txt','r')
import math 
import math
total = int(input())
for tot in range(1,total+1):
    print('# {}'.format(tot))
    n = int(input())/10
    up = math.ceil(n) * 10  # 올림이 소숫점밖에 안되기에 10으로 나눈 후 올림하고 10을 곱했음
    print(up)
    if up >= 50000:
        zero = int(up/50000)
        up = up - zero * 50000
        print(zero, end=' ')
    else: print(0, end=' ')
    if up >= 10000:
        one = int(up/10000)
        up = up - one * 10000
        print(one, end=' ')
    else: print(0, end=' ')
    if up >= 5000:
        two = int(up/5000)
        up = up - two * 5000
        print(two, end=' ')
    else: print(0, end=' ')
    if up >= 1000:
        three = int(up/1000)
        up = up - three * 1000
        print(three, end=' ')
    else: print(0, end=' ')
    if up >= 500:
        four = int(up/500)
        up = up - four * 500
        print(four, end=' ')
    else: print(0, end=' ')
    if up >= 100:
        five = int(up/100)
        up = up - five * 100
        print(five, end=' ')
    else: print(0, end=' ')
    if up >= 50:
        six = int(up/50)
        up = up - six * 50
        print(six, end=' ')
    else: print(0, end=' ')
    if up >= 10:
        seven = int(up/10)
        up = up - seven * 10
        print(seven)
    else: print(0)