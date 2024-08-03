import torch
from torch.nn import L1Loss
import torch.nn as nn
input = torch.tensor([1,2,3],dtype=torch.float32)
target = torch.tensor([1, 2, 5], dtype=torch.float32)

input = torch.reshape(input,(1,1,1,3))
target = torch.reshape(target, (1, 1, 1, 3))

loss = L1Loss(reduction='sum')
result = loss(input,target)

print("L1loss: "+str(result))

loss = nn.MSELoss()
result = loss(input,target)
print("MSEloss: "+str(result))

x = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float)
y= torch.tensor([1])
x = torch.reshape(x,(1,3))
loss = nn.CrossEntropyLoss()
result = loss(x,y)
print("CrossEntropyLoss: "+str(result))