"""
Operates a motorized plunger mechanism for the automatic launcher.

## Cycle of Operation
When the program starts, the LED starts as green.

1.  The motor runs continuously to retract a plunger.
2.  When the plunger is fully retracted, it hits a limit switch, which stops the motor. The system is now armed.
3.  Pressing the launch button runs the motor for a moment to release the plunger.
4.  After launch, the limit switch is released, and the cycle repeats from step 1.

The off button can be pressed at any time to stop the program, turning the
status LED to red.
"""

# -----------------------------------------------------------------------------
## IMPORTS
# -----------------------------------------------------------------------------
from machine import Pin
from time import sleep

# -----------------------------------------------------------------------------
## HARDWARE SETUP (GPIO PINS)
# -----------------------------------------------------------------------------
clockwise_motor = Pin(0, Pin.OUT)               # If motor rotates in wrong direction, set this to 1
counter_clockwise_motor = Pin(1, Pin.OUT)       # Motor control pin
green_led = Pin(2, Pin.OUT)                     # LED (HIGH=green, LOW=red)
off_button = Pin(3, Pin.IN, Pin.PULL_DOWN)      # Button to stop the program
button = Pin(4, Pin.IN, Pin.PULL_DOWN)          # Launch button
switch = Pin(5, Pin.IN, Pin.PULL_DOWN)          # Limit switch for plunger
led = Pin(25, Pin.OUT)                          # Onboard LED on the Pico

# -----------------------------------------------------------------------------
## INITIAL STATE
# -----------------------------------------------------------------------------
clockwise_motor.value(0)
reset = False           # Flag to control the main loop
green_led.value(1)      # Start with the status LED as green

# -----------------------------------------------------------------------------
## MAIN LOOP
# -----------------------------------------------------------------------------
while not reset:
    # --- State 1: Plunger is retracted and hits the LIMIT SWITCH ---
    if switch.value():
        # Stop the motor and onboard LED while waiting for launch
        led.value(0)
        counter_clockwise_motor.value(0)

        # Wait here until the 'launch' button is pressed
        while not button.value():
            sleep(0.1)  # Small delay to prevent high CPU usage
            # Check if the 'off' button is pressed to exit the program
            if off_button.value():
                reset = True
                break

        # Once button is pressed, run motor briefly to release the plunger
        led.value(1)
        counter_clockwise_motor.value(1)
        sleep(0.5)

    # --- State 2: Plunger is retracting ---
    else:
        # Run the motor continuously until the limit switch is hit
        led.value(1)
        counter_clockwise_motor.value(1)

    sleep(0.01) # Short delay to stabilize the loop

# -----------------------------------------------------------------------------
## CLEANUP
# -----------------------------------------------------------------------------
# This code runs after the 'off_button' is pressed.
# Turn everything off to return to a safe state.
led.value(0)
green_led.value(0) # Set status LED to red
counter_clockwise_motor.value(0)