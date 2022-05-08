import numpy as np
import dataHandling


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


def computeFinalGrades(grades: np.array) -> np.array:
    '''
    Calculate the final grades for all students.
    If a student has a grade of -3, then their final grade is -3.
    If only one assignment is present, then the final grade is the grade of that assignment.
    If multiple assignments are present, then the final grade is the mean of the highest M-1 grades.

    @param grades: A matrix of int grades for multiple students.
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


def getIndicesForErrorRows(data: np.array) -> np.array:
    '''
    Print errors in the data.
    Color the errors in red.
    '''
    rowsWithErrors = np.empty((0,2), dtype=np.int)
    rowsWithErrors = np.append(rowsWithErrors, __getDublicatedStudyIdsCoordinates(data), axis=0)
    rowsWithErrors = np.append(rowsWithErrors, __getNonPossibleGradesCoordinates(data), axis=0)
    return rowsWithErrors


def __getDublicatedStudyIdsCoordinates(data: np.array) -> np.array:
    studyIds = dataHandling.getStudyIdsFromData(data)
    dublicatedStudyIdsIndices = np.empty((0,2), dtype=np.int)
    for i in range(len(studyIds)):
        for j in range(len(studyIds)):
            if i != j and studyIds[i] == studyIds[j]:
                coordinate = dataHandling.mapStudyIdCoordinateBack(np.array([i,j]))
                dublicatedStudyIdsIndices = np.append(dublicatedStudyIdsIndices, [coordinate], axis=0)
    return dublicatedStudyIdsIndices
    

def __getNonPossibleGradesCoordinates(data:np.array) -> np.array:
    gradeMatrix = dataHandling.getGradeMatrixFromData(data)
    nonPossibleGradesIndices = np.empty((0,2), dtype=np.int)
    for i in range(gradeMatrix.shape[ROW]):
        for j in range(gradeMatrix.shape[COLUMN]):            
            if not __isPossibleGrade(gradeMatrix[i,j]):
                coordinate = dataHandling.mapGradeCoordinateBack(np.array([i,j]))
                nonPossibleGradesIndices = np.append(nonPossibleGradesIndices, [coordinate], axis=0)
    return nonPossibleGradesIndices

def __isPossibleGrade(grade) -> bool:
    try:
        grade = int(grade)
        return grade in gradeScale
    except ValueError: # if grade is not an integer
        return False


if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/test.csv')
    #print(__getDublicatedStudyIdsCoordinates(data))

    getIndicesForErrorRows(data)