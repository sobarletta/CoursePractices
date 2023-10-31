import unittest
import main

class TestMain(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(main.average_temperature(3, [300, 310, 280]), 296)

    def test_case_2(self):
        self.assertEqual(main.average_temperature(3, [300, 300, 300]), 300)

    def test_case_3(self):
        self.assertEqual(main.average_temperature(1, [100]), 100)

    def test_case_4(self):
        self.assertEqual(main.average_temperature(4, [100, 200, 300, 400]), 250)

    def test_case_5(self):
        self.assertEqual(main.average_temperature(5, [50, 60, 70, 80, 90]), 70)

    def test_case_6(self):
        self.assertEqual(main.average_temperature(2, [1, 99999]), 50000)

if __name__ == '__main__':
    unittest.main()
