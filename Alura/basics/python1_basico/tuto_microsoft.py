import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 20, 100) #create a list of evenly-spaced numbers over the range.
plt.plot (x, np.sin(x))
plt.show()


msg = "bem vindo ao jogo de adivinhação!"
print(msg)
