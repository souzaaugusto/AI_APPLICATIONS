# CARLA-ROS Bridge<sup>2</sup>
## Make a bridge between Carla scenarios and the ROS framework

## Installation

### Install the ROS 1 (Melodic version)

1. Run ```ros_install.launch``` to install the full ROS framework and its dependencies

    ```bash
    chmod +x ros_install.launch
    ```
    ```bash
    ./ros_install.launch
    ```
2 . Or you can go to the site and follow the install instructions

[ROS installation link](http://wiki.ros.org/melodic/Installation/Ubuntu)

### Install the CARLA-ROS Bridge

1. Run ```carla_ros_bridge.launch``` to install the carla-ros bridge into the /opt path

    ```bash
    chmod +x carla_ros_bridge.launch
    ```
    ```bash
    ./carla_ros_bridge.launch
    ```
2 . Or you can go to the site and follow the install instructions

https://carla.readthedocs.io/en/0.9.11/ros_installation/


## Usage
1. Replace the lib files for the files from the repository. The path:
'/opt/carla-ros-bridge/melodic/lib/python2.7/dist-packages/carla_ros_bridge'
To make this only in the root user.

2. Run ```CarlaUE4.sh``` on the main folder

    ```bash
    bash CarlaUE4.sh
    ```

3. Run ```run_ros_bridge.launch``` to set the right Python path with the Carla egg file (ROS melodic work in Python2), source the ROS setup path, and then run the ROS bridge. 


4. Run ```sas2.sh``` on the folder `<Carla Main Directory>/PythonAPI/examples/`

    ```bash
    bash sas2.sh [options]
    ```

Options:

```text
Syntax: run_main.sh [-s|p|r|b|i|a]

s     Selects the scenario to simulate. Can choose a scenario between 1 and 9.
      If gets 0 will run all scenarios. Run all scenarios by default
p     Enables plot of charts in the end of simulation. Disabled by default.
r     Enables plot of route of each vehicle in scenario. Disabled by default.
b     Enables bounding boxes of ISO's 17387 in scenario. Disabled by default.
i     Enables remote host. Needs the IP adress of host. Local host enabled by default.
a     Enables all visualization. Disabled by default.
```
