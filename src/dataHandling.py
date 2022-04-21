import numpy as np



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


def getGradesFromData(data:np.array, assignmentIndex:int):
    '''
    Get the grades for a specific assignment. 0th index.
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