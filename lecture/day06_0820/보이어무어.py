#보이어-무어 알고리즘을 구현해보자.
for t in range(int(input())):
    str1,str2 = input().strip(), input().strip()
    lstr1,lstr2 = len(str1), len(str2)
    sid = lstr1-1
    res =0
    while True:
        check = str2[sid]
        pos = str1.rfind(check)
        if sid == lstr2-1:
            if str2[sid-lstr1+1:sid+1] == str1:
                res = 1
            break
        elif pos == lstr1-1:
            if str2[ sid-lstr1+1:sid+1] == str1:
                res = 1
                break
            else:
                sid +=1
        else:
            sid += lstr1-pos-1
            if sid >=lstr2:
                sid = lstr2-1
    print('#{} {}'.format(t+1,res))