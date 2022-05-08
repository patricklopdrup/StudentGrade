from hashlib import new
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import grade
import dataHandling
import random


def generateFinalGradePlot(data):
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
    grades = dataHandling.getGradesForAssignment(data, 0)
    fig, ax = plt.subplots()
    # Data to use
    x = getXValuesForPlot(data)
    y = getYValuesForPlot(data)
    # Create a scatter plot
    plt.scatter(x, y, color='b', s=10)
    ax.set_title('Grades per assignment')
    ax.set_ylabel('Grades')
    ax.set_xlabel('Assignments')
    plt.xticks(np.arange(1, dataHandling.getAssignmentCount(data) + 1))
    plt.yticks(grade.gradeScale)
    plt.show()


def getXValuesForPlot(data: np.array) -> np.array:
    xValues = np.array([], dtype=np.float)
    assignmentCount = dataHandling.getAssignmentCount(data)
    for i in range(assignmentCount):
        grades = dataHandling.getGradesForAssignment(data, i)
        xValues = np.append(xValues, getXIndices(grades, i))
    return xValues

def getXIndices(grades: np.array, assignmentIndex: int) -> np.array:
    assignmentIndex += 1
    xIndices = np.array([], dtype=np.int)
    for _ in range(grades.size):
        xIndices = np.append(xIndices, assignmentIndex + getRandomOffset(0.1))
    print(xIndices)
    return xIndices


def getYValuesForPlot(data: np.array) -> np.array:
    yValues = np.array([], dtype=np.float)
    assignmentCount = dataHandling.getAssignmentCount(data)
    for i in range(assignmentCount):
        grades = dataHandling.getGradesForAssignment(data, i)
        yValues = np.append(yValues, getYIndices(grades))
    return yValues

def getYIndices(grades: np.array) -> np.array:
    newGrades = np.array([], dtype=np.float)
    for g in np.nditer(grades):
        newGrades = np.append(newGrades, g + getRandomOffset(0.3))
    return newGrades


def getRandomOffset(offset:float) -> float:
    return random.uniform(-offset, offset)


if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/test.csv')
    #generateFinalGradePlot(data)
    generateGradesPerAssignmentPlot(data)