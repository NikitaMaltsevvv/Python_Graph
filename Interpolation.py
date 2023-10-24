import numpy as np
import matplotlib.pyplot as plt

y1 =lambda x: np.sin(x)
y2=lambda x: np.sin(x) + np.log(x)
y3=lambda x: -0.0045*np.power(x, 4) - 0.081*np.power(x, 3) + 0.10235*np.power(x, 2) + 0.98*x

fig = plt.subplots()

x1 = np.linspace(-6, 0, 100)
x2 = np.linspace(0, 6, 100)
x3 = np.linspace(-6, 6, 100)

plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.grid(True)
    
plt.plot(x1, y1(x1))
plt.plot(x2,y2(x2))
plt.plot(x3, y3(x3))

plt.show()