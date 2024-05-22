from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")

for i in range(100):
	writer.add_scalar("y=x", i, i)

image_path = r"D:\Document\pytorch-dataset-test\train\ants_image\0013035.jpg"
img_PIL = Image.open(image_path)
print(type(img_PIL))
# <class 'PIL.JpegImagePlugin.JpegImageFile'>

# convert PIL format to nparray
img_array = np.array(img_PIL)
print(type(img_array))
# <class 'numpy.ndarray'>

# add to writer,by the way you need to change shape to HWC
# use print(img_array.shape) to see (Height,Weight,Channels)
writer.add_image(tag="test", img_tensor=img_array, global_step=1, dataformats="HWC")

writer.close()
