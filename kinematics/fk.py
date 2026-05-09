import numpy as np

def forward_kinematics(theta1, theta2, theta3, L1, L2, L3):
    """
    Compute end-effector position for a 3-DOF planar arm

    Args:
        theta1, theta2,theta3: joint angles in radians
        L1,L2,L3: link lengths
    Returns:
        (x,y): end-effector position

    """
    x_base ,y_base =0,0
    x1 = L1*np.cos(theta1) + x_base
    y1 = L1*np.sin(theta1) + y_base

    x2 = x1 + L2*np.cos(theta1+theta2)
    y2 = y1 + L2*np.sin(theta1+theta2)

    x3 = x2 + L3*np.cos(theta1+theta2+theta3)
    y3 = y2 + L3*np.sin(theta1+theta2+theta3)

    return (x_base,y_base) , (x1,y1),(x2,y2),(x3,y3)