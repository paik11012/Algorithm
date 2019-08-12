import sys
from typing import Any, Union
sys.stdin = open('GNS1.txt','r')

# dictionary = {"ZRO": '0', "ONE": '1', "TWO": '2', "THR": '3', "FOR": '4', "FIV": '5', "SIX": '6', "SVN": '7', "EGT": '8', "NIN": '9'}

a, num = map(str, input().split())  # #1 7041
numb = int(num)
str_list = input().split()

dictionary = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
for i in str_list:  # svn for zro
    dictionary[i] += 1
print(dictionary)

result = ''
result +=("ZRO " * dictionary['ZRO'])
result +=("ONE " * dictionary['ONE'])
result +=("TWO " * dictionary['TWO'])
result +=("THR " * dictionary['THR'])
result +=("FOR " * dictionary['FOR'])
result +=("FIV " * dictionary['FIV'])
result +=("SIX " * dictionary['SIX'])
result +=("SVN " * dictionary['SVN'])
result +=("EGT " * dictionary['EGT'])
result +=("NIN " * dictionary['NIN'])
print(result)

# for key, value in dictionary.items():
#     print((key + ' ') * value)