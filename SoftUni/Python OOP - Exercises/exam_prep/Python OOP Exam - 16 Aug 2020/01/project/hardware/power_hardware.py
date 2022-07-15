from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Power', int(floor(capacity * 0.25)), int(floor(memory * 1.75)))
