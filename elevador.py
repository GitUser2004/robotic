import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8

valor = int(0)

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('sub2')
        self.subscription = self.create_subscription(Int8, 'mensaj', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.j = msg.data
        valor = msg.data 

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('pub2')
        self.publisher_ = self.create_publisher(Int8, 'mens', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int8()
        msg.data = valor * valor
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()