from typing import Tuple, Optional

from project.furniture import Furniture

from unittest import TestCase, main

class TestFurniture(TestCase):
    def setUp(self) -> None:
        self.furniture = Furniture('Chair', 12.4, (20, 40, 60))

    def test_init(self):
        self.assertEqual('Chair', self.furniture.model)
        self.assertEqual(12.4, self.furniture.price)
        self.assertEqual((20, 40, 60), self.furniture.dimensions)
        self.assertTrue(self.furniture.in_stock)
        self.assertFalse(self.furniture.weight)

    def test_attribute_types(self):
        self.furniture.weight = 20.4

        self.assertIsInstance(self.furniture.model, str)
        self.assertIsInstance(self.furniture.price, float)
        self.assertIsInstance(self.furniture.weight, Optional[float])

    def test_furniture_model_setter_if_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = ''

        expected = "Model must be a non-empty string with a maximum length of 50 characters."
        self.assertEqual(expected, str(ex.exception))

        self.assertEqual('Chair', self.furniture.model)

    def test_furniture_model_setter_if_len_greater_than_50_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = ''.join(['a' for _ in range(51)])

        expected = "Model must be a non-empty string with a maximum length of 50 characters."
        self.assertEqual(expected, str(ex.exception))

        self.assertEqual('Chair', self.furniture.model)

    def test_furniture_price_setter_if_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.price = -1

        expected = "Price must be a non-negative number."
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(12.4, self.furniture.price)

    def test_furniture_dimensions_setter_if_len_not_equal_3_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (12, 13)

        expected = "Dimensions tuple must contain 3 integers."
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual((20, 40, 60), self.furniture.dimensions)

        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (12, 13, 14, 15)

        expected = "Dimensions tuple must contain 3 integers."
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual((20, 40, 60), self.furniture.dimensions)

    def test_furniture_dimensions_less_than_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (0, 12, 13)

        expected = "Dimensions tuple must contain integers greater than zero."

        self.assertEqual(expected, str(ex.exception))
        self.assertEqual((20, 40, 60), self.furniture.dimensions)

    def test_furniture_weight_setter_if_not_none_and_less_than_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = -1

        expected = "Weight must be greater than zero."

        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(None, self.furniture.weight)

        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = 0

        expected = "Weight must be greater than zero."

        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(None, self.furniture.weight)

    def test_furniture_available_status_if_available(self):
        expected = f"Model: Chair is currently in stock."
        result = self.furniture.get_available_status()

        self.assertEqual(expected, result)

    def test_furniture_available_status_if_unavailable(self):
        self.furniture.in_stock = False

        expected = f"Model: Chair is currently unavailable."
        result = self.furniture.get_available_status()

        self.assertEqual(expected, result)

    def test_furniture_get_specifications(self):
        # If weight is None
        expected = f"Model: Chair has the following dimensions: " \
                   f"20mm x 40mm x 60mm and weighs: N/A"

        result = self.furniture.get_specifications()

        self.assertEqual(expected, result)

        # If weight is declared
        self.furniture.weight = 50.0
        expected = f"Model: Chair has the following dimensions: " \
                   f"20mm x 40mm x 60mm and weighs: 50.0"

        result = self.furniture.get_specifications()

        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()

