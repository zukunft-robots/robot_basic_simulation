# robot_basic_simulation
This project focus on creating a simple robot model and creating a simulation using ROS2 humble on this robot where we are going to achieve path planning, mapping and navigation. 

------------------------------------------------------------
Task 1 :- Set Up Gazebo Simulation Environment

Install Gazebo and ROS on the development machine.
	-> Operating system :- Ubuntu Jammy 22.04.2 LTS
	-> ROS version :- Ros2 Humble Hawksbill (EOL - May, 2027)
	-> Gazebo version :- Gazebo 11.10.2
	
Set up a new ROS workspace for the simulation project.
	-> Ros package has been created in local machine inside the ros2_simulation_ws
	
Install gazebo.
	-> sudo apt install gazebo

start of second task

Task 2 :- Design Robot Model in URDF

	-> "sudo apt-get install ros-humble-xacro" (install xacro in local machine)
	-> create ament python build type my_robot package inside the src folder
    -> execute "colcon build" 
	-> make urdf file inside the description folder
		description
			-inertial_macros.xacro (this file contains inertial properties of objects which can be used in robot)
			-robot_core.xacro (this file has information of robots componenets such as chassis,sensors and wheels)
			-robot.urdf.xacro (this is the main xacro file)
	--> create launch folder and create below files
		- gazebo.launch.py (to launch model in gazebo)
		- rsp.launch.py (to launch model in rviz)
	--> Most important, copy the launch and description folder inside the install/share directory of workspace
	--> check the urdf model using "check_urdf robot_core.xacro" command

	--> to visulize the model in gazebo use this command
		--> Open the terminal and navigate to workspace then use following command -
			--> ros2 launch my_robot gazebo.launch.py
	--> To visulize the model in Rviz use following method
		--> Open the terminal and navigate to workspace then use following command -
			--> ros2 launch my_robot rsp.launch.py 
		--> Open another terminal and use following command -
			--> rviz2
		--> open another terminal and use following command -
			--> ros2 run joint_state_publisher_gui joint_state_publisher_gui 

Task 3 :- Implement Robot Controller
	-> create gazebo_control.xacro file inside install/.../description location which is responsible movement of robot
	-> create python package name robot_controller in src folder
    -> execute "colcon build"
	-> create controller.py python file for basic movement in package folder
	-> add dependency in package.xml file
	-> add console script inside the setup.py file
	-> run command in workspace to launch gazebo ros2 launch my_robot gazebo.launch.py 
	-> run command in another terminal inside the workspace to make basic movement for robot ros2 run robot_controller basic_movement (or) ros2 run robot_controller basic_movement --ros-args -r /cmd_vel:=/demo/cmd_demo 
    -> ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/demo/cmd_demo   (teleoperation keyboard)

	#Important ros commands :
	1. To create a pkg : <ros2 pkg create --build-type ament_python <package name>>
	2. To build : <colcon build>   ---> first go to root directory of project

		1. if you want to build with symlink use <colcon build --symlink-install> 
		2. if you wnat to build a package with a specific package use <colcon build --packages-select package_name>
		3. if we need to automatically detect use <colcon build --symlink-install --packages-up-to package_name --event-handlers console_cohesion+ --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=1>

	3. To Source : <source install/setup.bash>
				   <source /opt/ros/humble/setup.bash>
	4. To run a Node : go to folder where your nodes are declared ---->  <python3 filename.py>
	5. To list all topics : ros2 topic list
	6. To listen : <ros2 topic echo <topic name>>
	7. To open bashrc file to avoid this multiple time of sourcing <nano ~/.bashrc>

	8. For mapping :  <ros2 launch slam_toolbox online_async_launch.py> 

	9.To disply map in rviz : change fixed frame to <map>
	 click add --> map now select topic  </map>     

	10 to save map, click on panels --> add new panels ---> slam tool plugins  ---> give path at savemap and serilize map right side and click on generate map files were saved.

