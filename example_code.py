from time import sleep
from machine import Pin
from keypad import KeyPad

# Set up the keypad
# Replace these pin numbers with your actual wiring
row_pins = [23, 32, 33, 19]
col_pins = [18, 5, 4, 15]

# Map the key positions to their corresponding value
keypad_mapping = {
    (0, 0): "1", (0, 1): "2", (0, 2): "3", (0, 3): "A",
    (1, 0): "4", (1, 1): "5", (1, 2): "6", (1, 3): "B",
    (2, 0): "7", (2, 1): "8", (2, 2): "9", (2, 3): "C",
    (3, 0): "*", (3, 1): "0", (3, 2): "#", (3, 3): "D"
}

keys = KeyPad(row_pins, col_pins, keypad_mapping)

# Main loop that prints value of button you press
while True:
    key = keys.read_key()
    if key is not None:
        print(key)
        sleep(0.3)