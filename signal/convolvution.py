#Convolvution 
import numpy as np
def Convolvution(signal,kernel):
    output=np.zeros(len(signal)+len(kernel)-1)
    kernel=np.array(kernel) #list can't broadcast,but array can broadcast
    for i in range(len(signal)):
        output+=np.concatenate((np.zeros(i),signal[i]*kernel,np.zeros(len(signal)-i-1)))
    return output
signal=[1,2,3,4]
kernel=[1,2,3,4]
result=Convolvution(signal,kernel)
print(result)
