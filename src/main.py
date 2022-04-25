import numpy as np
import grade
import dataHandling
import mainHelper as helper
import customOutput as customOut
import debug


while True:
    helper.showInfoText()

    if debug.isDebug:
        data = dataHandling.readDataFromCsvFile('data/test.csv')

    _input = input('What to do: ')

    if helper.isExit(_input):
        print('Bye!')
        break

    elif _input == '1':
        data = helper.loadData()
        if data is None:
            continue
        customOut.showCsvData(data)

    elif _input == '2':
        helper.checkDataError(data)