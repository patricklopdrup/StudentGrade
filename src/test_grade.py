import unittest
import numpy as np
import grade

class TestRoundGrade(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass        

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


class TestFinalGrade(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()