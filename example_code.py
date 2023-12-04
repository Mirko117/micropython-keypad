from time import sleep
from machine import Pin
from keypad import KeyPad

# Set up the keypad
# Replace these pin numbers with your actual wiring
row_pins = [23, 32, 33, 19]
col_pins = [18, 5, 4, 15]

# Map the key positions to their corresponding value
keypad_mapping = ["1","2","3","A",
                  "4","5","6","B",
                  "7","8","9","C",
                  "*","0","#","D"]

keys = KeyPad(row_pins, col_pins, keypad_mapping)

# Main loop that prints value of button you press
while True:
    key = keys.read_key()
    if key is not None:
        print(key)
        sleep(0.3)