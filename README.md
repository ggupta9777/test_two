# What is this package? 

The package reads the camera data from webcam (device id 0), performs a canny edge detection and displays the resulting frame in rviz.

## Requirements

It is necessary that cv_camera package be installed

## How to run

A single launch file is present. It loads the parameters, runs the cv_camera node, runs the canny_edge.py node and displays rviz. It maybe needed to manually load the rviz config (canny_edge.rviz in the launch/ directory). 