import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Connor", 20)
        self.room = Room(1, 10)

    

    