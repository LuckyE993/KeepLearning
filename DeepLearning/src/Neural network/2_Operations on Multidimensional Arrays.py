import numpy as np

X = np.array([1, 2])
print("Matrix X is: \n", X)

# The first clone of Matrix W is w11 and w12
# The second clone is w21 and w23
# 3rd is the same.
W = np.array((
    [1, 3, 5],
    [2, 4, 6]
))
print("Matrix W is: \n", W)
Y = np.dot(X, W)

print("Matrix Y = X dot W is; \n", Y)
