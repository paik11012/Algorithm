import sys
sys.stdin = open('1253.txt','r')

n = int(input())
box = []
for _ in range(8):
    box.append(list(str(input())))
print(box)