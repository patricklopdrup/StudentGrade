import dataHandling
import os

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


def printHeaderLine(text:str) -> str:
    textLines = text.split('\n')
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


def loadData():
    printHeaderLine("Load data from a CSV file")
    while True:
        fileName = input('Enter file name: ')
        if fileName == 'q':
            return None
        elif not os.path.isfile(fileName):
            print('File not found! Try again.')
            continue

        return dataHandling.readDataFromCsvFile(fileName)
    

def checkDataError():
    printHeaderLine("Check data error")
    while True:
        data = loadData()
        if data is None:
            return
        print(data.header)
        print(data.grades)