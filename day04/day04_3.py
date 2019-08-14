# import sys
# sys.stdin = open('3.txt', 'r')

p = 'XYPV'
t = 'EOGGXYPVSY'

sets = set(p)
no_list = list(sets)  # X Y P V

count = 0
pi = 0
ti = 0
while no_list[pi] == t[ti]:
    if no_list[pi] != t[ti]:
        ti = ti + 1
    else:
        count = +1
        pi = +1
print(count)