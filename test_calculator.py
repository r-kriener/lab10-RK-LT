import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(7, 37), 44)
        self.assertEqual(add(4, 4), 8)
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(7, 4), 3)
        self.assertEqual(sub(4, 4), 0)
        self.assertEqual(sub(5, 4), 1)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(8, 2), 3.0)
        self.assertAlmostEqual(log(100, 10), 2.0)
        self.assertAlmostEqual(log(4, 16), 0.25)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10, 1)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()