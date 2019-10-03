import timeit
start = timeit.default_timer()

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return fibo(n-1) + n

print(fibo(100))
stop = timeit.default_timer()
print(stop - start)   #  0.00023675176577358638

def fiboo(n):
    

