import numpy as np
import grade
import dataHandling
import mainHelper as helper


while True:
    helper.showInfoText()
    _input = input('What to do: ')

    if helper.isExit(_input):
        print('Bye!')
        break

    elif _input == '1':
        data = helper.loadData()
        print(data.header)