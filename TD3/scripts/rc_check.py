import time
from pymavlink import mavutil



# Connect to the drone
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
master.wait_heartbeat()

# Arm the drone
master.arducopter_arm()
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

# Set mode to GUIDED
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    4  # GUIDED mode
)
print("Mode set to GUIDED")
time.sleep(2)

# Function to wait for a specific MAVLink message
def wait_for_message(master, message_type, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        msg = master.recv_match(type=message_type, blocking=True)
        if msg:
            return msg
    print(f"Timeout waiting for {message_type} message")
    return None

# Function to verify RC channel overrides
def verify_rc_channels(master, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        msg = master.recv_match(type='RC_CHANNELS', blocking=True)
        if msg:
            print(f"RC Channel 3 value: {msg.chan3_raw}")
            return msg.chan3_raw
    print("Timeout waiting for RC_CHANNELS message")
    return None

# Send RC override command for channel 3
print("Sending RC override command for channel 3 at 1500...")
master.mav.rc_channels_override_send(
    master.target_system,
    master.target_component,
    0, 0, 1500, 0, 0, 0, 0, 0  # Channel 3 at 1500
)


# Wait and verify
time.sleep(2)
chan3_value = verify_rc_channels(master)
set_rc_channel_pwm(master, 3, 1500)  
if chan3_value == 1500:
    print("RC override successful. value is ",chan3_value)
else:
    print("RC override failed or not applied correctly. value is ",chan3_value)

# Continue with additional commands if necessary
