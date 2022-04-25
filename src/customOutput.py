from codecs import getdecoder
from prettytable import PrettyTable
from colorama import Fore, Style
import numpy as np
import dataHandling
import sys
np.set_printoptions(threshold=sys.maxsize)

ROW = 0
COLUMN = 1


def showCsvData(data: np.array) -> None:
    rowsToColor = __getIndicesForEvenRows(data)
    table = getDefaultTable(data)
    table = createTableRows(data, table, rowsToColor, Fore.CYAN)
    print(f"\nTabel med {dataHandling.getStudentCount(data)} studerende:")
    print(table)


def __getIndicesForEvenRows(data: np.array) -> np.array:
    return np.arange(0, data.shape[ROW], 2)


def getDefaultTable(data:np.array) -> PrettyTable:
    table = PrettyTable(data.dtype.names)
    table.field_names = data[0]
    table.align['Name'] = 'l'
    table.align['StudentID'] = 'l'
    return table


def createTableRows(data:np.array, table:PrettyTable, rowsToColor = [], color = Fore.CYAN) -> PrettyTable:
    count = 0
    for row in data[1:]:
        if count in rowsToColor:
            table.add_row(__colorRow(row, color))
        else:
            table.add_row(row)
        count += 1
    return table


def showErrorTable(data:np.array, errorCoordinates:np.array) -> None:
    table = getDefaultTable(data)
    createErrorTableRows(data, table, errorCoordinates)
    print(f"\nTabel med {errorCoordinates.shape[0]} fejl:")
    print(table)


def createErrorTableRows(data:np.array, table:PrettyTable, errorCoordinates = np.empty((0,2), dtype=np.int), color = Fore.RED) -> PrettyTable:
    count = 0
    for row in data[1:]:
        if count in errorCoordinates[:,ROW]:
            table.add_row(__colorCellInRow(row, color, errorCoordinates[errorCoordinates[:,ROW] == count, COLUMN]))
        else:
            table.add_row(row)
        count += 1


def __colorRow(row: np.array, color: Fore) -> np.array:
    return np.array([color + str(cell) + Style.RESET_ALL for cell in row])


def __colorCellInRow(row: np.array, color: Fore, index: int) -> np.array:
    row = np.delete(row, index)
    errorInRow = np.array([color + str(row[index]) + Style.RESET_ALL])
    newRow = np.array([], dtype=np.str)
    ### TODO: Fix this.
    for i, cell in np.ndenumerate(row):
        if i[0] == index:
            newRow = np.append(newRow, errorInRow)
        else:
            newRow = np.append(newRow, cell)
    #row = np.insert(row, index, errorInRow)
    print(newRow)
    return row
    

if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/test.csv')
    __colorCellInRow(data[1], Fore.RED, 1)