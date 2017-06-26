import unittest

from main import Car

class TestCar(unittest.TestCase):

    def test_no_wheels(self):
        car = Car()
        self.assertEqual(car.wheels, 4)

    def test_with_wheels(self):
        truck = Car(wheels=6)
        self.assertEqual(truck.wheels, 4)

if __name__ == '__main__':
    unittest.main()
