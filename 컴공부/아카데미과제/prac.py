

total = 'SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA'
num1 = list(total)
slist = []
for i in range(1,len(num1)): # K O R E A K O R E A, S A M S U N G S
    if num1[i] == num1[0]:
        slist.append(i)
print(slist)
