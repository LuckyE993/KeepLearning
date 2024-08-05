import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0


def XOR(x1, x2):
    output1 = NAND(x1, x2)
    output2 = OR(x1, x2)
    y = AND(output1, output2)
    return y


if __name__ == '__main__':
    print("1 AND 1 =" + str(AND(1, 1)))
    print("1 XOR 1 = " + str(XOR(1, 1)))
