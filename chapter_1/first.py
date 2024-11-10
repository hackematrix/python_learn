import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,np.pi,100)
y=1/(1+np.exp(-x));
plt.plot(x,y)
plt.show()
  
