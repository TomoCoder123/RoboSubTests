from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='your_package_name',  # Replace with your package name
            executable='image_publisher', # The name of the executable (should match the entry point defined in setup.py)
            name='image_publisher_node',
            output='screen',
            parameters=[],
            arguments=['/path/to/your/videoplayback.mp4']  # Replace with the path to your video file
        ),
    ])
