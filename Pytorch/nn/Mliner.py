import torch
from torch import nn
import torchvision
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("../data",train=False,transform=torchvision.transforms.ToTensor(),download=True)

dataloader = DataLoader(dataset,batch_size=64)

class Mynn(nn.Module):
	def __init__(self):
		super().__init__()
		self.linear1 = Linear(196608,10)
	def forward(self,input):
		output = self.linear1(input)
		return output

mynn = Mynn()

for data in dataloader:
	imgs,_ = data
	# input = torch.reshape(imgs,(1,1,1,-1))
	input = torch.flatten(imgs)

	print(input.shape)

	output = mynn(input)
	print(output.shape)

