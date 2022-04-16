import dataHandling
import os


def showInfoText():
    box = ''.join(['+'] + ['-'] * 51 + ['+'])
    print('\n' + box)
    print("[1] Load Data\t[3] Generate Diagrams\t[5] Exit\n"
          + "[2] Check Error\t[4] Show Grade List\t[6] Show Help")
    print(box)


def isExit(input):
    return input == 'exit' or input == '5'


def loadData():
    while True:
        fileName = input('Enter file name: ')
        if not os.path.isfile(fileName):
            print('File not found! Try again.')
            continue

        return dataHandling.readDataFromCsvFile(fileName)