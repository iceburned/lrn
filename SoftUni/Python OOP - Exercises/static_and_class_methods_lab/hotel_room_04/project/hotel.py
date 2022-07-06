from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum(_.guests for _ in self.rooms)

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                return r.take_room(people)

    def free_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number:
                return r.free_room()

    def status(self):
        free = []
        taken = []
        [taken.append(str(_.number)) if _.is_taken else free.append(str(_.number)) for _ in self.rooms]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free)}\n" \
               f"Taken rooms: {', '.join(taken)}"
