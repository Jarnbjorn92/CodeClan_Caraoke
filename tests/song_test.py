import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song('The Breach', 1)
        self.song_2 = Song('Granite', 1)