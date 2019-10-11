from pprint import pprint
import sys
sys.stdin = open('2117.txt', 'r')


def out_idx(xx, yy):
    if xx < 0 or xx >= city: return True
    if yy < 0 or yy >= city: return True
    else: return False


def brute_force(x, y, cnt):
    global pay
    
    pass


city, pay = map(int, input().split())
box = []
for _ in range(city):
    box.append(list(map(int, input().split())))
for i in range(city):
    for j in range(city):
        if box[i][j] == 1:
            brute_force(i, j, 0)

