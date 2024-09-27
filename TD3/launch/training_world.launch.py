import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    # Path to the SDF file
    sdf_file_path = os.path.join(
        get_package_share_directory('drl_x500'),
        'worlds',
        'training_env.sdf'
    )

    # Robot State Publisher
    # robot_state_publisher_node = Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher',
    #     name='robot_state_publisher',
    #     output='screen',
    #     arguments=[
    #         '--ros-args', 
    #         '-p', 'use_sim_time:=true',  
    #         '-p', f'robot_description:=$(find-pkg-share drl_x500)/worlds/training_env.sdf'
    #     ]
    # )

#     # RViz Configuration
#     rviz_config_file = os.path.join(
#         get_package_share_directory('drl_x500'),
#         'rviz',
#         'config.rviz'  
#     )
#     rviz_node = ExecuteProcess(
#         cmd=['rviz2', '-d', rviz_config_file],
#         output='screen'
#     )

#     # ROS-Gazebo Bridge Configuration
#     bridge = IncludeLaunchDescription(
#     PythonLaunchDescriptionSource([os.path.join(
#         get_package_share_directory('ros_gz_bridge'),
#         'launch',
#         'ros_gz_bridge.launch.py'
#     )]),
#     launch_arguments={
#         'config_file': os.path.join(
#             get_package_share_directory('drl_x500'), 
#             'config',
#             'iris_lidar_bridge.yaml'   # Update to your YAML filename
#         ),
#         'name': 'my_bridge_node'
#     }.items()
#     )


    # Bridge
    lidar_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/lidar@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'],
        output='screen'
    )
    gps_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/gps@sensor_msgs/msg/NavSatFix@gz.msgs.NavSatFix'],
        # remappings=[
        #     ('/gps', 'your/custom/gps/topic')
        # ]
        output='screen'
    )
    camera_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/camera@sensor_msgs/msg/Image@gz.msgs.Image'],
        # remappings=[
        #     ('/camera/image_raw', '/camera')
        # ],
        output='screen'
    )


    rviz_config_file = os.path.join(
        get_package_share_directory('drl_x500'),
        'rviz',
        'config.rviz')

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )





    # Declare launch argument for config file
    declare_config_file_cmd = DeclareLaunchArgument(
        'config_file',
        default_value=os.path.join(get_package_share_directory('drl_x500'), 'iris_lidar_bridge.yaml'),
        description='Configuration file for ROS-Gazebo Bridge'
    )


    # # TF Broadcaster (Joint State Publisher)
    # joint_state_publisher_node = Node(
    #     package='joint_state_publisher_gui',  
    #     executable='joint_state_publisher_gui',
    #     name='joint_state_publisher_gui',
    #     output='screen'
    # )


    return LaunchDescription([
        # Gazebo Simulation
        ExecuteProcess(
            cmd=['gz', 'sim', '-v4', '-r', sdf_file_path],
            output='screen'
        ),
        # Declare launch argument for config file
        declare_config_file_cmd,
        # Robot State Publisher
        #robot_state_publisher_node, 
               # RViz
        rviz,
        # ROS-Gazebo Bridge
        # joint_state_publisher_node,
        lidar_bridge,
        gps_bridge,
        camera_bridge
    ])

