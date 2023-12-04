from machine import Pin
from time import sleep

class KeyPad:
    def __init__(self, row_pins, col_pins, keypad_mapping):
        row_pins = [Pin(pin, Pin.OUT) for pin in row_pins]
        col_pins = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in col_pins]

        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keypad_mapping = keypad_mapping
    
    def read_key(self):
        for i in range(4):
            self.row_pins[i].value(1)
        for j in range(4):
            self.row_pins[j].value(0)
            for i in range(4):
                val = self.col_pins[i].value()
                while self.col_pins[i].value() == 0:
                    pass
                if val == 0:
                    return self.keypad_mapping[i+4*j]
            self.row_pins[j].value(1)
