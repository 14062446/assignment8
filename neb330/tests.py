import unittest
from Investment import *
from assignment8 import *

list1 = [1, 10, 100, 1000]
list2 = [2, 4, 10, 20]
num1 = 5
num2 = 2.5


class Test(unittest.TestCase):

    
    def test_class(self):
        result1 = Investment(list1, num1)
        result2 = Investment(list2, num1)
        self.assertIsInstance(result1, Investment)
        self.assertIsInstance(result2, Investment)
        self.assertRaises(TypeError, Investment(list1, num2))

 
        
        