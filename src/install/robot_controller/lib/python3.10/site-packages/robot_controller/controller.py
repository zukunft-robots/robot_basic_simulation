import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.move_robot)
        self.linear_speed_ = 0.0  # m/s
        self.angular_speed_ = 0.0  # rad/s

    def move_robot(self):
        msg = Twist()
        msg.linear.x = self.linear_speed_
        msg.angular.z = self.angular_speed_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    controller = RobotController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
