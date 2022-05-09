import grade
import random

firstNames = ['John', 'Jane', 'Mary', 'Mark', 'Tom', 'Peter', 'Lars', 'Jenns', 'Helle', 'Patrick', 'Sarah', 'Martin', 'Rasmus', 'Lene', 'Pia', 'Tine']
lastNames = ['Mikkelsen', 'Hansen', 'Jensen', 'Marcussen', 'Nielsen', 'Aagaard', 'Bertelsen', 'Christensen', 'Dahl', 'Eriksen', 'Falken']

def generateLongCsv():
    file = open('data/longtest.csv', 'a')
    for i in range(150):
        number = '%06d' % random.randint(0, 999999)
        studyNumber = 's' + number
        name = random.choice(firstNames) + ' ' + random.choice(lastNames)
        grades = [random.choice(grade.gradeScale) for i in range(8)]
        grades = ','.join(map(str, grades))
        file.write(studyNumber + ',' + name + ',' + grades + '\n')
    file.close()


if __name__ == '__main__':
    ###
    # Uncomment the following line to generate a long csv file.
    ###
    #generateLongCsv()
    print()