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

import matplotlib.animation as animation

def create_gif(filename='demo.gif'):
    """Animate arm moving through different angles and save as GIF"""
    fig, ax = plt.subplots()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.grid(True)
    ax.set_aspect('equal')
    line, = ax.plot([], [], 'bo-', markersize=8)
    
    def update(frame):
        theta1 = (frame / 100) * 2 * np.pi  # sweeps from 0 to 2π
        theta2 = np.sin(frame * 0.1) * np.pi/3  # oscillates
        theta3 = np.cos(frame * 0.1) * np.pi/4  # oscillates
        (x_base,y_base),(x1,y1),(x2,y2),(x3,y3)=forward_kinematics(theta1,theta2,theta3,1,1,1)
        X = [x_base, x1, x2, x3]
        Y = [y_base, y1, y2, y3]
        line.set_data(X, Y)
        return line,
    ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
    ani.save(filename, writer='pillow')
    print(f'GIF saved to {filename}')

if __name__ == '__main__':
    create_gif('viz/demo.gif')