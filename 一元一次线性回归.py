import matplotlib.pyplot as plt
import numpy as np
train_x=np.array([235,216,148,35,85,204,45,25,173,191,134,99,117,112,162,272,159,159,69,198])
train_y=np.array([591,539,413,310,308,519,325,332,498,498,392,334,385,387,425,659,400,427,319,522])
mu=train_x.mean()
sigma=train_x.std()
def standardize(x):
    return (x-mu)/sigma
train_z=standardize(train_x)
theta_0=np.random.rand()
theta_1=np.random.rand()
def f(x):
    return theta_0+theta_1*x
def E(x,y):
    return 0.5*np.sum((y-f(x))**2)
eta=1e-4
diff=1
count=0
error=E(train_z,train_y)
while diff>1e-2:
    temp_0=theta_0-eta*np.sum((f(train_z)-train_y))
    temp_1=theta_1-eta*np.sum((f(train_z)-train_y)*train_z)
    theta_0=temp_0
    theta_1=temp_1
    current_error=E(train_z,train_y)
    diff=error-current_error
    error=current_error
    count+=1
    log='第{}次:theta0:{:.3f},theta1:{:.3f},差值={:.4f}'
    print(log.format(count,theta_0,theta_1,diff))
x=np.linspace(-3,3,100)
plt.plot(train_z,train_y,'o')
plt.plot(x,f(x))
plt.show()
