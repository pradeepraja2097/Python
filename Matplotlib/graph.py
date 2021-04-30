import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 250])
ypoints = np.array([0, 250])


plt.plot(xpoints, ypoints)
plt.show() 

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)

plt.show() 