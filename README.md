# Simulating Autonomous Exploration and Object Detection with an E-puck Robot in Webots

A robotic simulation of an e-puck robot in an industrial environment trained to identify red-colored objects and avoid obstacles.

## Project Overview

This project showcases the capabilities of an e-puck robot in a virtual environment. The robot autonomously explores, avoids obstacles, and detects objects by color. Equipped with distance/proximity sensors, it safely navigates by adjusting motor speeds to avoid collisions. The camera sensor enables object detection, specifically red-colored objects, with images saved for analysis. This project has practical applications in search and rescue operations.

![Flowchart](https://github.com/ojumah20/Robotic-Simulation-Webots/blob/main/Image%2016-07-2024%20at%2015.01.jpeg)

## Flowchart

The flowchart above give an overview of the project and shoes the following main states:

1. **Initialization**: The robot is set up with necessary parameters and devices. Wheel motors are configured for continuous rotation, and sensors (distance and camera) are initialized.
2. **Exploration**: The robot moves forward at MAX_SPEED, measuring distances and capturing images. If distance sensors detect an object over 100 units away, it transitions to "Obstacle Avoidance." If a red object is detected, it moves to "Image Capture and Save."
3. **Obstacle Avoidance**: If a sensor detects an object within range, the left wheel speed is set to -MAX_SPEED to turn away from the obstacle, then returns to "Exploration."
4. **Object Detection**: The robot analyzes camera images for red objects. If one is detected and differs from the previous image, it transitions to "Image Capture and Save."
5. **Image Capture and Save**: The robot saves the current image, updates the image counter, and refreshes the previous image, allowing continuous exploration while storing data for future analysis.

## Control Architecture

The robot operates using a closed-loop control system with sensor feedback to adapt and achieve desired outcomes. The Controller processes sensor data to direct robot actions, including velocities and turns. Sensors provide feedback for obstacle detection and object recognition. Motors execute the Controller's commands, ensuring continuous adaptation and stability.

![Loop System](https://github.com/ojumah20/Robotic-Simulation-Webots/blob/main/Image%2016-07-2024%20at%2015.02.jpeg)

## Main Code

The main code can be found in `robot_controller.py`. It initializes the robot, sets its timestep to 20 milliseconds and maximum speed to 3, and configures the motors for continuous rotation. Six distance sensors are enabled for obstacle detection, and a camera is set up for image capture.

In the control loop, the robot continuously captures images. If a recognized object appears, the image is saved with a unique name. The robot processes distance sensor data to adjust its movement, reversing direction when an obstacle is detected. This ensures effective navigation and object recognition.

## Simulation Video

A recorded video of the simulation can be downloaded from [this link](https://drive.google.com/file/d/1Xy5myxZ-eMWhHrQmENpmZP7pxJvrSo3w/view?usp=drive_link).
