import torch
from torch import nn

class Mynn(nn.Module):
	def __init__(self):
		super().__init__()
	def forward(self,input):
		output = input + 1
		return output


mynn = Mynn()
x = torch.tensor(1.0)
output = mynn.forward(x)
print(output)
