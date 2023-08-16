# tests/test_spacecraft.py
import unittest
from spacecraft import Spacecraft, Direction

class TestSpacecraft(unittest.TestCase):
    def test_initialization(self):
        spacecraft = Spacecraft()
        self.assertEqual(spacecraft.get_position(), (0, 0, 0))
        self.assertEqual(spacecraft.get_direction(), Direction.N)

class TestSpacecraft(unittest.TestCase):
    # ... (previous code)

    def test_move_forward(self):
        spacecraft = Spacecraft()
        spacecraft.move_forward()
        self.assertEqual(spacecraft.get_position(), (0, 1, 0))

    def test_move_backward(self):
        spacecraft = Spacecraft()
        spacecraft.move_backward()
        self.assertEqual(spacecraft.get_position(), (0, -1, 0))

    def test_move_beyond_galactic_boundaries(self):
        spacecraft = Spacecraft()
        spacecraft.move_backward()  # Initial position: (0, -1, 0)
        spacecraft.move_backward()  # Beyond galactic boundary, should stay at (0, -1, 0)
        self.assertEqual(spacecraft.get_position(), (0, -1, 0))