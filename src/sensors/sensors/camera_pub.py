import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image  # Import Image message

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 1)  # Change the message type and topic

    def publish_camera_image(self, image_data):
        msg = Image()
        # Fill in the image data and other necessary fields
        msg.data = image_data  # Replace 'image_data' with your actual image data
        msg.width = 640  # Replace with the actual image width
        msg.height = 480  # Replace with the actual image height
        msg.encoding = 'rgb8'  # Replace with the actual image encoding (e.g., 'bgr8', 'mono8', etc.)

        # Publish the camera image
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing camera image')

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()

    # Simulate camera image data (replace with your actual image capturing logic)
    image_data = b'\x00\xFF\x00' * 640 * 480  # Example: Green image

    def publish_image_callback():
        publisher_node.publish_camera_image(image_data)

    # Publish the camera image periodically (replace this with your actual image capturing loop)
    timer_period = 1.0  # Publish every 1 second
    timer = publisher_node.create_timer(timer_period, publish_image_callback)

    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()