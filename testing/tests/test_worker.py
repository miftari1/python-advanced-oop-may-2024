from testing.worker import Worker

from unittest import TestCase, main


class TestWorker(TestCase):
    def setUp(self) -> None:
        self.worker = Worker('TestName', 2000, 10)

    def test_init(self):
        self.assertEqual('TestName', self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_work_energy_less_then_or_equal_raises(self):
        # Energy equals zero
        self.worker.energy = 0
        self.assertEqual(0, self.worker.energy)

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, self.worker.energy)

        # Energy less than zero
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(-1, self.worker.energy)

    def test_worker_work(self):
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

        self.worker.work()
        self.assertEqual(2000, self.worker.money)
        self.assertEqual(9, self.worker.energy)

        result = self.worker.work()
        self.assertEqual(4000, self.worker.money)
        self.assertEqual(8, self.worker.energy)
        self.assertEqual(None, result)

    def test_worker_rest(self):
        self.assertEqual(10, self.worker.energy)
        result = self.worker.rest()
        self.assertEqual(11, self.worker.energy)
        self.assertEqual(None, result)

    def test_worker_get_info(self):
        expected = f'TestName has saved 0 money.'
        result = self.worker.get_info()
        self.assertEqual(expected, result)




if __name__ == '__main__':
    main()