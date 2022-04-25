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
    __createErrorTableRows(data, table, errorCoordinates)
    if errorCoordinates.shape[0] == 0:
        print("\nIngen fejl i tabellen.")
    else:
        print(f"\nTabel med {errorCoordinates.shape[0]} fejl " + Fore.RED +  "(rød)" + Style.RESET_ALL + ":")
    print(table)


def __createErrorTableRows(data:np.array, table:PrettyTable, errorCoordinates = np.empty((0,2)), color = Fore.RED) -> PrettyTable:
    count = 1 # header is row 0. So start at 1
    error_count = 0
    for row in data[1:]:
        if count in errorCoordinates[:,ROW]:
            errorsInRow = __getAllErrorForRow(count, errorCoordinates)
            table.add_row(__colorCellInRow(row, color, errorsInRow))
            error_count += 1
        else:
            table.add_row(row)
        count += 1
    return table

def __getAllErrorForRow(rowNumber: int, errorCoordinates: np.array) -> np.array:
    return errorCoordinates[errorCoordinates[:,ROW] == rowNumber][:,COLUMN]


def __colorRow(row: np.array, color: Fore) -> np.array:
    return np.array([color + str(cell) + Style.RESET_ALL for cell in row])


def __colorCellInRow(row: np.array, color: Fore, cell_indices: np.array) -> np.array:
    '''
    Color a single cell in a row.
    '''
    newRow = np.array([], dtype=np.str)
    errorsInRow = __getErrorRowColored(row, color, cell_indices)
    errorCount = 0
    for i, cell in np.ndenumerate(row):
        if i[0] in cell_indices:
            newRow = np.append(newRow, errorsInRow[errorCount])
            errorCount += 1
        else:
            newRow = np.append(newRow, cell)
    return newRow
    
def __getErrorRowColored(row: np.array, color: Fore, cell_indices: np.array) -> np.array:
    errorsInRow = np.array([])
    for index in cell_indices:
        errorsInRow = np.append(errorsInRow, color + str(row[index]) + Style.RESET_ALL)
    return errorsInRow

if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/test.csv')
    errors = np.array([
        [1,0],
        [4,0],
        [1,3],
        [2,5]
        ])
    np.reshape(errors, (4, 2))
    print(errors)
    print()
    table = getDefaultTable(data)
    table = __createErrorTableRows(data, table, errors)
    print(table)

    # table = getDefaultTable(data)
    # table.add_row(__colorCellInRow(data[1], Fore.RED, [0,3]))
    # table.add_row(data[2])
    # print(table)
