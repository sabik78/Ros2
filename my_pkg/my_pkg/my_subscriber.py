#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class MySubscriber(Node):
    def __init__(self):
        super().__init__("my_subscriber")
        self.get_logger().info("Subscriber Node Started")
        self.subscriber_=self.create_subscription(String,'news', self.display_news,10)
        

    def display_news(self,msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = MySubscriber()
   
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()