# Development of an Autonomous Drone Navigation System in a Simulated Environment Using ROS 2 Humble Hawksbill, Gazebo Harmonic, and ArduPilot

## Objective
The primary objective of this project is to develop a comprehensive autonomous drone navigation system by creating a simulated environment in Gazebo using ROS 2. This involves integrating ArduPilot with ROS 2 within the simulation to control and monitor the drone's flight dynamics and behavior. Additionally, the project aims to develop and execute scripts that command the drone to perform specific tasks, such as flying in predefined patterns like squares and circles within the simulated environment. 

## Project Overview

For a detailed overview of the project, including background information, methodology, and repository structure, please refer to the [Project Overview](docs/project_overview.md) document.

## Project Structure
```
Autonomous-Drone-Navigation-TD3-vs-SAC/
├── data/                  # Data collected during simulations
├── docs/                  # Documentation and project reports
├── envs/                  # Gazebo environment files and configurations
├── models/                # Trained DRL models (PPO and SAC)
├── notebooks/             # Jupyter notebooks for analysis
├── scripts/               # Python scripts for training and evaluation
│   ├── td3/               # PPO related scripts
│   ├── sac/               # SAC related scripts
├── src/                   # Source code for ROS packages and other implementations
├── tests/                 # Test scripts and validation cases
├── README.md              # Project overview and setup instructions
├── LICENSE                # License information
└── .gitignore             # Files and directories to ignore in git
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

## Training and Evaluating Models

### TD3 Algorithm
1. **Train the TD3 Model**


2. **Evaluate the TD3 Model**


### SAC Algorithm
1. **Train the SAC Model**

2. **Evaluate the SAC Model**

## Contributing

Please see the  [CONTRIBUTING.md](/docs/contributing.md) file for guidelines on how to contribute to this project.


## License
This project is licensed under the [MIT License](/LICENSE).

## Contact
For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer.
