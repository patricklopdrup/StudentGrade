import numpy as np


ROW = 0
COLUMN = 1


def readDataFromCsvFile(fileName: str) -> np.array:
    arr = np.genfromtxt(fileName, delimiter=',', dtype=str)
    return arr
    

def getHeaderValueFromData(data:np.array):
    return data[0]


def getBodyValuesFromData(data:np.array):
    return data[1:]


def getStudyIdsFromData(data:np.array):
    body = getBodyValuesFromData(data)
    return body[:,0]


def getNamesFromData(data:np.array):
    body = getBodyValuesFromData(data)
    return body[:,1]


def getStudentCount(data: np.array) -> int:
    headerRowCount = 1
    return data.shape[ROW] - headerRowCount


def getGradesFromData(data:np.array, assignmentIndex:int):
    '''
    0th index.
    getGradesFromData(data, 0) will give the grades for the first assignment.
    '''
    body = getBodyValuesFromData(data)
    return body[:,assignmentIndex + 2]


def getGradeMatrixFromData(data:np.array):
    '''
    Get the grades for all assignments.
    '''
    body = getBodyValuesFromData(data)
    return body[:,2:]


def mapGradeCoordinateBack(gradeCoordinate:np.array) -> np.array:
    '''
    Map a grade coordinate back to the coordinate in the data.
    '''
    return np.array([gradeCoordinate[ROW] + 1, gradeCoordinate[COLUMN] + 2])



if __name__ == '__main__':
    data = readDataFromCsvFile('data/test.csv')
    print(mapGradeCoordinateBack(np.array([0,0])))