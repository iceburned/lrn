from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                if r.capacity >= people + r.guests:
                    r.guests += people
                    r.is_taken = True

    def free_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number:
                r.guests = 0
                r.is_taken = False

    def status(self):
        all_guests = sum(_.guests for _ in self.rooms)
        free = []
        taken = []
        [taken.append(_.number) if _.is_taken else free.append(_.number) for _ in self.rooms]
        return f"Hotel {self.name} has {all_guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free))}\n" \
               f"Taken rooms: {', '.join(map(str, taken))}"
