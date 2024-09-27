import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    sdf_file_path = os.path.join(
        get_package_share_directory('drl_x500'),
        'worlds',
        'training_env.sdf'
    )

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

    # Gazebo
    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', '-v4', '-r', sdf_file_path],
        output='screen'
    )

    # Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        arguments=[sdf_file_path]
    )

    # Joint State Publisher (for TF)
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
    )

    # MAVROS
    mavros = IncludeLaunchDescription(
        [os.path.join(get_package_share_directory('mavros'), 'launch'), '/px4.launch'],  # Note: No '.py' extension
        launch_arguments={'fcu_url': 'udp://:14540@127.0.0.1:14557'}.items(),
    )

    # Your Custom Python Script
    your_script = Node(
        package='drl_x500',  # Replace with your package
        executable='contrl_node',  # Replace with your script's name
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        joint_state_publisher,  
        mavros,
        your_script,
        rviz,
        lidar_bridge,
        gps_bridge,
        camera_bridge
    ])
