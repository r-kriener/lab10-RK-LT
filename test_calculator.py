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
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3),15)
        self.assertEqual(mul(7,3),21)
        self.assertEqual(mul(8,1),8)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(8,4),2)
        self.assertAlmostEqual(div(12,2),6)
        self.assertAlmostEqual(div(24,3),8)

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
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertEqual(hypotenuse(9,12),15)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        with self.assertRaises(ValueError):
            square_root(-3)
        with self.assertRaises(ValueError):
            square_root(-6)
        with self.assertRaises(ValueError):
            square_root(-32)

        # Test basic function
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(49),7)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()