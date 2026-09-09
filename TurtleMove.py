import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import Twist
import math


class RurMover(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_twist = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.main()

    def publish_twist(self, linear, angular):
        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = math.radians(float(angular))
        self.publisher_twist.publish(msg)
        self.get_clock().sleep_for(Duration(seconds=1.0))

    def main(self):
        self.publish_twist(0, 90.0)
        self.publish_twist(3, 0.0)
        self.publish_twist(0, -120.0)
        self.publish_twist(1, 0.0)
        self.publish_twist(0, -120.0)
        self.publish_twist(1, 0.0)
        self.publish_twist(0, 60.0)
        self.publish_twist(2, 0.0)


def main(args=None):
    rclpy.init(args=args)

    mover = RurMover()

    rclpy.spin(mover)

    mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()