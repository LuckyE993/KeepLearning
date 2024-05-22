import cv2
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
image_path = r"D:\Document\pytorch-dataset-test\train\ants_image\0013035.jpg"
cv_img = cv2.imread(image_path)

writer = SummaryWriter("logs")
writer.add_image(tag="test_ndarray",img_tensor=cv_img,global_step=1,dataformats='HWC')

totensor = transforms.ToTensor()
img_tensor = totensor(cv_img)

writer.add_image(tag="test_tensor",img_tensor=img_tensor,global_step=1)
writer.close()