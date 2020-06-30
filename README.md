# keyboard_control

### How to Install
1. cd to the src folder in your catkin workspace, and clone this repository there (assuming you have ros and git installed)
2. ```git clone https://github.com/jbennet-t/keyboard_control.git```
3. Install the python getch module: ```pip3 install getch```

### How to Run
1. In the first terminal tab, run ```roscore```
2. In a new tab, source ```devel/setup.bash```
3. cd to ```/opt/ros/noetic/share/stage_ros``` or wherever stage_ros is installed for your ROS version
4. Run ```rosrun stage_ros stageros $(rospack find stage_ros)/world/willow-erratic.world```
5. A window with the sim running should appear
6. In a new tab, source ```devel/setup.bash```
7. roscd to wherever you cloned the repository (```.../src/keyboard_control```)
8. Run the program: ```rosrun keyboard_control keyboard_input.py```

Note: you may have to install pip3 and if it is not already part of your python install
* pip install: https://pip.pypa.io/en/stable/installing/
