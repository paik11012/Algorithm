중간값 찾기 
n = 10
a_list = [1,9,3,4,5,6,7,8,9,1]
for i in range(n):






# def counting(num_k, ks):
#    c = [0] * num_k
#    ls = [0] * len(ks)
#    for i in ks:
#        c[i] += 1
#    for i in range(0, len(c)-1):
#        c[i+1] += c[i]
#    for i in ks:
#        ls[c[i]-1] = i
#        c[i] -= 1
#    return ls