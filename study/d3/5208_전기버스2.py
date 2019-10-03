def back(start, cnt):
    global stops
    if start == stops:  # 마지막까지 가면 그만할 것
        return
    else:  # [3, 5, 4, 5, 5]
        end = energies[0]
        for j in range(start, end):  # 1-3
            node = energies[j]  # 현재 위치
            print(node)
            # back(node, cnt + 1)
            # cnt -= 1


energies = [10, 2, 1, 3, 2, 2, 5, 4, 2, 1]
stops = energies.pop(0)
energies.append(stops)
for i in range(1, stops):
    energies[i-1] += i
back(1, 0)10 2 1 3 2 2 5 4 2 1