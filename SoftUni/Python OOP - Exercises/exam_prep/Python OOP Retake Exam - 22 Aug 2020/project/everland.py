from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        answer = [_.expenses + _.room_cost for _ in self.rooms]
        return f"Monthly consumption: {answer}$."

    def pay(self):
        pass

    def status(self):
        pass
