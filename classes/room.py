class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []

    def add_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def get_capacity(self):
        return self.capacity

    def check_capacity(self):
        if len(self.guest_list) > self.capacity:
            return "No entry"
        return "Entry permitted"
