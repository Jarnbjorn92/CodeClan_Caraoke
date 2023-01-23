import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 10)
        self.guest = Guest("Connor", 20)
        self.song  = Song("The Breach", 1)

    def test_room_has_a_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_room_has_a_guest(self):
        self.assertEqual(10, self.room.capacity)

    def test_add_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(self.guest, self.room.guest_list[0])

    def test_remove_guest_from_room(self):
        self.room.remove_guest(self.guest)
        self.assertEqual([], self.room.guest_list)

    def test_add_song_to_song_list(self):
        self.room.add_song(self.song)
        self.assertEqual(self.song, self.room.song_list[0])

    def test_check_room_has_capacity(self):
        self.assertEqual(10, self.room.get_capacity())


    # def test_check_room_capacity(self):
    #     self.room.check_capacity(self.room.guest_list)
    #     self.assertEqual("No entry", self.room.guest_list)

