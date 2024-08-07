import sys
sys.path.append("../../dataset")
from dataset.mnist import load_mnist

import numpy as np
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train,t_train),(x_test,t_test) = load_mnist(flatten= True,normalize= False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img_show(img)

img = img.reshape(28,28)
print(img.shape)
img_show(img)


print(x_train.shape)
