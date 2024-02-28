#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__("simple")
        self.get_logger().info("Publisher node stared")
        self.publisher_=self.create_publisher(String,'news',10)
        timer_ = self.create_timer(0.5, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = "Publishing News"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
   
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()