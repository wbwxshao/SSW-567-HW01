"""Xueshi Wang SSW 567 HW01
   2019.01.27
"""
import unittest
def classify_triangle(a, b, c):
    """The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, and whether it is a right triangle as well."""
    result = ''
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : #check if triangle is valid
        return False
    else:
        if a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2:    #determine if the triangle is right first
            result = 'right'
        elif a == b and b == c and a == c:
            result = 'equilateral'    #if it is right and euilateral, the result will be right/equilateral
        elif a != b and a != c and b != c:
            result = 'scalene'
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            result = 'isosceles'
        return result
    
    
class Test_classify_triangle(unittest.TestCase):
    def test_case(self):
        """test triangle function"""
        self.assertEqual(classify_triangle(3, 4, 5) , 'right')
        self.assertEqual(classify_triangle(4, 5, 3) , 'right')
        self.assertEqual(classify_triangle(1, 2, 100) , False)  #invalid triangle
        self.assertEqual(classify_triangle(3, 3, 3) , 'equilateral')
        self.assertEqual(classify_triangle(3, 3, 4) , 'isosceles')
         
    def test_case2(self):
        self.assertNotEqual(classify_triangle(3, 3, 3), 'right')
        self.assertNotEqual(classify_triangle(3, 3, 4) , 'equilateral')
        self.assertNotEqual(classify_triangle(1, 2, 100) , 'scalene')
        self.assertNotEqual(classify_triangle(10,10,10),'isoceles')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)