import pickle
import sys

sys.path.append("../../common")

import numpy as np
from PIL import Image

from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

net = simpleNet()
print(net.W)

x = np.array([0.6,0.9])
t = np.array([0,0,1])
loss = net.loss(x,t)
print(loss)
def f(W):
    return net.loss(x,t)

dW = numerical_gradient(f, net.W)
print(dW)