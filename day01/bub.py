ai = [100, 11111, 2, 1, 21, -200, 49012840]
def mymax(args):
    length = len(args)
    max_value = args[0]
    for i in range(length):
        if max_value < args[i]:
            max_value = args[i]
    return max_value
print(mymax(ai))


