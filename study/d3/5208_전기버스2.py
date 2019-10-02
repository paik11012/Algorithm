def back(start, cnt):
    global stops
    if start == stops:  # 마지막까지 가면 그만할 것
        return
    else:  # [3, 5, 4, 5]
        end = energies[0]
        for j in range(start, end):
            node = energies[j]  # 현재 위치
            print(node)
            # back(node, cnt + 1)
            # cnt -= 1





energies = [5, 2, 3, 1, 1]
stops = energies.pop(0)
for i in range(1, stops):
    energies[i-1] += i
print(energies)  # 갈 수 있는 길
back(1, 0)