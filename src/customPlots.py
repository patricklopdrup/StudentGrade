from hashlib import new
import numpy as np
import matplotlib.pyplot as plt
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
    data = dataHandling.getGradeMatrixFromData(data, asInt=True)
    hej = dataHandling.getGradesForAssignment(data, 0)
    newGrades = getGradesForPlot(hej)
    print(newGrades)
    fig, ax = plt.subplots()
    x = []
    y = []


def getGradesForPlot(grades: np.array) -> np.array:
    newGrades = np.array([], dtype=np.float)
    for grade in np.nditer(grades):
        newGrades = np.append(newGrades, grade + getRandomOffSet())
    return newGrades


def getRandomOffSet() -> float:
    return random.uniform(-0.1, 0.1)


if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/longtest.csv')
    #generateFinalGradePlot(data)
    generateGradesPerAssignmentPlot(data)