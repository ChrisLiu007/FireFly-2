from math import sin , pi
import numpy


class Michaelwicz_function:
    def compute(self, decision_variable, dimensions):
        OverallResult = 0
        i=1
        #OverallResult= sin (decision_variable[0])* (sin((decision_variable[0]**2)/pi))**2 + sin (decision_variable[1])* (sin((2*decision_variable[1]**2)/pi))**2


        for dim in range(dimensions):
           #X = decision_variable[dim]
           Result = sin(decision_variable[dim]) * ((sin((i*decision_variable[dim]**2) / pi ))** (20))
           OverallResult = OverallResult + Result
           i= i+1

        return -(OverallResult)

