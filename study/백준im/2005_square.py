a = 64 #int(input()) #map(int, input().split())
new = []
for i in range(1, a):
    if i % 5 == 0:
        new.append(i)
s = new[:10]
y = ''
for i in s:
    y += str(i) + ' '
print(y)