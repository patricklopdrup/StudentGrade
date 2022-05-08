import numpy as np
import grade
import dataHandling
import mainHelper as helper
import customTables as table
import debug


while True:
    helper.showInfoText()

    if debug.isDebug:
        data = dataHandling.readDataFromCsvFile('data/longtest.csv')

    _input = input('What to do: ')

    if helper.isExit(_input):
        print('Bye!')
        break

    elif _input == '1':
        data = helper.loadData()
        if data is None:
            continue
        table.showCsvData(data)

    elif _input == '2':
        helper.checkDataError(data)
    
    elif _input == '3':
        if grade.hasAnyError(data):
            helper.printErrorLine()
        else:
            pass

    elif _input == '4':
        if grade.hasAnyError(data):
            helper.printErrorLine()
        else:
            helper.showGradeListTable(data)