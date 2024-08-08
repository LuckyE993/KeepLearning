import pickle
import sys

sys.path.append("../../dataset")
from dataset.mnist import load_mnist

import numpy as np
from PIL import Image


def mean_squared_error(y, t):
    return 0.5 * (np.sum((y - t) ** 2))


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

print(mean_squared_error(np.array(y), np.array(t)))


def cross_entropy_error(y, t):
    delta = 1e-7
    if (y.ndim == 1):
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    batch_size = y.shape[0]
    return -(np.sum(t * np.log(y + delta)))/batch_size


print(cross_entropy_error(np.array(y), np.array(t)))

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, flatten=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
# from 60000 random select 10 pcs
batch_mask = np.random.choice(train_size, batch_size)
print(np.random.choice(train_size, batch_size))

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
