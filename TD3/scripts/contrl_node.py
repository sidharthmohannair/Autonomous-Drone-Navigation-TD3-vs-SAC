import rclpy
from mavros_msgs.srv import CommandBool, CommandTOL, SetMode
from rclpy.node import Node

class TakeoffController(Node):
    def __init__(self):
        super().__init__('takeoff_controller')
        
        # Clients for MAVROS services
        self.arm_client = self.create_client(CommandBool, '/mavros/cmd/arming')
        self.takeoff_client = self.create_client(CommandTOL, '/mavros/cmd/takeoff')
        self.set_mode_client = self.create_client(SetMode, '/mavros/set_mode')
        
        # Wait for services to be available
        self.arm_client.wait_for_service()
        self.takeoff_client.wait_for_service()
        self.set_mode_client.wait_for_service()

    def arm(self):
        req = CommandBool.Request()
        req.value = True
        self.arm_client.call_async(req)

    def takeoff(self, altitude=3.0):
        req = CommandTOL.Request()
        req.altitude = altitude
        self.takeoff_client.call_async(req)

    def set_mode(self, mode="OFFBOARD"):
        req = SetMode.Request()
        req.custom_mode = mode
        self.set_mode_client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    takeoff_controller = TakeoffController()

    # Arm the drone
    takeoff_controller.set_mode(mode="GUIDED")
    takeoff_controller.arm()

    # Take off
    takeoff_controller.takeoff()

    rclpy.spin(takeoff_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
