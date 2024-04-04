import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
import launch_ros.actions
from launch.launch_description_sources import PythonLaunchDescriptionSource

#def launch(launch_descriptor, argv):
def generate_launch_description():
    # package_name='turn_on_dlrobot_robot' #<--- CHANGE ME

    # rsp = IncludeLaunchDescription(
    #             PythonLaunchDescriptionSource([os.path.join(
    #                 get_package_share_directory(package_name),'launch','rsp.launch.py'
    #             )]), launch_arguments={'use_sim_time': 'false'}.items()
    # )

    # robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])

    akmcar = LaunchConfiguration('akmcar', default='false')
    return LaunchDescription([
        # rsp,
        DeclareLaunchArgument(
            'akmcar',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
#the default mode is akm
        launch_ros.actions.Node(
            condition=IfCondition(akmcar),
            package='turn_on_dlrobot_robot', 
            executable='dlrobot_robot_node', 
            parameters=[{'usart_port_name': '/dev/ttyACM0',
                'serial_baud_rate': 115200,
                'robot_frame_id': 'base_link',
                'odom_frame_id': 'odom_combined',
                'cmd_vel': 'cmd_vel',
                'akm_cmd_vel': 'ackermann_cmd',
                'product_number': 0,}],
            remappings=[('/cmd_vel', 'cmd_vel'),]),

        launch_ros.actions.Node(
            condition=IfCondition(akmcar),
            package='turn_on_dlrobot_robot', 
            executable='cmd_vel_to_ackermann_drive.py', 
            name='cmd_vel_to_ackermann_drive',
            output='screen'),

        # launch_ros.actions.Node(
        #     # condition=IfCondition(akmcar),
        #     package='robot_state_publisher', 
        #     executable='robot_state_publisher', 
        #     name='robot_state_publisher',
        #     output='screen',
        #     parameters=[{'use_sim_time': False,'robot_description': robot_description}]
        #     ),

        # launch_ros.actions.Node(
        #     # condition=IfCondition(akmcar),
        #     package='joint_state_publisher', 
        #     executable='joint_state_publisher', 
        #     name='joint_state_publisher',
        #     output='screen',
        #     parameters=[{'use_sim_time': False,'robot_description': robot_description}]
        #     ),

#the default mode is not akm
        launch_ros.actions.Node(
            condition=UnlessCondition(akmcar),
            package='turn_on_dlrobot_robot', 
            executable='dlrobot_robot_node', 
            parameters=[{'usart_port_name': '/dev/ttyACM0',
                'serial_baud_rate': 115200,
                'robot_frame_id': 'base_link',
                'odom_frame_id': 'odom_combined',
                'cmd_vel': 'cmd_vel',
                'akm_cmd_vel': 'none',
                'product_number': 0,}],
            )


  ])
