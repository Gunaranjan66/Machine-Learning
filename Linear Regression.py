import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def forward(x,w,b):
    return x*w+b
def cost(y,ycap):
    return (1/(2*len(y)))*np.sum(np.power(y-ycap,2))
def der(x,y,w,b,alpha):
    out=forward(x,w,b)
    t=out-y
    w-=alpha*(1/len(y))*np.sum(t*x)
    b-=alpha*(1/len(y))*np.sum(t)
    return w,b
if __name__=='__main__':
    data=pd.read_csv("ex1data1.csv")
    x=np.array(data['6.1101']);
    y=np.array(data['17.592'])
    w=np.random.randn(1)*10
    b=np.random.rand(1)*10
    print("Initial cost :",cost(x,forward(x,w,b)))
    for i in range(100):
        w,b=der(x,y,w,b,0.001)
    print("Final cost :",cost(x,forward(x,w,b)))
    print("Weight :",w,"\nBias :",b)
    plt.plot(x,forward(x,w,b),'r')
    plt.scatter(x,y)
    plt.show()
    
