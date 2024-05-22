from torchvision import transforms
from PIL import Image
image_path = r"D:\Document\pytorch-dataset-test\train\ants_image\0013035.jpg"
img_PIL = Image.open(image_path)
print(img_PIL)
img_tensor = transforms.ToTensor()
img_transform = img_tensor(img_PIL)
print(img_transform)


