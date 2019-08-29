switch = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
# s = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
# str_s = ' '.join(list(map(str, switch)))
mock = len(switch)//10
na = len(switch) % 10  # 나머지
m_list = []
n_list = []
for i in range(mock): # 2번 동안(0 1 2)
    m_list = []
    for j in range(i * 10, i * 10 + 10):
        m_list.append(switch[j])
    print(' '.join(list(map(str, m_list))))

for i in range(mock * 10, mock * 10 + na):
    n_list.append(switch[i])
print(' '.join(list(map(str, n_list))))


