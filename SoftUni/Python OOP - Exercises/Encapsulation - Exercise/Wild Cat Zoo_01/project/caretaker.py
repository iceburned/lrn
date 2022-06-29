from project.worker import Worker


class Caretaker(Worker):
    def __init__(self, age, name, salary):
        super().__init__(age, name, salary)
