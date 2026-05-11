import sys
sys.path.insert(0, '/Users/riyabaranwal/kinematics-3dof')
import numpy as np
import pytest
from kinematics.fk import forward_kinematics
from kinematics.ik_analytic import inverse_kinematics

def test_roundtrip():
    _, _, _, (x, y) = forward_kinematics(np.pi/2, 0, np.pi/2, 1, 1, 1)
    phi = np.pi
    theta1,theta2,theta3=inverse_kinematics(x,y,1,1,1,phi)
    _,_,_,(x_n,y_n)=forward_kinematics(theta1,theta2,theta3,1,1,1)
    assert np.isclose(x,x_n)
    assert np.isclose(y,y_n)