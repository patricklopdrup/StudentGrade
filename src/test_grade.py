import unittest
import numpy as np
import grade

class TestRoundGrade(unittest.TestCase):     

    def test_roundGrade_comma(self): 
        self.assertEqual(
            np.array_equal(
                np.array([7, 0]),
                grade.roundGrade(np.array([8.2, -0.5]))
            ), True)

    def test_roundGrade_comma2(self):
        self.assertEqual(
            np.array_equal(
                np.array([12, -3]),
                grade.roundGrade(np.array([11.4, -2]))
            ), True)

    def test_roundGrade_sameValue(self):
        self.assertEqual(
            np.array_equal(
                np.array([10, -3]),
                grade.roundGrade(np.array([10, -3]))
            ), True)

    def test_roundGrade_largeValues(self):
        self.assertEqual(
            np.array_equal(
                np.array([12, -3]),
                grade.roundGrade(np.array([100, -300]))
            ), True)
    
    def test_roundGrade_1LowVal(self):
        self.assertEqual(
            np.array_equal(
                np.array([2]),
                grade.roundGrade(np.array([3]))
            ), True)

    def test_roundGrade_1LMidVal(self):
        self.assertEqual(
            np.array_equal(
                np.array([7]),
                grade.roundGrade(np.array([8.5]))
            ), True)

    def test_roundGrade_1LargeValue(self):
        self.assertEqual(
            np.array_equal(
                np.array([10]),
                grade.roundGrade(np.array([11]))
            ), True)

    def test_roundGrade_hej(self):
        self.assertEqual(
            np.array_equal(
                np.array([7, 7, 2]),
                grade.roundGrade(np.array([8.5, 8, 3]))
        ), True)




if __name__ == '__main__':
    unittest.main()