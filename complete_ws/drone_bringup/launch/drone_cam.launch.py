from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    usb_cam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('usb_cam'),
                         'launch/launch.py')
    )
    )

    aruco_recognition_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros2_aruco'),
                         'launch/aruco_recognition.launch.py')
        )
    )

    drone_urdf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('drone_urdf'),
                            'launch.py')
        )
    )


    ld.add_action(usb_cam_launch)
    ld.add_action(aruco_recognition_launch)
    ld.add_action(drone_urdf_launch)
    return ld
