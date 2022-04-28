import unittest
import numpy as np
import grade
import dataHandling

class TestRoundGrade(unittest.TestCase):

    def setUp(self) -> None:
        self.correct_csv = dataHandling.readDataFromCsvFile('test_data/correct.csv')
        self.float_csv = dataHandling.readDataFromCsvFile('test_data/float_grade.csv')
        self.letter_csv = dataHandling.readDataFromCsvFile('test_data/letter_grade.csv')


    def test_correct_grade(self):
        errors = grade.getIndicesForErrorRows(self.correct_csv)
        self.assertEqual(errors.shape[0], 0)


    def test_float_grade(self):
        errors = grade.getIndicesForErrorRows(self.float_csv)
        self.assertEqual(errors.shape[0], 2)

        errorLocations = np.array([[1,2],[2,3]])
        self.assertEqual(np.array_equal(errors, errorLocations), True)


    def test_letter_grade(self):
        errors = grade.getIndicesForErrorRows(self.letter_csv)
        self.assertEqual(errors.shape[0], 2)

        errorLocations = np.array([[1,4],[2,3]])
        self.assertEqual(np.array_equal(errors, errorLocations), True)


if __name__ == '__main__':
    unittest.main()