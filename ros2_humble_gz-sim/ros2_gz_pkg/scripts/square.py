import time
from pymavlink import mavutil

def wait_for_ack(master, command):
    """ Wait for an ACK from the specified command. """
    while True:
        ack = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack and ack.command == command:
            return ack.result

# Connect to the drone
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
master.wait_heartbeat()

# Switch to GUIDED mode
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    4  # GUIDED mode
)
print("Switching to GUIDED mode")

# Arm the drone
master.arducopter_arm()
print("Arming motors")
master.motors_armed_wait()
print('Motors armed')

# Takeoff to 15 meters
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0, 0, 0, 0, 0, 0, 0, 15
)
print("Taking off to 15 meters")
time.sleep(15)  # Wait for the drone to reach the altitude

# Function to send the drone to a position (local coordinates)
def goto_position_target_local_ned(master, north, east, down):
    master.mav.set_position_target_local_ned_send(
        0,       # time_boot_ms (not used)
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111111000, # Ignore everything except position
        north, east, down, # x, y, z positions in meters
        0, 0, 0, # x, y, z velocity in m/s
        0, 0, 0, 0, 0)    # x, y, z acceleration and yaw/yaw_rate (not used)
    
# Fly in a square pattern (10 meters per side)
for i in range(1):
    # North
    goto_position_target_local_ned(master, 5, 0, -15)
    time.sleep(5)

    # East
    goto_position_target_local_ned(master, 5, 5, -15)
    time.sleep(5)

    # South
    goto_position_target_local_ned(master, 0, 5, -15)
    time.sleep(5)

    # West (back to start)
    goto_position_target_local_ned(master, 0, 0, -15)
    time.sleep(5)

    # North
    goto_position_target_local_ned(master, 5, 0, -15)
    time.sleep(5)

    # East
    goto_position_target_local_ned(master, 5, 5, -15)
    time.sleep(5)


# Return to Launch (RTL)
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
    0, 0, 0, 0, 0, 0, 0, 0
)
print("Returning to Launch (RTL)")
time.sleep(20) 

local_pos = master.recv_match(type='LOCAL_POSITION_NED', blocking=True, timeout=5)
while local_pos.z < 0.2:
    time.sleep(5)

master.arducopter_disarm()  # Use the convenience function for disarming
print("Disarming motors")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,     # 0: disarm
    21196,  # Magic number for FORCE_DISARM 
    0, 0, 0, 0, 0, 0
)


print("Mission complete")