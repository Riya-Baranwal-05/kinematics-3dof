import numpy as np
import torch
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/Users/riyabaranwal/kinematics-3dof')

from kinematics.ik_analytic import inverse_kinematics
from kinematics.fk import forward_kinematics
from ml.ik_neural import load_model

count = 0
n_samples =100
x = []
y = []
phi=[]

model, in_mean, in_std, lb_mean, lb_std = load_model()
analytic_errors = []
neural_errors = []

while count<n_samples:
    x.append(np.random.uniform(-3,3))
    y.append(np.random.uniform(-3,3))
    phi.append(np.random.uniform(-np.pi, np.pi))
    try:
        theta1_f,theta2_f,theta3_f=inverse_kinematics(x=x[count],y=y[count],L1=1,L2=1,L3=1,phi = phi[count])
    except:
        count += 1
        continue
    (_,_),(_,_),(_,_),(x_f,y_f) = forward_kinematics(theta1=theta1_f,theta2=theta2_f,theta3=theta3_f,L1=1,L2=1,L3=1)
    phi_f = theta1_f+theta2_f+theta3_f


    test = torch.tensor([[x[count],y[count],phi[count]]],dtype=torch.float32)
    test_norm = (test-in_mean)/in_std
    pred_norm=model(test_norm)
    pred = pred_norm*lb_std+lb_mean
    angles = pred.detach().numpy()[0]
   
    (_,_),(_,_),(_,_),(x_p,y_p) = forward_kinematics(theta1=angles[0],theta2=angles[1],theta3=angles[2],L1=1,L2=1,L3=1)

    error_a = np.sqrt((x_f-x[count])**2 + (y_f-y[count])**2)
    error_n = np.sqrt((x_p-x[count])**2 + (y_p-y[count])**2)

    analytic_errors.append(error_a)
    neural_errors.append(error_n)
    count+=1



#plot comparison
plt.figure(figsize =(10,5))

plt.subplot(1,2,1)
plt.hist(analytic_errors, bins=20, color='blue', alpha=0.7)
plt.title('Analytic IK Errors')
plt.xlabel('Endpoint Error')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.hist(neural_errors, bins=20, color='red', alpha=0.7)
plt.title('Neural IK Errors')
plt.xlabel('Endpoint Error')

plt.suptitle('Analytic vs Neural IK Endpoint Error Comparison')
plt.tight_layout()
plt.savefig('viz/comparison.png')
plt.show()

print('Analytic IK mean error:', np.mean(analytic_errors))
print('Neural IK mean error:  ', np.mean(neural_errors))