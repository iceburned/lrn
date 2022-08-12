from unittest import TestCase

from project.plantation import Plantation


class PlantationTest(TestCase):
    SIZE = 8
    WORKER = "worker"

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):

        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertDictEqual({}, self.plantation.plants)
        self.assertListEqual([], self.plantation.workers)

    def test_size_validation_less_than_0(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_len_no_plant(self):
        self.plantation.plants = {"Worker": ["rose"], "Worker2": ["mak"]}
        count = self.plantation.__len__()
        self.assertEqual(2, count)

    def test_hire_worker_exist(self):
        worker = "worker"
        self.plantation.workers.append(worker)
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(worker)
        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker(self):
        result = self.plantation.hire_worker(self.WORKER)
        self.assertEqual("worker successfully hired.", result)
        self.assertEqual(1, len(self.plantation.workers))

    def test_str_workers_and_plants(self):
        self.plantation.hire_worker("Worker")
        self.plantation.plants = {"Worker": ["rose"]}
        result = self.plantation.__str__()
        expect = "Plantation size: 8\nWorker\nWorker planted: rose"
        self.assertEqual(expect, result)

    def test_repr_workers(self):
        self.plantation.hire_worker("Worker")
        self.plantation.plants = {"Worker": ["rose"]}
        result = self.plantation.__repr__()
        expect = "Size: 8\nWorkers: Worker"
        self.assertEqual(expect, result)

    def test_planting_when_worker_not_exist(self):
        with self.assertRaises(ValueError) as error:

            self.plantation.planting("Ivan", "rose")
        self.assertEqual("Worker with name Ivan is not hired!", str(error.exception))

    def test_planting_when_plantation_is_full(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Worker")
        self.plantation.plants = {"Worker": ["rose", "tree"], "Worker2": ["mak"]}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Worker", "mak")
        self.assertEqual("The plantation is full!", str(error.exception))
        self.assertEqual(self.plantation.size, self.plantation.__len__())

    def test_planting_when_plantation_is_full_le(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Worker")
        self.plantation.plants = {"Worker": ["rose", "tree", "lipa"], "Worker2": ["mak"]}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Worker", "mak")
        self.assertEqual("The plantation is full!", str(error.exception))
        self.assertLessEqual(self.plantation.size, self.plantation.__len__())

    def test_planting_when_worker_have_plant(self):
        self.plantation.hire_worker("Worker")
        self.plantation.planting("Worker", "rose")
        result = self.plantation.planting("Worker", "tomatoes")
        self.assertEqual("Worker planted tomatoes.", result)
        self.assertEqual(["rose", "tomatoes"], self.plantation.plants["Worker"])

    def test_planting_when_worker_have_never_plant(self):
        self.plantation.hire_worker("Worker")
        result = self.plantation.planting("Worker", "tomatoes")
        self.assertEqual("Worker planted it's first tomatoes.", result)
        self.assertEqual(["tomatoes"], self.plantation.plants["Worker"])
