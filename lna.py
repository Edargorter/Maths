#!/usr/bin/env python3 

import matplotlib.pyplot as plt

m = 20

inc = 0.0001
n = int(m/inc)

a = [i*inc for i in range(n)]
b = [m - a[i] for i in range(n)]
#b = [i*inc for i in range(n)]
r = [a[i]**b[i] - (b[i]**a[i]) for i in range(n)]

print(a)
print(b)

ax = plt.axes(projection='3d')
ax.set_xlabel("a")
ax.set_ylabel("b")
ax.set_zlabel("a^b - b^a")

plt.plot(a, b)

ax.plot3D(a, b, r)
plt.show()
