from machine import Pin
from time import sleep

class KeyPad:
    def __init__(self, row_pins, col_pins, keypad_mapping):
        # Initialize keypad pins
        row_pins = [Pin(pin, Pin.OUT) for pin in row_pins]
        col_pins = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in col_pins]

        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keypad_mapping = keypad_mapping
    
    # Checks is button is pressed
    def read_key(self):
        for i, row_pin in enumerate(self.row_pins):
            row_pin.value(0)
            for j, col_pin in enumerate(self.col_pins):
                if col_pin.value() == 0:
                    while col_pin.value() == 0:
                        pass
                    sleep(0.2) # Debounce
                    return self.keypad_mapping.get((i, j), None)
            row_pin.value(1)
        # Returns None if no buttons are pressed