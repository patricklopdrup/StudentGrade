from prettytable import from_csv
import numpy as np


def showGradeList(grades: np.array) -> None:
    table = from_csv(grades.tolist())
    print(table)
