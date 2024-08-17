from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    fuel = 30.0
    horse_power = 101.0
    default_consumption = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.default_consumption, self.vehicle.fuel_consumption)

    def test_if_init_values_not_correct_type_raises(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_vehicle_drive_needed_fuel_greater_than_available_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(30)

        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_vehicle_drive_enough_fuel(self):
        needed = self.vehicle.fuel_consumption * 20

        self.vehicle.drive(20)

        available_fuel = self.fuel - needed
        self.assertEqual(available_fuel, self.vehicle.fuel)

    def test_vehicle_refuel_if_fuel_exceeds_raises(self):
        self.vehicle.drive(3)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.vehicle.fuel = self.fuel - (self.default_consumption * 3)

    def test_vehicle_refuel_correct(self):
        self.vehicle.drive(5)

        self.vehicle.refuel(5)

        self.assertEqual(28.75, self.vehicle.fuel)

    def test_vehicle_str_method(self):
        expected = f"The vehicle has 101.0 " \
               f"horse power with 30.0 fuel left and 1.25 fuel consumption"

        result = self.vehicle.__str__()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()

