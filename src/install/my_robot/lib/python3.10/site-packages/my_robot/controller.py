import rclpy
from geometry_msgs.msg import Twist

rclpy.init()
node = rclpy.create_node('controller')

cmd_vel_pub = node.create_publisher(Twist, 'cmd_vel', 10)

cmd = Twist()

while rclpy.ok():
    # Set linear and angular velocity values based on your desired movement
    cmd.linear.x = 0.2  # Forward linear velocity
    cmd.angular.z = 0.0  # No angular velocity (turning)

    cmd_vel_pub.publish(cmd)
    rclpy.spin_once(node)


node.destroy_node()
rclpy.shutdown()

