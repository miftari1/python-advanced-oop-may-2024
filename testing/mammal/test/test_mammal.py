from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Tom', 'cat', 'meow')

    def test_mammal_init(self):
        self.assertEqual('Tom', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        expected = f"Tom makes meow"
        result = self.mammal.make_sound()

        self.assertEqual(expected, result)

    def test_mammal_get_kingdom(self):
        expected = self.mammal._Mammal__kingdom
        result = self.mammal.get_kingdom()

        self.assertEqual(expected, result)

    def test_mammal_info(self):
        expected = f"Tom is of type cat"
        result = self.mammal.info()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
