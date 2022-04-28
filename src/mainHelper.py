import dataHandling
import os
import numpy as np
import grade
import customTables as table
from colorama import Fore, Style

LEN_OF_BOX = 65

def printInBox(text:str) -> str:
    textLines = text.split('\n')
    maxLen = max([len(line) for line in textLines])
    box = ''.join(['+'] + ['-'] * LEN_OF_BOX + ['+'])
    padding = int((LEN_OF_BOX - maxLen) / 2)
    print('\n' + box)
    for line in textLines:
        print(' ' * padding + line)
    print(box)


def printHeaderLine(text:str, canGoBack = True) -> str:
    textLines = text.split('\n')
    if canGoBack:
        textLines.append('Press \'q\' to go back')
    box = ''.join(['+'] + ['-'] * LEN_OF_BOX + ['+'])
    print('\n' + box)
    for line in textLines:
        padding = int((LEN_OF_BOX - len(line)) / 2)
        print(' ' * padding + line)
    print(box)


def showInfoText():
    printInBox("[1] Load Data\t[3] Generate Diagrams\t[5] Exit\n"
             + "[2] Check Error\t[4] Show Grade List\t[6] Show Help")


def isExit(input:str) -> bool:
    input = input.lower()
    return input == 'exit' or input == '5'


def loadData() -> np.array:
    printHeaderLine("Load data from a CSV file")
    while True:
        fileName = input('Enter file name: ')
        if fileName == 'q':
            return None
        elif not os.path.isfile(fileName):
            print('File not found! Try again.')
            continue

        return dataHandling.readDataFromCsvFile(fileName)
    

def checkDataError(data:np.array):
    printHeaderLine("Check data error", False)
    errorRows = grade.getIndicesForErrorRows(data)
    table.showErrorTable(data, errorRows)

    
def showGradeListTable(data:np.array):
    while True:
        orderedBy = "name"
        printHeaderLine(f"Grade list ordered by {orderedBy}")
        table.showGradeListTable(data)
        __orderByHelp()
        orderBy = input('Order by: ')
        if orderBy == 'q':
            return None
        

def __orderByHelp() -> None:
    printHeaderLine("Order by:\n[1] StudentId  [2] Name  [3] Final grade")

