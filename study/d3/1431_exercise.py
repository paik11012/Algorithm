# 일주일에 L분 이상 U분 이하
minn, maxx, X = 300, 400, 240
# 300 400 350
# 300 400 480
if X < minn:
    result = minn-X
elif X >= minn and X <= maxx:
    result = -0
elif X > maxx:
    result = -1
print(result)