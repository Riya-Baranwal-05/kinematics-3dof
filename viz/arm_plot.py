import numpy as np
import matplotlib.pyplot as plt
from kinematics.fk import forward_kinematics

def draw_arm(theta1,theta2,theta3,L1,L2,L3):
    (x_base,y_base),(x1,y1),(x2,y2),(x3,y3) = forward_kinematics(theta1=theta1,theta2=theta2,theta3=theta3,L1=L1,L2=L2,L3=L3)
    X = [x_base,x1,x2,x3]
    Y= [y_base,y1,y2,y3]
    plt.plot(X, Y, 'bo-', markersize=8)  # blue dots at joints
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.grid(True)
    plt.axis('equal')
    plt.title('3-DOF Robot Arm')
    plt.show()