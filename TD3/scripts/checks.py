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

vfr_hud_msg = master.recv_match(type='VFR_HUD', blocking=True, timeout=1)
print(vfr_hud_msg.alt)


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


master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    64  # DISARMED mode
)
master.mav.manual_control_send(
        master.target_system,
        0, 0, 0, 0, 0  # all controls to zero
    )


# 0	COPTER_MODE_STABILIZE	
# 1	COPTER_MODE_ACRO	
# 2	COPTER_MODE_ALT_HOLD	
# 3	COPTER_MODE_AUTO	
# 4	COPTER_MODE_GUIDED	
# 5	COPTER_MODE_LOITER	
# 6	COPTER_MODE_RTL	
# 7	COPTER_MODE_CIRCLE	
# 9	COPTER_MODE_LAND	
# 11	COPTER_MODE_DRIFT	
# 13	COPTER_MODE_SPORT	
# 14	COPTER_MODE_FLIP	
# 15	COPTER_MODE_AUTOTUNE	
# 16	COPTER_MODE_POSHOLD	
# 17	COPTER_MODE_BRAKE	
# 18	COPTER_MODE_THROW	
# 19	COPTER_MODE_AVOID_ADSB	
# 20	COPTER_MODE_GUIDED_NOGPS	
# 21	COPTER_MODE_SMART_RTL	
# 22	COPTER_MODE_FLOWHOLD	
# 23	COPTER_MODE_FOLLOW	
# 24	COPTER_MODE_ZIGZAG	
# 25	COPTER_MODE_SYSTEMID	
# 26	COPTER_MODE_AUTOROTATE	
# 27	COPTER_MODE_AUTO_RTL


