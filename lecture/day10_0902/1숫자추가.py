# import sys
# sys.stdin = open('bus.txt','r')

# N, M, L = 5, 2, 5
# num_list = [1, 2, 3, 4, 5]
# idx1, num1 = 2, 7
# idx2, num2 = 4, 8
#
# list_a = [1,2,3,4,5]

top = [1,2,3]
back = [4,5]

list_b = top
list_b.append(6)
list_b.extend(back)
print(list_b)