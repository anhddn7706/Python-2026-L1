import math
import matplotlib.pyplot as plt

x = [i / 100 for i in range(-500, 501)]
y = [2 * value + math.sin(value) ** 2 + 3 for value in x]

plt.plot(x, y)
plt.grid(True)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("po.pdf")
plt.show()