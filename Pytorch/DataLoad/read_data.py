from torch.utils.data import Dataset
from PIL import Image
import os


class Mydata(Dataset):
	def __init__(self, root_dir, label_dir, transform=None):
		self.root_dir = root_dir
		self.label_dir = label_dir
		self.path_dir = os.path.join(self.root_dir, self.label_dir)
		self.img_path = os.listdir(self.path_dir)

	def __getitem__(self, idx):
		img_name = self.img_path[idx]
		img_idx_path = os.path.join(self.root_dir, self.label_dir, img_name)
		img = Image.open(img_idx_path)
		label = self.label_dir
		return img, label

	def __len__(self):
		return len(self.img_path)


if __name__ == "main":
	root_dir = "DataLoad/dataset/train"
	label_dir = "ants"
	ants_dataset = Mydata(root_dir, label_dir)
