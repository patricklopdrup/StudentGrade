import numpy as np

ROW = 0
COLUMN = 1
gradeScale = np.array([-3, 0, 2, 4, 7, 10, 12])

def roundGrade(grades: np.array) -> np.array:
    '''
    Round an array of arbitrary grades to the nearest grade in the grade scale.
    '''
    gradesRounded = np.array([], dtype=np.int)
    for grade in grades:
        differenceVector = np.abs(grade - gradeScale)
        minIndex = np.argmin(differenceVector)
        gradesRounded = np.append(gradesRounded, gradeScale[minIndex])
    return gradesRounded


def computeFinalGrades(grades: np.matrix) -> np.array:
    '''
    Calculate the final grades for all students.
    If a student has a grade of -3, then their final grade is -3.
    If only one assignment is present, then the final grade is the grade of that assignment.
    If multiple assignments are present, then the final grade is the mean of the highest M-1 grades.

    @param grades: A matrix of grades for multiple students.
    @return: An array of final grades for each student.
    The array is rounded to the nearest grade in the grade scale.
    '''
    gradesFinal = np.array([])
    studentCount = grades.shape[ROW]

    for student in range(studentCount):
        studentGrades = grades[student]
        gradesFinal = np.append(gradesFinal, calculateFinalGrade(studentGrades))
    return roundGrade(gradesFinal)
    

def calculateFinalGrade(grades: np.array) -> int:
    '''
    Calculate the final grade for a single student.
    '''
    assignmentCount = grades.size
    if assignmentCount == 1:
        return grades[0]
    else:
        return __finalGradeForMultipleAssignments(grades)


def __finalGradeForMultipleAssignments(grades: np.array) -> int:
    if -3 in grades:
        return -3
    else:
        return __finalGradeForMultipleAssignmentsNoMinus3(grades)


def __finalGradeForMultipleAssignmentsNoMinus3(grades: np.array) -> int:
    lowestGradeIndex = np.argmin(grades)
    highestGrades = np.delete(grades, lowestGradeIndex)
    return np.mean(highestGrades)