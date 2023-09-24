import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image  # Import Image message

class SubscriberNode(Node):

    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription_ = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)  # Subscribe to /camera/image_raw topic

    def image_callback(self, msg):
        # This callback is called when a new camera image is received
        self.get_logger().info('Received camera image')
        self.get_logger().info('Width: %d' % msg.width)
        self.get_logger().info('Height: %d' % msg.height)
        self.get_logger().info('Encoding: %s' % msg.encoding)

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = SubscriberNode()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()