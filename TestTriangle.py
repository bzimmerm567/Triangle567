# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,4), 'Scalene', '1,2,3 should be scalene')

    def testIsoscelessTriangleA(self):
        self.assertEqual(classifyTriangle(2,2,1), 'Isosceles', '2,2,1 should be isosceles')

    def testIsoscelessTriangleB(self): 
        self.assertEqual(classifyTriangle(1,2,2), 'Isosceles', '1,2,2 should be isosceles')

    def testIsoscelessTriangleC(self): 
        self.assertEqual(classifyTriangle(2,1,2), 'Isosceles', '2,1,2 should be isosceles')

    def testUpperBoundsA(self): 
        self.assertEqual(classifyTriangle(201,4,5), 'InvalidInput', 'a above the upper bound should be invalid')

    def testUpperBoundsB(self): 
        self.assertEqual(classifyTriangle(3,201,5), 'InvalidInput', 'b above the upper bound should be invalid')
    
    def testUpperBoundsC(self): 
        self.assertEqual(classifyTriangle(3,4,201), 'InvalidInput', 'c above the upper bound should be invalid')

    def testLowerBoundsA(self): 
        self.assertEqual(classifyTriangle(0,4,5), 'InvalidInput', 'a below the lower bound should be invalid')

    def testLowerBoundsB(self): 
        self.assertEqual(classifyTriangle(3,0,5), 'InvalidInput', 'b below the lower bound should be invalid')
    
    def testLowerBoundsC(self): 
        self.assertEqual(classifyTriangle(3,4,0), 'InvalidInput', 'c below the lower bound should be invalid')

    def testSumTwoSidesLTThirdA(self):
        self.assertEqual(classifyTriangle(3,1,1), 'NotATriangle', 'b + c < a should be invalid')

    def testSumTwoSidesLTThirdB(self):
        self.assertEqual(classifyTriangle(1,3,1), 'NotATriangle', 'a + c < b should be invalid')

    def testSumTwoSidesLTThirdC(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle', 'a + b < c should be invalid')

    def testFloatsInvalid(self):
        self.assertEqual(classifyTriangle(3.5,4.5,5.5), 'InvalidInput', 'Floats should be invalid inputs')

    def testStringsInvalid(self):
        self.assertEqual(classifyTriangle("3","4","5"), 'InvalidInput', 'Strings should be invalid inputs')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()