from project.worker import Worker


class Vet(Worker):
    def __init__(self, age, name, salary):
        super().__init__(age, name, salary)

