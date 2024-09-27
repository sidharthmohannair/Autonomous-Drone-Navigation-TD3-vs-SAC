import time
from pymavlink import mavutil

# Connect to the drone
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
master.wait_heartbeat()


def wait_for_ack(master, command):
    """ Wait for an ACK from the specified command. """
    while True:
        ack = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack and ack.command == command:
            return ack.result


def print_rc_channels(master):
    rc_channels_raw = master.recv_match(type='RC_CHANNELS', blocking=True, timeout=1)
    if rc_channels_raw:
        print("RC Channels:", [rc_channels_raw.chan1_raw,
                             rc_channels_raw.chan2_raw,
                             rc_channels_raw.chan3_raw,
                             rc_channels_raw.chan4_raw,
                             rc_channels_raw.chan5_raw,
                             rc_channels_raw.chan6_raw,
                             rc_channels_raw.chan7_raw,
                             rc_channels_raw.chan8_raw])
    else:
        print("Failed to get RC_CHANNELS_RAW message")

home_position = None
def get_gps_position(master):
    global_position_msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=1)
    if global_position_msg:
        lat = global_position_msg.lat / 1e7  # Latitude in degrees
        lon = global_position_msg.lon / 1e7  # Longitude in degrees
        alt = global_position_msg.alt / 1e3  # Altitude in meters (above MSL)
        return lat, lon, alt
    else:
        return None, None, None

# Capture home position once
while home_position is None:
    home_position = get_gps_position(master)
    if home_position is not None:
        print(f"Captured home position: Lat: {home_position[0]}, Lon: {home_position[1]}, Alt: {home_position[2]}")
    else:
        print("Waiting for GPS fix...")
    time.sleep(1)


# Switch to GUIDED mode
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    4  # GUIDED mode
)
print("Switching to GUIDED mode")
# wait_for_ack(master, mavutil.mavlink.MAV_CMD_DO_SET_MODE)
print("GUIDED mode set")

# Arm the drone
master.arducopter_arm()
print("Arming motors")
master.motors_armed_wait()
print('Motors armed')


# Define the wait_for_message function
def wait_for_message(master, message_type, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        msg = master.recv_match(type=message_type, blocking=True)
        if msg:
            return msg
    print(f"Timeout waiting for {message_type} message")
    return None

# Request battery status
master.mav.request_data_stream_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_EXTENDED_STATUS,
    1,
    1
)

# Wait for the battery status message
battery_status_msg = wait_for_message(master, 'SYS_STATUS')
if battery_status_msg:
    battery_voltage = battery_status_msg.voltage_battery / 1000.0  # Voltage in volts
    print(f"Battery Voltage: {battery_voltage} V")
else:
    print("Failed to get battery status")



# Takeoff to 10 meters
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
    15  # Altitude in meters
)
print("Taking off to 10 meters")
time.sleep(10)  # Wait for the drone to reach the altitude


# Hover using RC control

# Print RC channels before override
print("RC Channels before override:")
print_rc_channels(master)

# Hover using RC control

master.mav.rc_channels_override_send(
    master.target_system,
    master.target_component,
    0, 0, 1500, 0, 0, 0, 0, 0  # Channel 3 at 1500
)
print("Attempting to hover at 10 meters (overriding RC Channel 3)")

# Wait for a moment to allow the override to take effect
time.sleep(1)

# Print RC channels after override
print("RC Channels after override:")
print_rc_channels(master)

time.sleep(10)  # Hover for 10 seconds

# Switch to CIRCLE mode
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    7  # CIRCLE mode
)
print("Switching to CIRCLE mode")
print("CIRCLE mode set")

# Wait for a few seconds in CIRCLE mode
time.sleep(10)

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
print("Returning to Launch (RTL)")

# Wait for RTL completion and disarm
while True:
    lat, lon, alt = get_gps_position(master)

    if lat is not None and lon is not None:
        # Check for RTL completion (adjust tolerances as needed)
        if abs(lat - home_position[0]) < 0.0001 and abs(lon - home_position[1]) < 0.0001 and abs(alt - home_position[2]) < 0.5:
            print("RTL complete, drone is home!")

            # Ensure the drone is disarmed
            if master.motors_armed():
                print("Forcing disarm...")
                master.arducopter_disarm()
                master.motors_disarmed_wait()
                print("Motors disarmed")

            break  # Exit the loop

    time.sleep(1)  # Check every second

print("Mission complete")