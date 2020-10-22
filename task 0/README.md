## Problem Statement
The objective of the task is to move the turtle inside the turtlesim window in a circle and stop at its initial location.
Teams are supposed to do this by creating a nodes name, /node_turtle_revolve within a python script, node_turtle_revolve.py.

### Procedure
First, create a package named pkg_task0, within your catkin workspace. Once done, compile and source the packages.
```
cd ~/catkin_ws
catkin build
source devel/setup.bash
```
Within this package, you should have a scripts folder inside which you'll create a python script, named node_turtle_revolve.py. 
After completing the python script. Make it executable, if it isn't already. To do that, enter the following code.
```
chmod +x ~/catkin_ws/src/pkg_task0/scripts/node_turtle_revolve.py
```
Before executing make sure that roscore is running along with turtlesim_node. You can either run them in separate terminals or simply create a task0.launch file inside the ~/catkin_ws/src/pkg_task0/launch/ folder. Launch file can run multiple nodes unlike a python/cpp script. Run the launch file, enter,
```
roslaunch pkg_task0 task0.launch 
```
 This should run three processes in parallel.
        - roscore
        - turtlesim_node
        - node_turtle_revolve.py
