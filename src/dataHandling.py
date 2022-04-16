import numpy as np


class StudentData():
    def __init__(self, header: np.array, grades: np.array):
        self.header = header
        self.grades = grades
    


def readDataFromCsvFile(fileName: str) -> np.array:
    arr = np.genfromtxt(fileName, delimiter=',', dtype=str)
    header = arr[0]
    grades = arr[1:]
    return StudentData(header, grades)
    