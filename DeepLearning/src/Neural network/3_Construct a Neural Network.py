import numpy as np


def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))


# layer 0(input) to layer 1
X = np.array([1.0, 0.5])
W1 = np.array((
    [0.1, 0.3, 0.5],
    [0.2, 0.4, 0.6]
))
B1 = np.array(([0.1, 0.2, 0.3]))
# dot
A1 = np.dot(X, W1) + B1
# Activate
Z1 = sigmoid_function(A1)

# layer1 to layer2
# Z1 is 1x3 matrix
W2 = np.array((
    [0.1, 0.4],
    [0.2, 0.5],
    [0.3, 0.6]
))
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid_function(A2)


# layer2 to layer3(output)
# Z2 is 1x2
# just differ from Activation Function
def identity_function(x):
    return x


W3 = np.array((
    [0.1, 0.3],
    [0.2, 0.4]
))
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3

Y = identity_function(A3)


# clean code
def init_neural_network():
    network = {}
    network['W1'] = np.array((
        [0.1, 0.3, 0.5],
        [0.2, 0.4, 0.6]
    ))
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array((
        [0.1, 0.4],
        [0.2, 0.5],
        [0.3, 0.6]
    ))
    network['B2'] = np.array([0.1, 0.2])
    network['W3'] = np.array((
        [0.1, 0.3],
        [0.2, 0.4]
    ))
    network['B3'] = np.array([0.1, 0.2])
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['B1'], network['B2'], network['B3']
    Z1 = sigmoid_function(np.dot(x, W1) + B1)
    Z2 = sigmoid_function(np.dot(Z1, W2) + B2)
    Y = identity_function(np.dot(Z2, W3) + B3)
    return Y


network = init_neural_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
