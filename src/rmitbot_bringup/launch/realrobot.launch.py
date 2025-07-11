import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    hardware_interface = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_firmware"),
            "launch",
            "hardware_interface.launch.py"
        ),
    )
    
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_controller"),
            "launch",
            "controller.launch.py"
        ),
    )
    
    teleopkeyboard = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("rmitbot_controller"),
            "launch"
            #"teleopkeyboard.launch.py"
        ),
        launch_arguments={
            "use_sim_time": "False"
        }.items()
    )

    # imu_driver_node = Node(
    #     package="bumperbot_firmware",
    #     executable="mpu6050_driver.py"
    # )
    
    return LaunchDescription([
        hardware_interface,
        controller,
        #teleopkeyboard,
        # imu_driver_node,
    ])