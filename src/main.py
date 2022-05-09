import grade
import dataHandling
import mainHelper as helper
import customTables as table
import debug

isDataLoaded = False

while True:
    helper.showInfoText()

    if debug.isDebug:
        data = dataHandling.readDataFromCsvFile('data/test.csv')
        isDataLoaded = True

    _input = input('What to do: ')

    if helper.isExit(_input):
        print('Bye!')
        break

    elif not helper.isValidInput(_input, isDataLoaded):
        helper.printErrorLine('Load data before working with it.')
        continue

    elif _input == '1':
        data = helper.loadData()
        if data is None:
            isDataLoaded = False
            continue
        isDataLoaded = True
        table.showCsvData(data)

    elif _input == '2':
        helper.checkDataError(data)
    
    elif _input == '3':
        if grade.hasAnyError(data):
            helper.printErrorLine()
        else:
            helper.generatePlots(data)

    elif _input == '4':
        if grade.hasAnyError(data):
            helper.printErrorLine()
        else:
            helper.showGradeListTable(data)
    
    else:
        helper.printErrorLine('Unknown command!\nTry again.')