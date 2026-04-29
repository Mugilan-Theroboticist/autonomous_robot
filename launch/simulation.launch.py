from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():

    # Package path
    pkg_neo = get_package_share_directory('neo')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # File paths
    urdf_path = os.path.join(pkg_neo, 'urdf', 'myrobot.xacro')
    rviz_config_path = os.path.join(pkg_neo, 'rviz', 'urdf_config.rviz')
    gazebo_config_path = os.path.join(pkg_neo, 'config', 'gz_bridge.yaml')
    world_path = os.path.join(pkg_neo, 'worlds', 'demo_world.sdf')

    # Process xacro → URDF
    robot_description_config = xacro.process_file(urdf_path)
    robot_description = {'robot_description': robot_description_config.toxml()}

    return LaunchDescription([

        # 🔹 Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[robot_description],
            output='screen'
        ),

        # 🔹 Gazebo Simulation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
            ),
            launch_arguments={
                'gz_args': world_path + ' -r'
            }.items()
        ),

        # 🔹 Spawn Robot
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', 'robot_description'],
            output='screen'
        ),

        # 🔹 Bridge
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            parameters=[{'config_file': gazebo_config_path}],
            output='screen'
        ),

        # 🔹 RViz
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        ),

    ])