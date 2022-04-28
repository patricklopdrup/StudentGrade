import unittest
import numpy as np
import grade


class TestComputeFinalGrade(unittest.TestCase):
    
    def test_computeFinalGrade_1Value(self):
        grades = np.array([[10],
                            [12],
                            [-3]])
        expected = np.array([10, 12, -3])
        self.assertEqual(
            np.array_equal(
                expected,
                grade.computeFinalGrades(grades)
            ), True)

    def test_computeFinalGrade_2Values(self):
        grades = np.array([[10, 7],
                            [12, 4],
                            [4, 2]])
        expected = np.array([10, 12, 4])
        self.assertEqual(
            np.array_equal(
                expected,
                grade.computeFinalGrades(grades)
            ), True)

    def test_computeFinalGrade_3Values(self):
        grades = np.array([[10, 7, 12],
                            [12, 4, 2],
                            [4, 2, 0]])
        expected = np.array([10, 7, 2])
        self.assertEqual(
            np.array_equal(
                expected,
                grade.computeFinalGrades(grades)
            ), True)


class TestFinalGradeHelperMethods(unittest.TestCase):

    def test_withMinus3(self):
        self.assertEqual(
            -3,
            grade.calculateFinalGrade(np.array([10, -3, 12]))
        )

    def test_sizeOne(self):
        self.assertEqual(
            10,
            grade.calculateFinalGrade(np.array([10]))
        )

    def test_doNotCountSmallestValue(self):
        self.assertEqual(
            12,
            grade.calculateFinalGrade(np.array([12, 12, 12, 12, 4]))
        )



if __name__ == '__main__':
    unittest.main()