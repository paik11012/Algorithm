tc = int(input())
for tcc in range(1, tc+1): 
    print('#{}'.format(tcc))
    num = int(input())
    data = ''
    for i in range(num):
        alpha, number = map(str, (input().split()))
        times = int(number)
        data += alpha * times

    for i in range(len(data)//10): # 3 번 동안 프린트
        print(data[i*10:i*10+10])
    na = len(data)%10
    print(data[-na-1:-1])