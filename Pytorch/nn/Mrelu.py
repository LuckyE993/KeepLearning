import torch
import torchvision
from torch import nn
from torch.nn import ReLU, Sigmoid
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

input = torch.tensor([
	[1,-0.5],
	[-3,1.5]
])

input = torch.reshape(input,(-1,1,2,2))
print(input.shape)

dataset = torchvision.datasets.CIFAR10("../data",train=False,
                                       transform=torchvision.transforms.ToTensor(),download = True)

dataloader = DataLoader(dataset,batch_size=64)

class Mynn(nn.Module):
	def __init__(self):
		super().__init__()
		self.relu1 = ReLU()
		self.sigmoid1 = Sigmoid()
	def forward(self,input):
		output = self.sigmoid1(input)
		return output

mynn = Mynn()
writer = SummaryWriter("../logs_sigmoid")

# output = mynn(input)
# print(output)
step = 0

for data in dataloader:
	imgs,_ = data
	writer.add_images("input",imgs,step)
	output = mynn(imgs)
	writer.add_images("output",output,step)
	print(step)
	step += 1

