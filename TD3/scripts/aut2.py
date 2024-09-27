import time
from math import sin, cos, radians
from pymavlink import mavutil

# Connect to the drone
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
master.wait_heartbeat()

# Arm the drone
master.arducopter_arm()
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

# Request GLOBAL_POSITION_INT message
master.mav.request_data_stream_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_POSITION,
    1,
    1
)

# Wait for the GLOBAL_POSITION_INT message
def wait_for_message(master, message_type, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        msg = master.recv_match(type=message_type, blocking=True)
        if msg:
            return msg
    print(f"Timeout waiting for {message_type} message")
    return None

global_position_msg = wait_for_message(master, 'GLOBAL_POSITION_INT')

# Extract position data from the stored message
if global_position_msg:
    center_x = global_position_msg.lat / 1e7
    center_y = global_position_msg.lon / 1e7
    center_z = global_position_msg.relative_alt / 1e3
    print(f"Current position: ({center_x}, {center_y}, {center_z})")
else:
    print("Failed to get position data")

# Set mode to GUIDED
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    4  # Guided mode
)

# Takeoff
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    12  # Altitude in meters
)

# Wait for the drone to reach the altitude
time.sleep(10)

# # Circle Parameters
# radius = 0.2  # Radius of the circle in meters
# speed = 0.1  # Speed of the drone in m/s
# altitude = center_z + 10  # Altitude relative to the ground

# # Draw Circle
# for angle in range(0, 361, 5):  # 5-degree increments
#     x = center_x + (radius * cos(radians(angle)))
#     y = center_y + (radius * sin(radians(angle)))
#     z = altitude  # Altitude relative to the ground

#     master.mav.set_position_target_global_int_send(
#         0,  # Time boot ms
#         master.target_system,
#         master.target_component,
#         mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,  # Frame type
#         0b0000111111111000,  # Type mask (only position enabled)
#         int(x * 1e7),  # Latitude in degrees * 1e7
#         int(y * 1e7),  # Longitude in degrees * 1e7
#         int(z * 1e3),  # Altitude in meters * 1e3
#         0,  # vx (ignored)
#         0,  # vy (ignored)
#         0,  # vz (ignored)
#         0,  # afx (ignored)
#         0,  # afy (ignored)
#         0,  # afz (ignored)
#         0,  # yaw (ignored)
#         0  # yaw_rate (ignored)
#     )
#     time.sleep(1)  # Adjust sleep time for desired speed

# Switch to mode circle
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    7  # Circle mode
)

# Return to Launch (RTL)
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
)
