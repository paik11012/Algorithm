data = 'S01D02H03H04'
#1 12 12 11 13
data = list(data)
criteria = len(data)//3
# print(data)
num = []
for i in range(0,len(data),3):  # 4까지
    num.append(data[i:i+3])

str_list = []  # ['S01', 'D02', 'H03', 'H04']
for i in range(criteria):
    new = (''.join(num[i]))
    str_list.append(new)

if len(set(str_list)) != 4:
    result = 'ERROR'

if
