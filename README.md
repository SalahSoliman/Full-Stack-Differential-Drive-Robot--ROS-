# Full-Stack-Differential-Drive-Robot--ROS-

The dependencies:

ORBSLAM: https://github.com/appliedAI-Initiative/orb_slam_2_ros 
Turtlebot3: (Already in the files)
World: https://github.com/aws-robotics/aws-robomaker-small-house-world
Codes run on Python 3.6
you will need to have the following installed:
- gazebo, ROS.
- CV_Bridge built from source to work with Python 3.6.
Currently, the robot uses a kinect (RGBD) image to build a map using ORBSLAM, and saves the map in home/.ros
All you've got to do to run the system is the following (after building)

- roslaunch robo_sim depth_robo_empty_world.launch (Which launches the robot and the aws_robomaker_small_house_world)
- roslaunch robo_sim modified_slam.launch (which runs the orb_slam_rgbd node)
You may change the parameters in the later launch file to create a new map.

