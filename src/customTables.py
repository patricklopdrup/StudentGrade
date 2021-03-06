from prettytable import PrettyTable
from colorama import Fore, Style
import numpy as np
import dataHandling
import sys
import grade
np.set_printoptions(threshold=sys.maxsize)

ROW = 0
COLUMN = 1


def showCsvData(data: np.array) -> None:
    '''
    Show the data of the loaded csv file in a table.
    '''
    rowsToColor = __getIndicesForEvenRows(data)
    table = getDefaultTable(data)
    table = addTableRows(data, table, rowsToColor, Fore.CYAN)
    print(f"\nTable with {dataHandling.getStudentCount(data)} students:")
    print(table)


def __getIndicesForEvenRows(data: np.array) -> np.array:
    return np.arange(0, data.shape[ROW], 2)


def getDefaultTable(data:np.array) -> PrettyTable:
    '''
    Returns a table with the header of the csv file and
    sets 'Name' and 'StudentID' to the left of the column.
    '''
    table = PrettyTable(data.dtype.names)
    table.field_names = data[0]
    table.align['Name'] = 'l'
    table.align['StudentID'] = 'l'
    return table


def addTableRows(data:np.array, table:PrettyTable, rowsToColor = [], color = Fore.CYAN) -> PrettyTable:
    '''
    Adding rows to the table from the data.
    Can also color the rows specified in 'rowsToColor'.
    '''
    count = 0
    for row in data[1:]:
        if count in rowsToColor:
            table.add_row(__colorRow(row, color))
        else:
            table.add_row(row)
        count += 1
    return table


def __colorRow(row: np.array, color: Fore) -> np.array:
    return np.array([color + str(cell) + Style.RESET_ALL for cell in row])


def showErrorTable(data:np.array, errorCoordinates:np.array) -> None:
    '''
    Prints a table with errors shown in red.
    @param errorCoordinates: np.array with the indices of the cells where an error occured.
    '''
    table = getDefaultTable(data)
    table = __createErrorTableRows(data, table, errorCoordinates)
    if not grade.hasAnyError(data):
        print("\nNo errors in table.")
    else:
        print(f"\nTable with {grade.getAmountOfErrors(data)} error(s) " + Fore.RED +  "(red)" + Style.RESET_ALL + ":")
    print(table)


def __createErrorTableRows(data:np.array, table:PrettyTable, errorCoordinates = np.empty((0,2)), color = Fore.RED) -> PrettyTable:
    '''
    Creating rows in the table where error cells are shown in red.
    '''
    count = 1 # header is row 0. So start at 1
    error_count = 0
    for row in data[1:]:
        if count in errorCoordinates[:,ROW]:
            # find where the errors are in the row and add them in red to the table
            errorsInRow = __getAllErrorForRow(count, errorCoordinates)
            table.add_row(__colorCellInRow(row, color, errorsInRow))
            error_count += 1
        else:
            table.add_row(row)
        count += 1
    return table


def __getAllErrorForRow(rowNumber: int, errorCoordinates: np.array) -> np.array:
    return errorCoordinates[errorCoordinates[:,ROW] == rowNumber][:,COLUMN]


def __colorCellInRow(row: np.array, color: Fore, cell_indices: np.array) -> np.array:
    '''
    Color cells in a row.
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
    '''
    Color single cells in a row.
    '''
    errorsInRow = np.array([])
    for index in cell_indices:
        errorsInRow = np.append(errorsInRow, color + str(row[index]) + Style.RESET_ALL)
    return errorsInRow


def showGradeListTable(data: np.array) -> None:
    '''
    Show a table with grades and final grade for all students sorted by name.
    Every other row is colored.
    '''
    dataSorted = __sortDataByName(data)
    dataSorted = grade.addFinalGradesToData(dataSorted)
    rowsToColor = __getIndicesForEvenRows(dataSorted)
    table = getDefaultTable(dataSorted)
    table = addTableRows(dataSorted, table, rowsToColor)
    print(table)


def __sortDataByName(data: np.array) -> np.array:
    columnIndexOfNames = 1
    dataWithOutHeader = data[1:]
    sortedByName = dataWithOutHeader[dataWithOutHeader[:,columnIndexOfNames].argsort()]
    return np.insert(sortedByName, 0, data[0], axis=0)



if __name__ == '__main__':
    data = dataHandling.readDataFromCsvFile('data/test.csv')
    # errors = np.array([
    #     [1,0],
    #     [4,0],
    #     [1,3],
    #     [2,5]
    #     ])
    # np.reshape(errors, (4, 2))
    # print(errors)
    # print()
    # table = getDefaultTable(data)
    # table = __createErrorTableRows(data, table, errors)
    # print(table)

    showGradeListTable(data)
