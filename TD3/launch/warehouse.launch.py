import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to the SDF file
    sdf_file_path = os.path.join(
        get_package_share_directory('drl_x500'),
        'worlds',
        'warehouse.sdf'
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', sdf_file_path],
            output='screen'
        )
    ])
