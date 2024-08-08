import pickle
import sys

sys.path.append("../../dataset")
from dataset.mnist import load_mnist

import numpy as np
from PIL import Image


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    max = np.max(x)
    exp_x = np.exp(x - max)
    sum_x = np.sum(exp_x)
    Y = exp_x / sum_x
    return Y


def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y


x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
print("Accurary: " + str(float(accuracy_cnt) / len(x)))

for i in range(0, len(x), batch_size):
    x_batch = x[i:i + batch_size]
    y_batch = predict(network, batch_size)

    p = np.argmax(y_batch, axis=1)

    # DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    accuracy_cnt += np.sum(p == t[i:i + batch_size])

print("Batchsize 100 Accurary: " + str(float(accuracy_cnt) / len(x)))
