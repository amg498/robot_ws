import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
   tank_launch_file = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turn_on_dlrobot_robot'), 'launch'),
         '/tank.launch.py'])
      )
   rsp_launch_file = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turn_on_dlrobot_robot'), 'launch'),
         '/rsp.launch.py'])
      )

   lidar_launch_file = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turn_on_dlrobot_robot'), 'launch'),
         '/rplidar.launch.py'])
      )
   
   camera_launch_file = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turn_on_dlrobot_robot'), 'launch'),
         '/camera.launch.py'])
      )

   rf2o_launch_file = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turn_on_dlrobot_robot'), 'launch'),
         '/rf2o_laser_odometry.launch.py'])
      )

   return LaunchDescription([
      tank_launch_file,
      rsp_launch_file,
      lidar_launch_file,
      camera_launch_file,
      rf2o_launch_file
      
   ])
