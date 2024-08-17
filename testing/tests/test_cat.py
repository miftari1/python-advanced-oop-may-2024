from testing.cat import Cat

from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Tom')

    def test_init(self):
        self.assertEqual('Tom', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat_if_fed_raises(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_eat(self):

        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        result = self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)
        self.assertEqual(None, result)

    def test_cat_sleep_if_not_fed_raises(self):
        self.cat.sleepy = True

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertTrue(self.cat.sleepy)

    def test_cat_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True

        result = self.cat.sleep()

        self.assertFalse(self.cat.sleepy)
        self.assertEqual(None, result)



if __name__ == '__main__':
    main()