import numpy as np
import sys
sys.path.append('..')


import torch
import torch.nn as nn
from ml.dataset import generate_dataset

class IKNeuralNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model=nn.Sequential(
            nn.Linear(3,128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64,3)
        )

    def forward(self,x):
        return self.model(x)
    