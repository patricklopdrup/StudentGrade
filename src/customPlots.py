import numpy as np
import matplotlib.pyplot as plt
import grade
import dataHandling
import random


def generateFinalGradePlot(data):
    '''
    Generates a bar plot of the distribution of final grades.
    '''
    fig, ax = plt.subplots()
    # Data to use
    grades = grade.gradeScale.astype(str)
    finalGrades = grade.getFinalGradeDestribution(data)
    # Create a bar plot
    ax.bar(grades, finalGrades, color='b')
    ax.set_title('Final grade distribution')
    ax.set_xlabel('Grades')
    ax.set_ylabel('Number of students')
    ax.set_ylim(0)
    barLabels = plt.bar(grades, finalGrades)
    plt.bar_label(barLabels, label_type='edge')
    plt.show()


def generateGradesPerAssignmentPlot(data: np.array):
    '''
    Generates a scatter plot for each grade per assignment.
    It also generates a line plot for the mean of each assignment.
    '''
    grades = dataHandling.getGradesForAssignment(data, 0)
    assignmentCount = dataHandling.getAssignmentCount(data)
    fig, ax = plt.subplots()
    # Scatter plot for grades per assignment
    x = getXValuesForPlot(data)
    y = getYValuesForPlot(data)
    plt.scatter(x, y, color='b', s=10)
    # Scatter plot for mean values
    xMean = range(1, assignmentCount+1)
    yMean = getMeanValuesForPlot(data)
    plt.plot(xMean, yMean, '--', color='r')
    # Set title and labels
    ax.set_title('Grades per assignment')
    ax.set_ylabel('Grades')
    ax.set_xlabel('Assignments')
    plt.legend(['Grades', 'Mean'])
    plt.xticks(np.arange(1, assignmentCount + 1))
    plt.yticks(grade.gradeScale)
    plt.show()


def getXValuesForPlot(data: np.array) -> np.array:
    '''
    Get the x values for the scatter plot for all assignments.
    @return: np.array of floats.
    '''
    xValues = np.array([], dtype=np.float)
    assignmentCount = dataHandling.getAssignmentCount(data)
    for i in range(assignmentCount):
        grades = dataHandling.getGradesForAssignment(data, i)
        xValues = np.append(xValues, getXIndices(grades, i))
    return xValues

def getXIndices(grades: np.array, assignmentIndex: int) -> np.array:
    '''
    Get the x values with a little offset for a single assignment.
    @return: np.array of floats.
    '''
    assignmentIndex += 1
    xIndices = np.array([], dtype=np.float)
    for _ in range(grades.size):
        xIndices = np.append(xIndices, assignmentIndex + getRandomOffset(0.1))
    return xIndices


def getYValuesForPlot(data: np.array) -> np.array:
    '''
    Get the y values for the scatter plot for all assignments.
    @return: np.array of floats.
    '''
    yValues = np.array([], dtype=np.float)
    assignmentCount = dataHandling.getAssignmentCount(data)
    for i in range(assignmentCount):
        grades = dataHandling.getGradesForAssignment(data, i)
        yValues = np.append(yValues, getYIndices(grades))
    return yValues

def getYIndices(grades: np.array) -> np.array:
    '''
    Get the y values with a little offset for a single assignment.
    @return: np.array of floats.
    '''
    newGrades = np.array([], dtype=np.float)
    for g in np.nditer(grades):
        newGrades = np.append(newGrades, g + getRandomOffset(0.3))
    return newGrades


def getRandomOffset(offset:float) -> float:
    return random.uniform(-offset, offset)


def getMeanValuesForPlot(data: np.array) -> np.array:
    '''
    Get the mean values for the line plot for all assignments.
    @return: np.array of floats.
    '''
    meanValues = np.array([], dtype=np.float)
    assignmentCount = dataHandling.getAssignmentCount(data)
    for i in range(assignmentCount):
        meanValues = np.append(meanValues, grade.getMeanValueForAssignment(data, i))
    return meanValues



if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/test.csv')
    #generateFinalGradePlot(data)
    generateGradesPerAssignmentPlot(data)