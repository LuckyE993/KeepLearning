import pickle
import sys

import numpy as np
from PIL import Image


def func1(x):
    return 0.01 * x ** 2 + 0.1 * x


def func2(x):
    # x[0]**2+x[1]**2
    return np.sum(x ** 2)


def numberical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


print(numberical_diff(func1, 5))


# gradient
def numberical_gradient(f, x):
    h = 1e4
    grad = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val

    return grad


print(numberical_gradient(func2, np.array([3.0, 4.0])))


def gradient_descent(f, init_x, lr=0.01, step=100):
    x = init_x
    for i in range(step):
        grad = numberical_gradient(f, x)
        x -= lr * grad
    return x


init_x = np.array([-3.0, 4.0])
print(gradient_descent(func2, init_x, lr=0.1, step=100))
