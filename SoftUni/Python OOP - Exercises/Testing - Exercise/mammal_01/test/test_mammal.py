from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def test_mammal_init_should_create_proper_object(self):
        name = "Pesho"
        mammal_type = "Mammal_Type"
        sound = "sound"
        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound_return_proper_result(self):
        name = "Pesho"
        mammal_type = "Mammal_Type"
        sound = "sound"
        mammal = Mammal(name, mammal_type, sound)

        actual_result = mammal.make_sound()
        expected_result = f"{name} makes {sound}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_returns_animals(self):
        mammal = Mammal("Name", "Type", "Sound")

        actual_result = mammal.get_kingdom()
        expected_result = "animals"

        self.assertEqual(expected_result, actual_result)

    def test_proper_info_output(self):
        name = "Pesho"
        mammal_type = "Mammal_Type"
        sound = "sound"
        mammal = Mammal(name, mammal_type, sound)

        actual_result = mammal.info()
        expected_result = f"{name} is of type {mammal_type}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
