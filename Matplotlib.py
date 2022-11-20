
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 16])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.plot([0,0],[15,0])
plt.plot([6,0],[25,15])
plt.plot([12,0],[15,15])
plt.plot([0,0],[15,0])



plt.show()
