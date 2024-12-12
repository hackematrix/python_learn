import matplotlib.pyplot as plt
import numpy as np
train_x=np.array([235,216,148,35,85,204,45,25,173,191,134,99,117,112,162,272,159,159,69,198])
train_y=np.array([591,539,413,310,308,519,325,332,498,498,392,334,385,387,425,659,400,427,319,522])
mu=train_x.mean()
sigma=train_x.std()
def standardize(x):
    return (x-mu)/sigma
train_z=standardize(train_x)
theta=np.random.rand(3)
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0]),x,x**2]).T
X=to_matrix(train_z)
def f(x):
    return np.dot(x,theta)
def E(x,y):
    return 0.5*np.sum((y-f(x))**2)
diff=1
error=E(X,train_y)
eta=1e-3
while diff>1e-2:
    temp_theta=theta-eta*np.dot(f(X)-train_y,X)
    theta=temp_theta
    current_error=E(X,train_y)
    diff=error-current_error
    error=current_error
x=np.linspace(-3,3,100)
plt.plot(train_z,train_y,'o')
plt.plot(x,f(to_matrix(x)))
plt.show()
