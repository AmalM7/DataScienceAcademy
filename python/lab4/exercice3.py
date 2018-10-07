import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x=np.linspace(0, 10*np.pi, 100)
y=np.cos(x)
y2=np.exp(-x/10)*np.cos(x)

plt.plot(x,y, 'r', x, y2, 'g')
plt.title('Cos function and cos with exponentiel')
plt.xlabel('x')
plt.ylabel('y & y2')
plt.show()

