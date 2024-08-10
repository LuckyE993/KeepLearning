import sys

sys.path.append('../../common')
from common import util
import numpy as np

x1 = np.random.rand(1, 3, 7, 7)
col1 = util.im2col(x1, 5, 5, stride=1, pad=0)
print(x1)
print(col1.shape)


class Convolution:
    def __init__(self, W, b, stride=1, padding=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.padding = padding

        self.col = None
        self.col_W = None
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape

        out_h = int((H + 2 * self.padding - FH) / self.stride) + 1
        out_w = int((W + 2 * self.padding - FW) / self.stride) + 1

        col = util.im2col(x, FH, FW)
        col_W = self.W.reshape(FN, -1).T
        out = np.dot(col, col_W) + self.b

        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        self.x = x
        self.col = col
        self.col_W = col_W

        return out

    def backward(self, dout):
        FN, C, FH, FW = self.W.shape
        dout = dout.transpose(0, 2, 3, 1).reshape(-1, FN)

        self.db = dout.reshape(dout, axis=0)
        self.dW = np.dot(self.col_W.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_W.T)
        dx = util.col2im(dcol, self.x.shape, FH, FW, self.stride, self.padding)
        return dx


class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = None
        self.pool_w = None
        self.stride = stride
        self.pad = pad

        self.x = None
        self.arg_max = None
    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int((H - self.pool_h) / self.stride) + 1
        out_w = int((W - self.pool_w) / self.stride) + 1

        col = util.im2col(x, self.pool_h, self.pool_w, stride=self.stride, pad=self.pad)
        col = col.reshape(-1, self.pool_h * self.pool_w)

        out = np.max(col, axis=1)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        return out

    def backward(self, dout):
        dout = dout.transpose(0, 2, 3, 1)

        pool_size = self.pool_h * self.pool_w
        dmax = np.zeros((dout.size, pool_size))
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
        dmax = dmax.reshape(dout.shape + (pool_size,))

        dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
        dx = util.col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)

        return dx




