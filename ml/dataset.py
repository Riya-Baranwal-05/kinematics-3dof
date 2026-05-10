import numpy as np
import sys
sys.path.insert(0, '/Users/riyabaranwal/kinematics-3dof')
from kinematics.ik_analytic import inverse_kinematics
def generate_dataset(n_samples, L1=1, L2=1, L3=1):
    """
    Generate dataset using analytic IK for consistent labels.
    Input: random (x, y, phi)
    Output: analytic IK solution (theta1, theta2, theta3)
    """
    inputs = []
    outputs = []
    
    count = 0
    while count < n_samples:
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        phi = np.random.uniform(-np.pi, np.pi)
        
        try:
            t1, t2, t3 = inverse_kinematics(x, y, L1, L2, L3, phi)
            if not any(np.isnan([t1, t2, t3])):
                inputs.append([x, y, phi])
                outputs.append([t1, t2, t3])
                count += 1
        except:
            continue
    
    return np.array(inputs), np.array(outputs)