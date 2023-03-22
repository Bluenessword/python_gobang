import numpy as np

a = np.array([[(7 - max(abs(x - 7), abs(y - 7))) for x in range(15)] for y in range(15)])
count = np.array([[0 for x in range(8)] for i in range(2)])
print(len(count[0]))
print(count[0], count[1])
count = [[[x] for x in range(15)] for y in range(15)]
lx = str(
        [count[i][i - x + y] for i in range(15) if (i - x + y) in range(15)])[1:-1].replace(',', '').replace(' ', '')

pass
