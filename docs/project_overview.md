
# Project Overview

## Objective

This project aims to develop and compare the performance of Twin Delayed DDPG (TD3) and Soft Actor-Critic (SAC) algorithms for autonomous drone navigation. The evaluation focuses on navigation efficiency, obstacle avoidance, and learning efficiency in simulated environments using ROS2 and Gazebo.

## Background

### Twin Delayed DDPG (TD3)

Twin Delayed DDPG (TD3) is an extension of the Deep Deterministic Policy Gradient (DDPG) algorithm. TD3 addresses the overestimation bias in DDPG by using two critic networks to estimate the Q-values and taking the minimum value to reduce overestimation. TD3 also introduces delay in policy updates and target smoothing to improve stability and performance.

### Soft Actor-Critic (SAC)

Soft Actor-Critic (SAC) is an off-policy actor-critic method that aims to maximize both the expected reward and entropy, promoting exploration by encouraging diverse actions. This approach helps in handling tasks that require adaptive and robust performance in dynamic and high-dimensional environments, which is essential for complex navigation scenarios.

## Methodology

1. **Environment Setup**: Creating and configuring simulation environments in Gazebo, integrated with ROS2 for realistic drone control simulations.
2. **Algorithm Implementation**: Developing TD3 and SAC models tailored for drone navigation, including defining state/action spaces and reward functions.
3. **Training and Testing**: Training the models using the simulation environments and evaluating their performance in various scenarios.
4. **Performance Analysis**: Analyzing and comparing the results to identify the strengths and weaknesses of each approach and determining which is more effective for specific navigation tasks.

## Repository Structure

The repository is organized as follows:

```
Autonomous-Drone-Navigation-TD3-vs-SAC/
├── data/                  # Data collected during simulations
├── docs/                  # Documentation and project reports
│   ├── project_overview.md
│   ├── environment_setup.md
│   ├── td3_implementation.md
│   ├── sac_implementation.md
│   ├── performance_analysis.md
│   ├── contributing.md
│   └── project_report.md
├── envs/                  # Gazebo environment files and configurations
├── models/                # Trained DRL models (TD3 and SAC)
├── notebooks/             # Jupyter notebooks for analysis
├── scripts/               # Python scripts for training and evaluation
│   ├── td3/               # TD3 related scripts
│   ├── sac/               # SAC related scripts
├── src/                   # Source code for ROS packages and other implementations
├── tests/                 # Test scripts and validation cases
├── README.md              # Project overview and setup instructions
├── LICENSE                # License information
└── .gitignore             # Files and directories to ignore in git
```

## Goals and Expected Outcomes

- **Compare Algorithms**: Evaluate TD3 and SAC to determine which algorithm performs better for autonomous drone navigation.
- **Analyze Efficiency**: Focus on navigation efficiency, obstacle avoidance, and learning efficiency.
- **Provide Insights**: Offer insights and recommendations based on the comparative analysis for real-world applications of these algorithms in autonomous systems.

## Additional Information

Detailed instructions on setting up the environment, implementing the algorithms, and analyzing the results are provided in the respective documentation files within the `docs/` folder.
