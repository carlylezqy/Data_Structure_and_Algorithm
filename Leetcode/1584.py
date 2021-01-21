points = [[0,0],[1,1],[1,0],[-1,1]]

for i in points:
    for j in points:
        print(abs(i[0] - j[0]) + abs(i[1] - j[1]))