from testing.List.extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.lst = IntegerList()

    def test_init(self):
        self.assertEqual([], self.lst._IntegerList__data)

        self.lst = IntegerList(4, 12, 3 ,5)
        self.assertEqual([4, 12, 3 ,5], self.lst._IntegerList__data)

        self.lst = IntegerList(4, 'b', 4.2 , 3)
        self.assertEqual([4, 3], self.lst._IntegerList__data)

    def test_integer_list_get_data(self):
        self.lst = IntegerList(4, 12, 3, 5)
        expected = [4, 12, 3, 5]
        result = self.lst.get_data()

        self.assertEqual(expected, result)

    def test_integer_list_add_if_not_integer_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.lst.add('b')

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([], self.lst._IntegerList__data)

    def test_integer_list_add(self):

        result = self.lst.add(2)
        self.assertEqual([2], self.lst._IntegerList__data)
        self.assertEqual([2], result)

    def test_integer_list_remove_index_greater_than_or_equal_to_lenght_list_raises(self):
        # Index is greater than lenght of list
        with self.assertRaises(IndexError) as ex:
            self.lst.remove_index(len(self.lst.get_data()) + 1)

        self.assertEqual("Index is out of range", str(ex.exception))

        # Index equals lenght of list
        with self.assertRaises(IndexError) as ex:
            self.lst.remove_index(len(self.lst.get_data()))

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_integer_list_remove_index(self):
        self.lst = IntegerList(4, 8, 12, 6)
        expected = 8
        result = self.lst.remove_index(1)

        self.assertEqual(expected, result)
        self.assertNotIn(8, self.lst.get_data())

    def test_integer_list_get_if_index_greater_than_or_equal_to_lenght_of_list(self):
        # Index is greater than lenght of list
        with self.assertRaises(IndexError) as ex:
            self.lst.get(len(self.lst.get_data()) + 1)

        self.assertEqual("Index is out of range", str(ex.exception))

        # Index equals lenght of list
        with self.assertRaises(IndexError) as ex:
            self.lst.get(len(self.lst.get_data()))

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_integer_list_get(self):
        self.lst = IntegerList(4, 8, 12, 6)
        expected = 8
        result = self.lst.get(1)

        self.assertEqual(expected, result)

    def test_integer_list_insert_if_index_greater_than_or_equal_to_lenght_of_list(self):
        # Index is greater than lenght of list
        with self.assertRaises(IndexError) as ex:
            self.lst.insert(len(self.lst.get_data()) + 1, 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([], self.lst.get_data())

        # Index equals lenght of list
        with self.assertRaises(IndexError) as ex:
            self.lst.insert(len(self.lst.get_data()), 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([], self.lst.get_data())

    def test_integer_list_insert_if_correct_index_not_integer_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.lst.insert(0, 'b')

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([], self.lst.get_data())

    def test_integer_list_insert(self):
        self.lst = IntegerList(6, 5)
        result = self.lst.insert(0, 2)
        self.assertEqual([2, 6, 5], self.lst.get_data())
        self.assertEqual(None, result)

        self.lst.insert(2, 4)
        self.assertEqual([2, 6, 4, 5], self.lst.get_data())

    def test_integer_list_get_biggest(self):
        self.lst = IntegerList(4, 6, 1, 9)
        result = self.lst.get_biggest()

        self.assertEqual(9, result)
        self.assertEqual([4, 6, 1, 9], self.lst.get_data())

    def test_integer_list_get_index(self):
        self.lst = IntegerList(4, 6, 1, 9)
        result = self.lst.get_index(1)

        self.assertEqual(2, result)


if __name__ == '__main__':
    main()