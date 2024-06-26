# Comparative Study of Twin Delayed DDPG (TD3) and Soft Actor-Critic (SAC) for Autonomous Drone Navigation

## Objective
This project aims to develop and compare the performance of Twin Delayed DDPG (TD3) and Soft Actor-Critic (SAC) algorithms for autonomous drone navigation. The evaluation will focus on navigation efficiency, obstacle avoidance, and learning efficiency in simulated environments using ROS2 and Gazebo.

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

#### Operating System
- Ubuntu 22.04

#### Development Tools
- Git
- Python 3.8+
- pip (Python package installer)

#### Robotics Middleware
- ROS2 Humble

#### Simulation Environment
- Gazebo (compatible with ROS2 Humble, typically Gazebo 11 or newer)

#### Drone Firmware and Control
- ArduPilot

#### Flight Controller
- Cube Orange

#### Companion Computer
- Raspberry Pi 5

#### Communication Interface
- MAVROS

#### Ground Control Software
- QGroundControl (QGC)

#### Python Libraries
- NumPy
- Stable Baselines3
- Gym
- Matplotlib (for plotting and visualization)
- pandas (for data analysis)
- Jupyter Notebook (for interactive development)

#### Additional Tools
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
