import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan # Import LaserScan message

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_lidar_node')
        self.publisher_ = self.create_publisher(LaserScan, '/custom_scan', 10)  # Change the message type and topic
        self.subscription_ = self.create_subscription(
            LaserScan, '/scan', self.scan_callback, 10)  # Subscribe to /scan topic

    def scan_callback(self, msg):
        # This callback is called when new LiDAR data is received
        self.publisher_.publish(msg)  # Publish the received LiDAR data
        self.get_logger().info('Publishing LiDAR data')

def main(args=None):
    rclpy.init(args=args)
    publisher_lidar_node = PublisherNode()
    rclpy.spin(publisher_lidar_node)
    publisher_lidar_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
