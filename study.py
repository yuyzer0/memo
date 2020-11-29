import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x>0, dtype = np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximun(0, x)

x= np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
y = sigmoid(x)
# y = relu(x)
plt.plot(x, y)
plt.show()

# print(np.__file__)
# print(plt.__file__)