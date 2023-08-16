# spacecraft.py
from enum import Enum

class Direction(Enum):
    N = 0
    S = 1
    E = 2
    W = 3
    Up = 4
    Down = 5

class Spacecraft:
    def __init__(self):
        self.position = (0, 0, 0)
        self.direction = Direction.N

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction
    def move_forward(self):
        x, y, z = self.position
        self.position = (x, y + 1, z)

    def move_backward(self):
        x, y, z = self.position
        self.position = (x, y - 1, z)