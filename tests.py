import unittest
from chacalc import *

acc = 1E-3

def err(i,e):
    return f'\nIn {i:.4f}\nExpected {e:.4f}'

class TestChaCalc(unittest.TestCase):
    
    def test_median_simple(self):
        expected = 2
        data = [1,102,2]
        inputed = median(data)
        self.assertLess(abs(inputed - expected), acc, msg=err(inputed,expected))

    def test_median_6(self):
        expected = 1.5
        data = [7,1,2,3,-4,0]
        inputed = median(data)
        self.assertLess(abs(inputed - expected), acc, msg=err(inputed,expected))

    def test_avr(self):
        expected = 35
        data = [1,102,2]
        inputed = avr(data)
        self.assertLess(abs(inputed - expected), acc, msg=err(inputed,expected))

    def test_variance(self):
        expected = 8.67
        data = [-1,4,-3]
        inputed = variance(data)
        self.assertLess(abs(inputed - expected), acc, msg=err(inputed,expected))

    def test_variance(self):
        expected = 8.67
        data = [-1,4,-3]
        inputed = variance(data)
        self.assertLess(abs(inputed - expected), acc, msg=err(inputed,expected))
       

if __name__ == '__main__':
    unittest.main()
