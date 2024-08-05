import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    # # method 1
    # # input is a int or float number
    # if x>0:
    #     return 1
    # else:
    #     return 0

    # method 2
    # input is a np array
    y = x > 0
    return y.astype(np.int32)


x = np.arange(-3.0, 3.0, 0.1)
y_step = step_function(x)

plt.plot(x, y_step)
plt.ylim(-0.1, 1.1)
plt.show()


def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))


y_sigmoid = sigmoid_function(x)

plt.plot(x, y_sigmoid)
plt.ylim(-0.1, 1.1)
plt.show()


def ReLU(x):
    return np.maximum(0,x)

y_ReLU = ReLU(x)
plt.plot(x, y_ReLU)
plt.ylim(-0.1, 1.1)
plt.show()


plt.plot(x, y_step, label="step")
plt.plot(x, y_sigmoid, linestyle="--", label="sigmoid")
plt.plot(x, y_ReLU, linestyle="dotted", label="sigmoid")
plt.legend()
plt.show()
