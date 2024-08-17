from testing.CarManager.car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car('Fiat', 'Panda', 8, 35)

    def test_car_init(self):
        self.assertEqual('Fiat', self.car.make)
        self.assertEqual('Panda', self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(35, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_if_not_new_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        self.assertEqual('Fiat', self.car.make)

    def test_car_make_if_new_value(self):
        self.car.make = 'Uno'
        self.assertEqual('Uno', self.car.make)

    def test_car_model_if_not_new_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
        self.assertEqual('Panda', self.car.model)

    def test_car_model_if_new_value(self):
        self.car.model = 'Punto'
        self.assertEqual('Punto', self.car.model)

    def test_car_fuel_consumption_if_new_value_less_than_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        self.assertEqual(8, self.car.fuel_consumption)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        self.assertEqual(8, self.car.fuel_consumption)

    def test_car_fuel_consumption_if_valid_new_value(self):
        self.car.fuel_consumption = 7
        self.assertEqual(7, self.car.fuel_consumption)

    def test_car_fuel_capacity_if_new_value_less_than_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        self.assertEqual(35, self.car.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        self.assertEqual(35, self.car.fuel_capacity)

    def test_car_fuel_capacity_if_valid_new_value(self):
        self.car.fuel_capacity = 38
        self.assertEqual(38, self.car.fuel_capacity)

    def test_car_fuel_amount_if_new_value_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount= 0

            self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
            self.assertEqual(0, self.car.fuel_amount)

    def test_car_fuel_amount_if_valid_new_value(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_car_refuel_if_fuel_less_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_refuel_if_fuel_is_valid(self):
        new_amount = 10
        self.car.refuel(new_amount)
        self.assertEqual(new_amount, self.car.fuel_amount)

        self.car.refuel(new_amount)
        self.assertEqual(new_amount * 2, self.car.fuel_amount)

    def test_car_refuel_if_fuel_is_valid_fuel_amount_greater_than_capacity_raises(self):
        new_amount = self.car.fuel_capacity + 1
        expected = 35

        self.car.refuel(new_amount)

        self.assertEqual(expected, self.car.fuel_amount)

    def test_car_drive_if_needed_fuel_greater_than_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(20)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_drive_if_enough_fuel_amount(self):
        self.car.refuel(20)
        self.car.drive(100)

        self.assertEqual(12, self.car.fuel_amount)

        self.car.drive(20)
        self.assertEqual(10.4, self.car.fuel_amount)


if __name__ == '__main__':
    main()