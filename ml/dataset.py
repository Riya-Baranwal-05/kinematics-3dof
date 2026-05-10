import numpy as np
import sys
sys.path.append('..')
from kinematics.fk import forward_kinematics

def generate_dataset(n_samples):
    """
    This computes samples for the finding end effector position and orientation.
    This calls forward kinematics with random values of thetas and returns x,y and phi
    """

    theta1 = np.random.uniform(-np.pi,np.pi,n_samples)
    theta2 = np.random.uniform(-np.pi,np.pi,n_samples)
    theta3 = np.random.uniform(-np.pi,np.pi,n_samples)
    inputs=[]
    output =[]

    for i in range(n_samples):
        phi=theta1[i]+theta2[i]+theta3[i]

        (_,_),(_,_),(_,_),(x,y)=forward_kinematics(theta1=theta1[i],theta2=theta2[i],theta3=theta3[i],L1=1,L2=1,L3=1)
        inputs.append((x,y,phi))
        output.append((theta1[i],theta2[i],theta3[i]))
 
    inputs =np.array(inputs)
    output = np.array(output)

    return inputs, output