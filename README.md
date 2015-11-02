Evol UArm basic support for ROS

John Nagle
nagle@animats.com

Some basic support for the Evol UArm robot arm for use with the Robot Operating System.

Evol has several sets of firmware for the UArm.  This uses the "Standard" firmware, which
allows sending commands to the arm but does not provide any response from the arm.


Quick start, assuming knowledge of ROS.

    1. Install ROS (preferably ROS Jade.)
    2. Install this package into ~/catkin_ws/src/ as uarm_utils
    3. Build with catkin_make
    4. Connect up UArm, and find its serial port.  UArm should have the Evol "Standard" firmware loaded.
    5. Edit the "params.yaml" file to contain the path to the UARM's serial port.
    6. In launch directory, roslaunch movetest1.launch
    
This just moves the arm around, following a canned pattern in movetest1.py.

For useful work, it's necessary to write something to replace "movetest1.py"
to send more useful move commands to the robot.
