import numpy as np
import sys
sys.path.append('..')

import torch
import torch.nn as nn
from ml.dataset import generate_dataset
from ml.ik_neural import IKNeuralNet
import torch.optim as optim

inputs, labels =generate_dataset(50)
inputs = torch.tensor(inputs, dtype=torch.float32)
labels = torch.tensor(labels, dtype=torch.float32)
model = IKNeuralNet()
criterion=nn.MSELoss()
optimizer = optim.Adam(model.parameters(),lr =0.01)

for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs,labels)
    loss.backward()
    optimizer.step()

    if(epoch%100==0):
        print(f"loss:{loss}")