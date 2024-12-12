import matplotlib.pyplot as plt
import numpy as np
train_x=np.array([[153,432],[220,262],  [118,214], [474,384],[485,411],[233,430],[396,361],[484,349],[429,259],
[286,220],[399,433],[403,340], [252,34],[497,472],[379,416],[76,163],[263,112],[26,193],[61,473],[420,253]])
train_y=np.array([-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,-1,1])
w=np.random.rand(2)
def f(x):
    if np.dot(w,x)>=0:
        return 1
    else:
        return -1
epoch=50
for _ in range(epoch):
    for x,y in zip(train_x,train_y):
        if f(x)!=y:
            w=w+y*x

plt.plot(train_x[train_y==1,0],train_x[train_y==1,1],'o')
plt.plot(train_x[train_y==-1,0],train_x[train_y==-1,1],'x')
x1=np.linspace(0,500)
plt.plot(x1,-w[0]/w[1]*x1,linestyle='dashed')
plt.axis('scaled')
plt.show()
