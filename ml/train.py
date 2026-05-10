import numpy as np
import sys
sys.path.insert(0, '/Users/riyabaranwal/kinematics-3dof')


import torch
import torch.nn as nn
from ml.dataset import generate_dataset
from ml.ik_neural import IKNeuralNet
import torch.optim as optim

inputs, labels =generate_dataset(10000)
inputs = torch.tensor(inputs, dtype=torch.float32)
labels = torch.tensor(labels, dtype=torch.float32)
model = IKNeuralNet()
criterion=nn.MSELoss()
optimizer = optim.Adam(model.parameters(),lr =0.01)

# Normalize inputs
input_mean = inputs.mean(dim=0)
input_std = inputs.std(dim=0)
inputs = (inputs - input_mean) / input_std

# Normalize labels
label_mean = labels.mean(dim=0)
label_std = labels.std(dim=0)
labels = (labels - label_mean) / label_std

for epoch in range(5000):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs,labels)
    loss.backward()
    optimizer.step()

    if(epoch%100==0):
        print(f"loss at epoch:{epoch}:{loss}")

#test neural IK
test_input_raw = torch.tensor([[1.0, 0.5, 1.5]], dtype=torch.float32)
test_input_normalized = (test_input_raw - input_mean) / input_std
predicted_angles_normalized = model(test_input_normalized)
predicted_angles = predicted_angles_normalized * label_std + label_mean
print('Neural IK Predicted:', predicted_angles.detach().numpy())

#compare with analytic IK
import sys
sys.path.insert(0,'/Users/riyabaranwal/kinematics-3dof')
from kinematics.ik_analytic import inverse_kinematics
t1,t2,t3=inverse_kinematics(1.0,0.5,1,1,1,1.5)
print('Analytic IK:    ',[t1,t2,t3])

from kinematics.fk import forward_kinematics
import numpy as np

# Check neural IK
angles = predicted_angles.detach().numpy()[0]
_, _, _, (x_n, y_n) = forward_kinematics(angles[0], angles[1], angles[2], 1, 1, 1)
print('Neural IK endpoint:  ', round(x_n,3), round(y_n,3))

# Check analytic IK
_, _, _, (x_a, y_a) = forward_kinematics(t1, t2, t3, 1, 1, 1)
print('Analytic IK endpoint:', round(x_a,3), round(y_a,3))
print('Target was:           1.0 0.5')