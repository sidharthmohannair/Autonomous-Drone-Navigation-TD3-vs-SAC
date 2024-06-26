# Comparative Study of Twin Delayed DDPG (TD3) and Soft Actor-Critic (SAC) for Autonomous Drone Navigation

## Objective
This project aims to develop and compare the performance of Twin Delayed DDPG (TD3) and Soft Actor-Critic (SAC) algorithms for autonomous drone navigation. The evaluation will focus on navigation efficiency, obstacle avoidance, and learning efficiency in simulated environments using ROS2 and Gazebo.

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
- Ubuntu 22.04
- ROS2 Humble
- Gazebo
- MAVROS
- Python 3.8+

### Installation Steps

1. **Install ROS2 Humble**


2. **Install Gazebo**
 `

3. **Install MAVROS**


4. **Clone and Set Up PX4 Simulation Environment**

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
To contribute to this project, please follow these steps:

1. **Fork the Repository**
    - Create a personal fork of the project repository on GitHub.

2. **Clone the Repository**
    ```bash
    git clone https://github.com/sidharthmohannair/Autonomous-Drone-Navigation-TD3-vs-SAC
    cd Autonomous-Drone-Navigation-TD3-vs-SAC
    ```

3. **Create a Branch**
    ```bash
    git checkout -b feature-branch-name
    ```

4. **Make Changes**
    - Implement your feature or fix the bug.

5. **Commit and Push**
    ```bash
    git add .
    git commit -m "Description of your changes"
    git push origin feature-branch-name
    ```

6. **Create a Pull Request**
    - Submit a pull request to the main repository.

## License
This project is licensed under the MIT License.

## Contact
For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer.
