from setuptools import find_packages, setup

package_name = 'robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zukunft',
    maintainer_email='zukunft@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'basic_movement = robot_controller.controller:main',
                'cam_pub = sensors.camera_pub:main',
                'cam_sub = sensors.camera_sub:main',
                'lid_pub = sensors.lidar_pub:main',
                'lid_sub = sensors.lidar_sub:main',
            
        ],
    },
)
