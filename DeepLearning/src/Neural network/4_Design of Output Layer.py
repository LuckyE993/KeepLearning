import numpy as np


def original_softmax(x):
    exp_x = np.exp(x)
    sum = np.sum(exp_x)
    y = exp_x / sum
    return y


X = np.array([0.3, 2.9, 4.0])

print(original_softmax(X))


# To solve the problem of overflow when we use exp func
def softmax(x):
    max = np.max(x)
    exp_x = np.exp(x - max)
    sum_x = np.sum(exp_x)
    Y = exp_x / sum_x
    return Y


# if overflow like 1010
input = np.array([1010, 1000, 990])
print(original_softmax(input))

# optimal Method
print(softmax(input))
