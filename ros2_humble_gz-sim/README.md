# Development of a Simulated Environment Using ROS 2 Humble Hawksbill, Gazebo Harmonic, and ArduPilot for Autonomous Drone Navigation 

## Objective
This project aims to develop and compare the performance of Twin Delayed DDPG (TD3) and Soft Actor-Critic (SAC) algorithms for autonomous drone navigation. The evaluation will focus on navigation efficiency, obstacle avoidance, and learning efficiency in simulated environments using ROS2 and Gazebo.

## Project Overview

For a detailed overview of the project, including background information, methodology, and repository structure, please refer to the [Project Overview](docs/project_overview.md) document.

## Project Structure
```
ros2_humble_gz-sim/
├── ros2_gz_pkg/
│   ├── config/               # PPO related scripts
│   ├── launch/ 
│   ├── models/               # PPO related scripts
│   ├── py_launch_example/ 
│   ├── resource/               # PPO related scripts
│   ├── rviz/ 
│   ├── scripts/               # PPO related scripts
│   ├── test/ 
│   ├── worlds/               # PPO related scripts
│   ├── LICENCE/
│   ├── package.xml/               # PPO related scripts
│   ├── setup.cfg/ 
│   ├── setup.py/               # PPO related scripts                                 
├── README.md              # Project overview and setup instructions
            
```


## Setup Instructions

### Prerequisites

#### 1. Operating System
- Ubuntu 22.04

#### 2. Development Tools
- Git
- Python 3.8+
- pip (Python package installer)

#### 3. Robotics Middleware
- ROS2 Humble

#### 4. Simulation Environment
- Gazebo (compatible with ROS2 Humble, typically Gazebo 11 or newer)

#### 5. Drone Firmware and Control
- ArduPilot

#### 6. Flight Controller
- Cube Orange

#### 7. Companion Computer
- Raspberry Pi 5

#### 8. Communication Interface
- MAVROS

#### 9. Ground Control Software
- QGroundControl (QGC)

#### 10. Python Libraries
- NumPy
- Stable Baselines3
- Gym
- Matplotlib (for plotting and visualization)
- pandas (for data analysis)
- Jupyter Notebook (for interactive development)

#### 11. Additional Tools
- Colcon (ROS2 build tool)
- Wget (for downloading dependencies)
- curl (for downloading dependencies)

### Installation Steps

1. **Install ROS2 Humble**


2. **Install Gazebo**
 `

3. **Install MAVROS**


4. **Clone and Set Up ArduPilot with Gazebo for Simulation**

5. **Set Up the Environment for Gazebo Models and Plugins**

6. **Install Python Libraries**

7. **Install QGroundControl**


## Running the Simulation

1. **Start the Gazebo Simulation**
    ```bash
    sim_vehicle.py -v ArduCopter -f gazebo-iris --console --map
    ```

2. **Launch MAVROS**
    ```bash
    ros2 launch mavros mavros.launch.py
    ```


## Contributing

Please see the  [CONTRIBUTING.md](/docs/contributing.md) file for guidelines on how to contribute to this project.


## License
This project is licensed under the [MIT License](/LICENSE).

## Contact
For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer.
