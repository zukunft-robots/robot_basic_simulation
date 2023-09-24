import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan  # Import LaserScan message

class SubscriberNode(Node):

    def __init__(self):
        super().__init__('subscriber_lidar_node')
        self.subscription_ = self.create_subscription(
            LaserScan, '/custom_scan', self.scan_callback, 10)  # Subscribe to /custom_scan topic

    def scan_callback(self, msg):
    # Access the LiDAR data
        ranges = msg.ranges  # List of LiDAR measurements

        # Print only a minimum value
        x = min(ranges)
        # This callback is called when new LiDAR data is received on /custom_scan topic
        self.get_logger().info('Subscribed LiDAR data: %s' % x)

def main(args=None):
    rclpy.init(args=args)
    subscriber_lidar_node = SubscriberNode()
    rclpy.spin(subscriber_lidar_node)
    subscriber_lidar_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()