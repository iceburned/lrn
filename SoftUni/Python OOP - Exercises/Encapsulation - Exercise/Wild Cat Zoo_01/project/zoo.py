from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget <= price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if worker_name == w.name:


                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salary = sum(o.salary for o in self.workers)
        if sum_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_care = sum(o.money_for_care for o in self.animals)
        if self.__budget < sum_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals = f'You have {len(self.animals)} animals'
        dkt = {'Cheetah': 0, 'Lion': 0, 'Tiger': 0}
        dkt1 = {'Cheetah': [], 'Lion': [], 'Tiger': []}

        for animal in self.animals:
            dkt[animal.__class__.__name__] += 1
            dkt1[animal.__class__.__name__].append(repr(animal))

        a = '\n'.join(dkt1['Lion'])
        b = '\n'.join(dkt1['Tiger'])
        c = '\n'.join(dkt1['Cheetah'])
        answer = f"{total_animals}\n----- {dkt['Lion']} Lions:\n{a}"
        answer2 = f"\n----- {dkt['Tiger']} Tigers:\n{b}"
        answer3 = f"\n----- {dkt['Cheetah']} Cheetahs:\n{c}"

        return answer + answer2 + answer3

    def workers_status(self):
        total_workers = f"You have {len(self.workers)} workers"
        dkt = {'Keeper': 0, 'Caretaker': 0, 'Vet': 0}
        dkt1 = {'Keeper': [], 'Caretaker': [], 'Vet': []}

        for worker in self.workers:
            dkt[worker.__class__.__name__] += 1
            dkt1[worker.__class__.__name__].append(repr(worker))

        a = '\n'.join(dkt1['Keeper'])
        b = '\n'.join(dkt1['Caretaker'])
        c = '\n'.join(dkt1['Vet'])
        answer = f"{total_workers}\n----- {dkt['Keeper']} Keepers:\n{a}"
        answer2 = f"\n----- {dkt['Caretaker']} Caretakers:\n{b}"
        answer3 = f"\n----- {dkt['Vet']} Vets:\n{c}"

        return answer + answer2 + answer3
