import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]], dtype=torch.float32)

input = torch.reshape(input, (-1, 1, 5, 5));
print(input.shape)


class Mynn(nn.Module):
	def __init__(self):
		super().__init__()
		self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=True)
		self.maxpool2 = MaxPool2d(kernel_size=3, ceil_mode=False)

	def forward(self, input):
		output = self.maxpool1(input)
		return output


dataset = torchvision.datasets.CIFAR10("../data", train=False, transform=torchvision.transforms.ToTensor()
                                       , download=True)
dataloader = DataLoader(dataset, batch_size=64)

writer = SummaryWriter("../logs_maxpool")

mynn = Mynn()
# output = mynn(input)
# print(output)

step = 0
for data in dataloader:
	imgs, targets = data
	writer.add_images("input", imgs, step)
	output = mynn(imgs)
	writer.add_images("output", output, step)
	print("step: " + str(step))

	step += 1
