import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class RelayNode(Node):
    def __init__(self):
        super().__init__('inter')

        # Suscriptor
        self.subscriber = self.create_subscription(
            Int32,    
            'mensaj',
            self.listener_callback,
            10
        )

        # Publicador
        self.publisher = self.create_publisher(
            Int32,          # Tipo de mensaje
            'mens',       # Nombre del tópico donde publicará
            10              # QoS
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"llego: {msg.data}")

        nuevo_valor = Int32()
        nuevo_valor.data = msg.data * msg.data

        self.publisher.publish(nuevo_valor)
        self.get_logger().info(f"sale: {nuevo_valor.data}")

def main(args=None):
    rclpy.init(args=args)
    node = RelayNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
