from sphero_sdk import SpheroRvrObserver
import time

# Create a new instance of the SpheroRvrObserver class
rvr = SpheroRvrObserver()

# Connect to the Sphero
rvr.wake()

# Set the LED color to green
rvr.led_control.set_all_leds_color(0, 255, 0)

# Move the Sphero forward for 2 seconds
rvr.drive_control.reset_heading()
rvr.drive_control.go_forward(100)
time.sleep(2)
rvr.drive_control.stop_robot()

# Set the LED color to red
rvr.led_control.set_all_leds_color(255, 0, 0)

# Rotate the Sphero in place for 2 seconds
rvr.drive_control.reset_heading()
rvr.drive_control.turn_left_degrees(90, 50)
time.sleep(2)
rvr.drive_control.stop_robot()

# Put the Sphero to sleep
rvr.sleep()