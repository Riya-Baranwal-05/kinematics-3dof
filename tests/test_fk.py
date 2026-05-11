import sys
sys.path.insert(0, '/Users/riyabaranwal/kinematics-3dof')
import numpy as np
import pytest
from kinematics.fk import forward_kinematics


def test_all_zeros():
    """When all angles are 0, arm is fully stretched, endpoint should be (3, 0)"""
    _, _, _, (x, y) = forward_kinematics(0, 0, 0, 1, 1, 1)
    assert np.isclose(x, 3.0)
    assert np.isclose(y, 0.0)


def test_90_degrees():
    """When theta1=90, arm points up, endpoint should be (0, 3)"""
    _, _, _, (x, y) = forward_kinematics(np.pi/2, 0, 0, 1, 1, 1)
    assert np.isclose(x, 0.0)
    assert np.isclose(y, 3.0)
