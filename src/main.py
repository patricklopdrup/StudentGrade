import numpy as np
import grade


grades = np.matrix([
            [10, 7, 12],
            [12, 4, 2],
            [4, 2, 0],
            [10, 7, -3],
            [12, 10, 2]
        ])

grade.computeFinalGrades(grades)