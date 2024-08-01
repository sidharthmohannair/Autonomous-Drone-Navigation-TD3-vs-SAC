# import os
# from launch import LaunchDescription
# from launch.actions import ExecuteProcess
# from ament_index_python.packages import get_package_share_directory

# def generate_launch_description():
#     # Path to the SDF file
#     sdf_file_path = os.path.join(
#         get_package_share_directory('py_launch_example'),
#         'worlds',
#         'training_env.sdf'
#     )

#     return LaunchDescription([
#         ExecuteProcess(
#             cmd=['gz', 'sim', '-r', sdf_file_path],
#             output='screen'
#         )
#     ])

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_my_pkg = get_package_share_directory('py_launch_example')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
           'gz_args': '-r training_env.sdf'
        }.items(),
    )

    # RViz
    rviz = Node(
       package='rviz2',
       executable='rviz2',
       # FIXME: Generate new RViz config once this demo is usable again
       # arguments=['-d', os.path.join(pkg_ros_gz_sim_demos, 'rviz', 'gpu_lidar.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )

    # Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/lidar@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan/'],
        output='screen'
    )

    # FIXME: need a SDF file (gpu_lidar.sdf) inside ros_gz_point_cloud/
    return LaunchDescription([
        gz_sim,
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),
        bridge,
        rviz
    ])