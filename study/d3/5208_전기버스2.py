def back(num, end, cnt):  # 1 3 0
    global stops, minn
    if cnt > minn:  # 가지치기 조건
        return
    if end >= stops:  # 마지막보다 더 멀리 가면 그만할 것, 기저조건
        if cnt < minn:
            minn = cnt
            # print(minn)
    else:
        for j in range(num, end):  # 1-3
            # j 는 또 새로운 num
            n_num, n_end = new[j-1]
            back(n_num, n_end, cnt + 1)


energies = [10, 2, 1, 3, 2, 2, 5, 4, 2, 1]
stops = energies.pop(0)  # 10
energies.append(0)
for j in range(stops): # 10번 동안
    energies[j] += (j+1)
new = [(i+1, energies[i]) for i in range(stops)]  # 정류장 번호와 그 에너지의 튜플
# [(1, 3), (2, 3), (3, 6), (4, 6), (5, 7), (6, 11), (7, 11), (8, 10), (9, 10), (10, 10)]
a, b = new.pop(0)
minn = 999
back(a, b, 0)
print(minn)
