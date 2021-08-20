import sys
sys.stdin = open('input.txt','r')

totalnum = input()
for ja in range(1,int(totalnum)+1):
    total = input()
    num1 = list(total)
    for i in range(len(num1)): # K O R E A K O R E A, S A M S U N G S
        ilist=''
        if ilist not in total:
            ilist += ''.join(num1[i])  # 스트링 + 리스트
    print(ilist)



    #     if num1[i] == num1[0]: #첫 글자 K랑 겹치는 것 찾기
    #         ilist.append(i)
    # first = ilist[0]  # 5 , 3
    # k = (num1[0:first]) # K O R E A
    # nstring = ''.join(k) # KOREA
    # print(nstring)
    # num = len(nstring)
    # print('#{0} {1}'.format(ja,num))
