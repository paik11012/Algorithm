import sys
sys.stdin = open('10158.txt', 'r')


w, h = map(int, input().split())
sx, sy = map(int, input().split())
cnt = int(input())
realx = sx + cnt
realy = sy + cnt
x = realx % w
y = realy % h  # 나머지
mx = realx // w  # 몫
my = realy // h
if mx % 2 == 0:
    rx = x
else: rx = w - x
if my % 2 == 0:
    ry = y
else: ry = h - y
print(rx, ry)
