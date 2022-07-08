from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for r in self.customers:
            if r.id == customer_id:
                for d in r.rented_dvds:
                    if d.id == dvd_id:
                        return f"{r.name} has already rented {d.name}"

                for disk in self.dvds:
                    if disk.id == dvd_id:
                        if disk.is_rented:
                            return "DVD is already rented"
                        if r.age >= disk.age_restriction:
                            r.rented_dvds.append(disk)
                            disk.is_rented = True
                            return f"{r.name} has successfully rented {disk.name}"
                        else:
                            return f"{r.name} should be at least {disk.age_restriction} to rent this " \
                                   f"movie"

    def return_dvd(self, customer_id, dvd_id):
        for r in self.customers:
            if r.id == customer_id:
                for d in r.rented_dvds:
                    if d.id == dvd_id:
                        r.rented_dvds.remove(d)
                        d.is_rented = False
                        return f"{r.name} has successfully returned {d.name}"
                return f"{r.name} does not have that DVD"

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(x) for x in self.dvds])
