from math import *
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

# print('achachachachachacha')

x = np.array([1,5,10])
y=np.array([2,10,20])

fig=plt.figure()
plt.plot(x,y,color='blue')
fig.savefig('test.png')
