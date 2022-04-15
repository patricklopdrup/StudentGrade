import numpy as np

gradeScale = np.array([-3, 0, 2, 4, 7, 10, 12])

def roundGrade(grades: np.array) -> np.array:
    '''
    Round an array of grades to the nearest grade in the grade scale.
    '''
    gradesRounded = np.array([], dtype=np.int)
    for grade in grades:
        differenceVector = np.abs(grade - gradeScale)
        minIndex = np.argmin(differenceVector)
        gradesRounded = np.append(gradesRounded, gradeScale[minIndex])
    return gradesRounded


def computeFinalGrades(grades):
    pass
