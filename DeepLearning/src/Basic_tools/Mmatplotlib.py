import numpy as np
import matplotlib.pyplot as plt

# for figure
from matplotlib.image import imread

x = np.arange(0, 6, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plot
plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, linestyle="--", label="cos")

# label
plt.xlabel("x")
plt.ylabel("y")

# title
plt.title("sin & cos")
plt.legend()  # 说明、图例
plt.show()

# display a figure
img_path = r"D:\Document\DeepLearningFromScratch\dataset\lena.png"

img = imread(img_path)
plt.imshow(img)
plt.show()

