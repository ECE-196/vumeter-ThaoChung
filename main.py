import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# Setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

# Define LED pins
led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,  # type: ignore
    board.IO34,  # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    
]

# Create a list of LED objects using list comprehension
leds = [DigitalInOut(pin) for pin in led_pins]

# Set direction for each LED
for led in leds:
    led.direction = Direction.OUTPUT

# Define maximum volume based on your microphone sensitivity
MAX_VOL = 40000

# Function to map volume to the number of LEDs to light up
def map_volume_to_leds(vol, max_vol, total_leds):
    return int((vol / max_vol) * total_leds)

# Main loop
while True:
    # Get current microphone value
    current_vol = microphone.value
    
    # Print the current volume for debugging purposes
    print(f"Current Volume: {current_vol}")
    
    # Determine how many LEDs to turn on
    active_led_count = map_volume_to_leds(current_vol, MAX_VOL, len(leds))
    
    # Update the LED statuses based on volume
    for i, led in enumerate(leds):
        led.value = i < active_led_count  # Turn on LEDs up to the active_led_count
    
    # Toggle the state of leds[0] and leds[1]
    leds[0].value = not leds[0].value  # Toggle the first LED
    leds[1].value = not leds[0].value  # Set the second LED opposite to the first

    # Short delay to avoid rapid updates
    sleep(0.05)


    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
