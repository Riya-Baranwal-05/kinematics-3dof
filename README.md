# Kinematics 3-DOF Arm

## What does this project do?
This project builds a Forward and Inverse Kinematics solver for a 
3-joint planar robot arm. 
Forward Kinematics: It would calculate the position and orientation of end-effector based on known joint angles using D-H parameters
Inverse Kinematics: To calculate the necessary joint angles to move the robot's end effector to a specific target

## Project Structure
- `kinematics/` — has equations and robot parameters
- `ml/` — the model that learns the movement
- `viz/` — visualization of the arm robot
- `tests/` — unit tests to verify FK and IK correctness
- `notebooks/` — results, plots, analysis

## What I will learn
- Denavit-Hartenberg parameters
- Rotation matrices and transform chaining
- Analytical vs neural IK comparison

## References
- Modern Robotics — Lynch & Park: https://modernrobotics.org