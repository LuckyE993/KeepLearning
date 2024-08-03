import torch
from torch import nn
from torch.nn import Sequential, Conv2d, MaxPool2d, Flatten, Linear
from torch.utils.tensorboard import SummaryWriter


class Mynn(nn.Module):
	def __init__(self):
		super().__init__()
		self.model1 = Sequential(
			Conv2d(3,32,kernel_size=5,padding=2),
			MaxPool2d(2),
			Conv2d(in_channels=32,out_channels=32,kernel_size=5,padding=2),
			MaxPool2d(2),
			Conv2d(in_channels=32,out_channels=64,kernel_size=5,padding=2),
			MaxPool2d(2),
			Flatten(),
			Linear(1024,64),
			Linear(64,10)
		)
	def forward(self,input):
		output = self.model1(input)
		return output

mynn = Mynn()

input = torch.ones((64,3,32,32))
output = mynn(input)
print(mynn)
print(output.shape)

writer = SummaryWriter("../logs_seq")
writer.add_graph(mynn,input)
writer.close()
