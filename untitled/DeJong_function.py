import math
import numpy

class DeJong_function:
    def compute(self, decision_variable, dimensions):
        OverallResult = 0
        for i in range(dimensions):
            Result = decision_variable[i]**2
            OverallResult = OverallResult + Result

        return OverallResult