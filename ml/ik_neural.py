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
    
def load_model(path='models/ik_neural.pth'):
        """
        Load a trained IK neural network form disk.

        Args:
            path: path to teh saved model weights
        Returns:
            loaded model ready for inference
        """

        model = IKNeuralNet()
        model.load_state_dict(torch.load(path))
        model.eval()

        input_mean = torch.tensor(np.load('models/input_mean.npy'))
        input_std = torch.tensor(np.load('models/input_std.npy'))
        label_mean = torch.tensor(np.load('models/label_mean.npy'))
        label_std = torch.tensor(np.load('models/label_std.npy'))
        
        return model, input_mean, input_std, label_mean, label_std
   