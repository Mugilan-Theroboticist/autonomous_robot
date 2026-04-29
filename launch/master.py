from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource, AnyLaunchDescriptionSource 
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_neo = get_package_share_directory('neo')
    pkg_nav2 = get_package_share_directory('nav2_bringup')

    simulation_launch = os.path.join(pkg_neo, 'launch', 'mygazebo.launch.xml')
    localization_launch = os.path.join(pkg_nav2, 'launch', 'localization_launch.py')
    navigation_launch = os.path.join(pkg_nav2, 'launch', 'navigation_launch.py')

    map_file = '/home/mugilan/ros_ws/src/neo/maps/my_map.yaml'

    return LaunchDescription([

        # 🔹 1. Gazebo + Robot (XML)
        IncludeLaunchDescription(
            AnyLaunchDescriptionSource(simulation_launch)
        ),

        # 🔹 2. Localization
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(localization_launch),
            launch_arguments={
                'map': map_file,
                'use_sim_time': 'true'
            }.items()
        ),

        # 🔹 3. Navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(navigation_launch),
            launch_arguments={
                'map': map_file,
                'use_sim_time': 'true'
            }.items()
        ),

    ])