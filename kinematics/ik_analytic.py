import numpy as np

def inverse_kinematics(x,y,L1,L2,L3):

    """
    Computer theta1, theta2 , theta3 for 3DOF planar arm in radians

    Args:
      x,y: position of end effector
      L1,L2,L3: Length of each arm

    return all joint angles 
    """
    x_base,y_base=0,0

    r = np.sqrt((x-x_base)**2 + (y-y_base)**2)

    cos_theta2 = (L1**2+L2**2-r**2)/(2*L1*L2)
    cos_theta2 = np.clip(cos_theta2,-1,1)
    theta2 = np.arccos(cos_theta2)
    theta1 = np.arctan2(y,x)-np.arctan2(L2*np.sin(theta2),L1+L2*np.cos(theta2))

    theta3 = 0

    return theta1, theta2, theta3