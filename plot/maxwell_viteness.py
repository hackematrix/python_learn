 import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
m=4.3e-26
k=1.38e-23
T=300
v=np.linspace(0,1000,1000)
fv=4*np.pi*(v**2)*((m/(2*np.pi*k*T))**(3/2))*np.exp((-m*(v**2))/(2*k*T))
plt.plot(v,fv)
plt.xlabel("v")
plt.ylabel("f(v)")
plt.title("麦克斯韦速度分布")
plt.grid()
plt.show()
