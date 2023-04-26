import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.contador = 0

    def move_turtle(self):
        self.contador +=1
        if self.contador == 1:
            self.twist_msg_.linear.x = 3.0 
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)
            print(self.contador)
        if self.contador == 2:
            self.twist_msg_.linear.x = 0.0 
            self.twist_msg_.angular.z = 2.0
            self.publisher_.publish(self.twist_msg_)
        if self.contador == 3:
            self.twist_msg_.linear.x = 3.0 
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)
        if self.contador == 4:
            self.twist_msg_.linear.x = 0.0 
            self.twist_msg_.angular.z = 2.2
            self.publisher_.publish(self.twist_msg_)
        if self.contador == 5:
            self.twist_msg_.linear.x = 3.1 
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)
        if self.contador == 6:
            self.twist_msg_.linear.x = 0.0 
            self.twist_msg_.angular.z = 2.0
            self.publisher_.publish(self.twist_msg_)

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()